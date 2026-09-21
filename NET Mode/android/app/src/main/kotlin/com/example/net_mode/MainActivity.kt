package com.example.net_mode

import android.Manifest
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.provider.Settings
import android.telephony.TelephonyManager
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel

class MainActivity : FlutterActivity() {
    private val CHANNEL = "com.netmode.app/radio"
    private val READ_PHONE_STATE_REQUEST_CODE = 101

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        // طلب صلاحية READ_PHONE_STATE عند الحاجة (Android 6.0+)
        if (!hasPhonePermission()) {
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.READ_PHONE_STATE),
                READ_PHONE_STATE_REQUEST_CODE,
            )
        }

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler { call, result ->
            when (call.method) {
                "openRadioSettings" -> {
                    val opened = triggerRadioActivity(this)
                    result.success(opened)
                }
                "getInstantNetworkSnapshot" -> {
                    val snapshot = getQuickNetworkSnapshot(this)
                    result.success(snapshot)
                }
                "setNetworkMode" -> {
                    // محاولة تغيير نمط الشبكة برمجياً عبر الـ API الخفي
                    val networkTypeCode = call.argument<Int>("networkTypeCode") ?: 0
                    val applied = trySetNetworkMode(networkTypeCode)
                    if (!applied) {
                        // Fallback: فتح قائمة الراديو لتغيير النمط يدوياً
                        triggerRadioActivity(this)
                    }
                    result.success(applied)
                }
                else -> result.notImplemented()
            }
        }
    }

    private fun hasPhonePermission(): Boolean {
        return ContextCompat.checkSelfPermission(
            this,
            Manifest.permission.READ_PHONE_STATE,
        ) == PackageManager.PERMISSION_GRANTED
    }

    private fun getQuickNetworkSnapshot(context: Context): Map<String, Any> {
        val tm = context.getSystemService(Context.TELEPHONY_SERVICE) as? TelephonyManager

        val carrierName = tm?.networkOperatorName.takeIf { !it.isNullOrEmpty() } ?: "No Carrier"

        val networkType = if (hasPhonePermission()) {
            when (tm?.dataNetworkType) {
                TelephonyManager.NETWORK_TYPE_LTE -> "4G LTE"
                TelephonyManager.NETWORK_TYPE_NR -> "5G NR"
                TelephonyManager.NETWORK_TYPE_HSPAP,
                TelephonyManager.NETWORK_TYPE_HSPA,
                TelephonyManager.NETWORK_TYPE_UMTS -> "3G"
                TelephonyManager.NETWORK_TYPE_EDGE,
                TelephonyManager.NETWORK_TYPE_GPRS -> "2G"
                else -> "Cellular / Unknown"
            }
        } else {
            "Permission Required"
        }

        val simReady = if (hasPhonePermission()) {
            tm?.simState == TelephonyManager.SIM_STATE_READY
        } else {
            carrierName != "No Carrier"
        }

        return mapOf(
            "carrier" to carrierName,
            "networkType" to networkType,
            "simState" to simReady,
        )
    }

    /**
     * يحاول تغيير نمط الشبكة برمجياً عبر الـ Hidden API للـ TelephonyManager.
     * يعمل على أجهزة أندرويد القياسية وبعض أجهزة سامسونج.
     * يتطلب صلاحية MODIFY_PHONE_STATE أو يستخدم ITelephony عبر الـ Reflection.
     * يُرجع true إذا نجح التغيير، وfalse للـ Fallback لقائمة الراديو.
     */
    private fun trySetNetworkMode(networkTypeCode: Int): Boolean {
        val tm = getSystemService(Context.TELEPHONY_SERVICE) as? TelephonyManager ?: return false
        return try {
            // المحاولة الأولى: عبر setPreferredNetworkType المخفية
            val method = tm.javaClass.getDeclaredMethod(
                "setPreferredNetworkType",
                Int::class.javaPrimitiveType,
            )
            method.isAccessible = true
            val resultCode = method.invoke(tm, networkTypeCode) as? Boolean
            resultCode == true
        } catch (_: NoSuchMethodException) {
            trySetNetworkModeViaSubscription(tm, networkTypeCode)
        } catch (_: Exception) {
            false
        }
    }

    /**
     * المحاولة الثانية: عبر setAllowedNetworkTypesForReason أو getPreferredNetworkType
     * المتاحة على أندرويد 12+ وبعض أجهزة سامسونج.
     */
    private fun trySetNetworkModeViaSubscription(tm: TelephonyManager, networkTypeCode: Int): Boolean {
        return try {
            // المحاولة عبر ITelephony AIDL
            val telephonyServiceMethod = tm.javaClass.getDeclaredMethod("getITelephony")
            telephonyServiceMethod.isAccessible = true
            val iTelephony = telephonyServiceMethod.invoke(tm) ?: return false

            val setMethod = iTelephony.javaClass.getDeclaredMethod(
                "setPreferredNetworkType",
                Int::class.javaPrimitiveType,
                Int::class.javaPrimitiveType,
            )
            setMethod.isAccessible = true
            // subId = 1 (SIM 1 الافتراضية)
            setMethod.invoke(iTelephony, 1, networkTypeCode)
            true
        } catch (_: Exception) {
            false
        }
    }

    private fun triggerRadioActivity(context: Context): Boolean {
        val targets = listOf(
            Intent().setComponent(ComponentName("com.android.phone", "com.android.phone.settings.RadioInfo")),
            Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.RadioInfo")),
            Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.TestingSettings")),
            Intent(Settings.ACTION_DATA_ROAMING_SETTINGS),
        )

        for (intent in targets) {
            try {
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                context.startActivity(intent)
                return true
            } catch (_: Exception) {
                continue
            }
        }
        return false
    }
}