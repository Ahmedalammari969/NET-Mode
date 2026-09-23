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
        val sm = context.getSystemService(Context.TELEPHONY_SUBSCRIPTION_SERVICE) as? android.telephony.SubscriptionManager

        // فحص وضع الطيران
        val isAirplaneMode = Settings.Global.getInt(
            context.contentResolver,
            Settings.Global.AIRPLANE_MODE_ON,
            0,
        ) != 0

        // استخراج اسم المشغل من SubscriptionManager أو TelephonyManager
        val activeSub = try {
            if (hasPhonePermission()) sm?.activeSubscriptionInfoList?.firstOrNull() else null
        } catch (_: Exception) {
            null
        }

        var carrierName = activeSub?.displayName?.toString()?.takeIf { it.isNotEmpty() }
        if (carrierName.isNullOrEmpty()) {
            carrierName = activeSub?.carrierName?.toString()?.takeIf { it.isNotEmpty() }
        }
        if (carrierName.isNullOrEmpty()) {
            carrierName = tm?.simOperatorName?.takeIf { it.isNotEmpty() }
        }
        if (carrierName.isNullOrEmpty()) {
            carrierName = tm?.networkOperatorName?.takeIf { it.isNotEmpty() }
        }
        if (carrierName.isNullOrEmpty()) {
            // كود اليمن 421 مع شريحة نشطة -> يمن موبايل
            carrierName = if (activeSub != null || tm?.simState == TelephonyManager.SIM_STATE_READY) "Yemen Mobile" else "No Carrier"
        }

        if (isAirplaneMode) {
            carrierName = "وضع الطيران"
        }

        // فحص نمط الشبكة الفعلي (يدعم CDMA, EVDO, LTE, 5G)
        val rawType = if (tm != null && hasPhonePermission() && !isAirplaneMode) {
            val dataType = tm.dataNetworkType
            if (dataType != TelephonyManager.NETWORK_TYPE_UNKNOWN) dataType else tm.voiceNetworkType
        } else {
            TelephonyManager.NETWORK_TYPE_UNKNOWN
        }

        val networkType = if (isAirplaneMode) {
            "الراديو متوقف (وضع الطيران)"
        } else {
            when (rawType) {
                TelephonyManager.NETWORK_TYPE_NR -> "5G NR"
                TelephonyManager.NETWORK_TYPE_LTE -> "4G LTE"
                TelephonyManager.NETWORK_TYPE_EVDO_0,
                TelephonyManager.NETWORK_TYPE_EVDO_A,
                TelephonyManager.NETWORK_TYPE_EVDO_B,
                TelephonyManager.NETWORK_TYPE_EHRPD,
                TelephonyManager.NETWORK_TYPE_HSPAP,
                TelephonyManager.NETWORK_TYPE_HSPA,
                TelephonyManager.NETWORK_TYPE_HSUPA,
                TelephonyManager.NETWORK_TYPE_HSDPA,
                TelephonyManager.NETWORK_TYPE_UMTS -> "3G"
                TelephonyManager.NETWORK_TYPE_1xRTT,
                TelephonyManager.NETWORK_TYPE_CDMA,
                TelephonyManager.NETWORK_TYPE_EDGE,
                TelephonyManager.NETWORK_TYPE_GPRS,
                TelephonyManager.NETWORK_TYPE_GSM -> "2G / 1xRTT"
                else -> if (carrierName != "No Carrier" && carrierName != "وضع الطيران") "3G" else "Cellular / Unknown"
            }
        }

        val simReady = (tm?.simState == TelephonyManager.SIM_STATE_READY) || (activeSub != null)

        return mapOf(
            "carrier" to carrierName,
            "networkType" to networkType,
            "simState" to simReady,
            "isAirplaneMode" to isAirplaneMode,
        )
    }

    /**
     * يحاول تغيير نمط الشبكة برمجياً عبر الـ Hidden API للـ TelephonyManager.
     * يعمل على أجهزة أندرويد القياسية وبعض أجهزة سامسونج.
     * يتطلب صلاحية MODIFY_PHONE_STATE أو يستخدم ITelephony عبر الـ Reflection.
     * يُرجع true إذا نجح التغيير، وfalse للـ Fallback لقائمة الراديو.
     */
    private fun trySetNetworkMode(networkTypeCode: Int): Boolean {
        // 1. محاولة التغيير عبر صلاحية Root إذا كان الجهاز مروتاً
        if (trySetViaRoot(networkTypeCode)) {
            return true
        }

        // حفظ القيمة في الإعدادات كمرجع للنظام
        trySetViaSettingsGlobal(networkTypeCode)

        // 2. محاولة التغيير عبر TelephonyManager Reflection (يتطلب صلاحيات نظام MODIFY_PHONE_STATE)
        val tm = getSystemService(Context.TELEPHONY_SERVICE) as? TelephonyManager ?: return false
        return try {
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

    private fun trySetViaSettingsGlobal(networkTypeCode: Int): Boolean {
        return try {
            val cr = contentResolver
            val s1 = Settings.Global.putInt(cr, "preferred_network_mode", networkTypeCode)
            Settings.Global.putInt(cr, "preferred_network_mode1", networkTypeCode)
            Settings.Global.putInt(cr, "preferred_network_mode2", networkTypeCode)
            s1
        } catch (_: Exception) {
            false
        }
    }

    private fun trySetViaRoot(networkTypeCode: Int): Boolean {
        return try {
            val process = Runtime.getRuntime().exec(arrayOf("su", "-c", "cmd phone set-preferred-network-type $networkTypeCode"))
            val exitCode = process.waitFor()
            exitCode == 0
        } catch (_: Exception) {
            false
        }
    }

    private fun trySetNetworkModeViaSubscription(tm: TelephonyManager, networkTypeCode: Int): Boolean {
        return try {
            val telephonyServiceMethod = tm.javaClass.getDeclaredMethod("getITelephony")
            telephonyServiceMethod.isAccessible = true
            val iTelephony = telephonyServiceMethod.invoke(tm) ?: return false

            val setMethod = iTelephony.javaClass.getDeclaredMethod(
                "setPreferredNetworkType",
                Int::class.javaPrimitiveType,
                Int::class.javaPrimitiveType,
            )
            setMethod.isAccessible = true
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