package com.example.net_mode

import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.os.Build
import android.provider.Settings
import android.telephony.TelephonyManager
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel

class MainActivity: FlutterActivity() {
    private val CHANNEL = "com.netmode.app/radio"

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

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
                else -> result.notImplemented()
            }
        }
    }

    private fun getQuickNetworkSnapshot(context: Context): Map<String, Any> {
        val tm = context.getSystemService(Context.TELEPHONY_SERVICE) as? TelephonyManager
        val carrierName = tm?.networkOperatorName.takeIf { !it.isNullOrEmpty() } ?: "No Carrier"
        
        val networkType = when (tm?.dataNetworkType) {
            TelephonyManager.NETWORK_TYPE_LTE -> "4G LTE"
            TelephonyManager.NETWORK_TYPE_NR -> "5G NR"
            TelephonyManager.NETWORK_TYPE_HSPAP,
            TelephonyManager.NETWORK_TYPE_HSPA,
            TelephonyManager.NETWORK_TYPE_UMTS -> "3G"
            TelephonyManager.NETWORK_TYPE_EDGE,
            TelephonyManager.NETWORK_TYPE_GPRS -> "2G"
            else -> "Cellular / Unknown"
        }

        return mapOf(
            "carrier" to carrierName,
            "networkType" to networkType,
            "simState" to (tm?.simState == TelephonyManager.SIM_STATE_READY)
        )
    }

    private fun triggerRadioActivity(context: Context): Boolean {
        val targets = listOf(
            // 1. هواتف سامسونج (المسار الفعلي المستكشف)
            Intent().setComponent(ComponentName("com.android.phone", "com.android.phone.settings.RadioInfo")),
            // 2. هواتف شاومي وأندرويد الخام (*#*#4636#*#*)
            Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.RadioInfo")),
            // 3. مسار شاشة الاختبار البديلة
            Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.TestingSettings")),
            // 4. التراجع الآمن لإعدادات التجوال والشبكة
            Intent(Settings.ACTION_DATA_ROAMING_SETTINGS)
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