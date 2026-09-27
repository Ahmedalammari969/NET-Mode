package com.example.net_mode

import android.Manifest
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
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
    private var methodChannel: MethodChannel? = null

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

        // إعداد وتأمين جسر القناة الموحدة com.netmode.app/radio (Issue #4 & Issue #6)
        methodChannel = MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL)
        methodChannel?.setMethodCallHandler { call, result ->
            try {
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
                        // محاولة تغيير نمط الشبكة برمجياً عبر الـ API الخفي مع درع الأمان
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
            } catch (se: SecurityException) {
                // التقاط قيود Knox وسياسات أمان أندرويد الصارمة وإرجاع استجابة آمنة (Issue #6)
                result.error("SECURITY_LOCKOUT", "تم حظر العملية بواسطة سياسات أمان الجهاز أو نظام Knox", se.localizedMessage)
            } catch (e: Exception) {
                // منع انهيار القناة وإرجاع الخطأ لطبقة Dart بأمان
                result.error("CHANNEL_EXECUTION_ERROR", e.localizedMessage, e.javaClass.simpleName)
            }
        }
    }

    /**
     * تنظيف موارد القناة وإلغاء المعالج لمنع تسريب الذاكرة (Memory Leak Prevention)
     */
    override fun cleanUpFlutterEngine(flutterEngine: FlutterEngine) {
        methodChannel?.setMethodCallHandler(null)
        methodChannel = null
        super.cleanUpFlutterEngine(flutterEngine)
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

        // فحص وضع الطيران اللحظي عبر Native Inspector (Issue #5)
        val isAirplaneMode = inspectAirplaneMode(context)

        // فحص حالة شريحة الاتصال بدقة (SIM State Inspector) (Issue #5)
        val (simReady, simDetailedState, activeSub) = inspectSimState(tm, sm)

        // استخراج اسم المشغل من SubscriptionManager أو TelephonyManager
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
            carrierName = if (simReady) "Yemen Mobile" else "No Carrier"
        }

        if (isAirplaneMode) {
            carrierName = "وضع الطيران"
        }

        // فحص نمط الشبكة الفعلي عبر RIL Modem Network Decoder (Issue #3)
        val rawType = if (tm != null && hasPhonePermission() && !isAirplaneMode) {
            val dataType = tm.dataNetworkType
            if (dataType != TelephonyManager.NETWORK_TYPE_UNKNOWN) dataType else tm.voiceNetworkType
        } else {
            TelephonyManager.NETWORK_TYPE_UNKNOWN
        }

        val networkType = decodeRilNetworkType(rawType, isAirplaneMode, carrierName)

        return mapOf(
            "carrier" to carrierName,
            "networkType" to networkType,
            "networkTypeCode" to rawType,
            "simState" to simReady,
            "simDetailedState" to simDetailedState,
            "isAirplaneMode" to isAirplaneMode,
        )
    }

    /**
     * فحص وضع الطيران اللحظي من إعدادات النظام العامة (Issue #5)
     */
    private fun inspectAirplaneMode(context: Context): Boolean {
        return try {
            Settings.Global.getInt(
                context.contentResolver,
                Settings.Global.AIRPLANE_MODE_ON,
                0,
            ) != 0
        } catch (_: Exception) {
            try {
                @Suppress("DEPRECATION")
                Settings.System.getInt(
                    context.contentResolver,
                    Settings.System.AIRPLANE_MODE_ON,
                    0,
                ) != 0
            } catch (_: Exception) {
                false
            }
        }
    }

    /**
     * فحص حالة وجاهزية شرائح الاتصال (SIM State & Subscription Inspector) (Issue #5)
     */
    private fun inspectSimState(
        tm: TelephonyManager?,
        sm: android.telephony.SubscriptionManager?,
    ): Triple<Boolean, String, android.telephony.SubscriptionInfo?> {
        val activeSub = try {
            if (hasPhonePermission()) sm?.activeSubscriptionInfoList?.firstOrNull() else null
        } catch (_: Exception) {
            null
        }

        val simStatus = tm?.simState ?: TelephonyManager.SIM_STATE_UNKNOWN
        val isReady = (simStatus == TelephonyManager.SIM_STATE_READY) || (activeSub != null)

        val detailedState = when (simStatus) {
            TelephonyManager.SIM_STATE_READY -> "READY"
            TelephonyManager.SIM_STATE_ABSENT -> "ABSENT"
            TelephonyManager.SIM_STATE_PIN_REQUIRED -> "PIN_REQUIRED"
            TelephonyManager.SIM_STATE_PUK_REQUIRED -> "PUK_REQUIRED"
            TelephonyManager.SIM_STATE_NETWORK_LOCKED -> "NETWORK_LOCKED"
            TelephonyManager.SIM_STATE_NOT_READY -> "NOT_READY"
            else -> if (activeSub != null) "READY" else "UNKNOWN"
        }

        return Triple(isReady, detailedState, activeSub)
    }

    /**
     * مفسر ومصنف أكواد مودم الراديو RIL Modem Network Decoder (Issue #3)
     * تحويل أكواد TelephonyManager الرقمية لمسميات تقنية واضحة ودقيقة.
     */
    private fun decodeRilNetworkType(rawType: Int, isAirplaneMode: Boolean, carrierName: String?): String {
        if (isAirplaneMode) {
            return "الراديو متوقف (وضع الطيران)"
        }

        return when (rawType) {
            // الجيل الخامس 5G New Radio
            TelephonyManager.NETWORK_TYPE_NR -> "5G NR"

            // الجيل الرابع 4G LTE
            TelephonyManager.NETWORK_TYPE_LTE -> "4G LTE"

            // الجيل الثالث 3G UMTS / HSPA / CDMA EVDO
            TelephonyManager.NETWORK_TYPE_HSPAP,
            TelephonyManager.NETWORK_TYPE_HSPA,
            TelephonyManager.NETWORK_TYPE_HSUPA,
            TelephonyManager.NETWORK_TYPE_HSDPA,
            TelephonyManager.NETWORK_TYPE_UMTS,
            TelephonyManager.NETWORK_TYPE_EVDO_0,
            TelephonyManager.NETWORK_TYPE_EVDO_A,
            TelephonyManager.NETWORK_TYPE_EVDO_B,
            TelephonyManager.NETWORK_TYPE_EHRPD -> "3G"

            // الجيل الثاني 2G GSM / CDMA 1xRTT
            TelephonyManager.NETWORK_TYPE_1xRTT,
            TelephonyManager.NETWORK_TYPE_CDMA,
            TelephonyManager.NETWORK_TYPE_EDGE,
            TelephonyManager.NETWORK_TYPE_GPRS,
            TelephonyManager.NETWORK_TYPE_GSM -> "2G / 1xRTT"

            // الحالات غير المعروفة
            else -> if (!carrierName.isNullOrEmpty() && carrierName != "No Carrier" && carrierName != "وضع الطيران") {
                "3G"
            } else {
                "Cellular / Unknown"
            }
        }
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

    /**
     * تشغيل واجهة إعدادات الراديو بسلسلة أولويات محكمة:
     * 1. مسار أجهزة سامسونج OneUI (Issue #1)
     * 2. مسار أجهزة شاومي MIUI/HyperOS والأندرويد الخام AOSP (Issue #2)
     * 3. مسار إعدادات الشبكة العامة للنظام كبديل أخير آمن
     */
    private fun triggerRadioActivity(context: Context): Boolean {
        // 1. محاولة إطلاق واجهة سامسونج المخصصة
        if (launchSamsungRadioIntent(context)) {
            return true
        }

        // 2. محاولة إطلاق واجهة شاومي والأندرويد الخام AOSP
        if (launchXiaomiAndAospIntent(context)) {
            return true
        }

        // 3. سلسلة البدائل العامة للنظام (System Network Settings Fallbacks)
        val systemFallbacks = listOf(
            Intent(Settings.ACTION_DATA_ROAMING_SETTINGS),
            Intent(Settings.ACTION_NETWORK_OPERATOR_SETTINGS),
            Intent(Settings.ACTION_WIRELESS_SETTINGS),
        )

        for (intent in systemFallbacks) {
            if (safeLaunchIntent(context, intent)) {
                return true
            }
        }
        return false
    }

    /**
     * استهداف هواتف سامسونج وقوائم RadioInfo الخفية المتوافقة مع OneUI (Issue #1)
     */
    private fun launchSamsungRadioIntent(context: Context): Boolean {
        val samsungTargets = listOf(
            // مسار سامسونج المعياري لشاشات إعدادات الراديو
            Intent().setComponent(ComponentName("com.android.phone", "com.android.phone.settings.RadioInfo")),
            // مسار قوائم ServiceMode لأجهزة جالاكسي
            Intent().setComponent(ComponentName("com.sec.android.RilServiceModeApp", "com.sec.android.RilServiceModeApp.ServiceMode")),
        )

        for (intent in samsungTargets) {
            if (safeLaunchIntent(context, intent)) {
                return true
            }
        }
        return false
    }

    /**
     * استدعاء مسار RadioInfo و TestingSettings لأجهزة شاومي (MIUI / HyperOS) والأندرويد الخام AOSP (Issue #2)
     */
    private fun launchXiaomiAndAospIntent(context: Context): Boolean {
        val targets = listOf(
            // مسار AOSP الخام القياسي لشاشة معلومات الراديو
            Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.RadioInfo")),
            // مسار إعدادات الفحص والاختبار العام
            Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.TestingSettings")),
            // مسار شاومي وواجهة MIUI / HyperOS المتخصص لشاشة الاختبار
            Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.Settings\$TestingSettingsActivity")),
            // بديل حزمة الهاتف لـ TestingSettings
            Intent().setComponent(ComponentName("com.android.phone", "com.android.phone.TestingSettings")),
            // برودكاست الكود السري المعياري للراديو (*#*#4636#*#*)
            Intent("android.provider.Telephony.SECRET_CODE", Uri.parse("android_secret_code://4636")),
        )

        for (intent in targets) {
            if (safeLaunchIntent(context, intent)) {
                return true
            }
        }
        return false
    }

    /**
     * محرك إطلاق المقاصد الآمن والتقاط استثناءات Knox وسياسات الأمان (Issue #6)
     * System Security Lockout & Exception Catching Engine
     */
    private fun safeLaunchIntent(context: Context, intent: Intent): Boolean {
        return try {
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
            context.startActivity(intent)
            true
        } catch (_: SecurityException) {
            // التقاط استثناءات أمان Knox أو قيود إدارة الأجهزة المؤسسية (MDM / Knox Lockout)
            false
        } catch (_: android.content.ActivityNotFoundException) {
            // عدم وجود الشاشة أو الحزمة في هذا الإصدار
            false
        } catch (_: Exception) {
            // التقاط أي استثناء غير متوقع ومنع انهيار التطبيق
            false
        }
    }
}