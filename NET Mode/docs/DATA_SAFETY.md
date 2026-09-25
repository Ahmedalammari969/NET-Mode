# دليل سلامة البيانات لمتجر Google Play — تطبيق طلباتك (Talabatuk)
# Google Play Console Data Safety Guide — Talabatuk

> وثيقة الامتثال الرسمية لتعبئة قسم **سلامة البيانات (Data Safety Section)** في لوحة تحكم **Google Play Console** لتفادي أي رفض في فحص الأذونات ومراجعة التطبيق.

---

## 1. ملخص سلامة البيانات (Data Safety Overview)

| السؤال في Play Console | الإجابة المعيارية | التوضيح / التبرير |
|---|---|---|
| هل يجمع تطبيقك بيانات المستخدمين أو يشاركها؟ | **لا (No)** | التطبيق يعالج البيانات آنياً على الجهاز محلياً، ولا يرسلها إلى أي خادم خارجي. |
| هل تتم مشاركة بيانات المستخدم مع أطراف ثالثة؟ | **لا (No)** | لا توجد أي مكتبات خارجية (SDKs) أو إعلانات أو تحليلات طرف ثالث. |
| هل يتم تشفير البيانات أثناء النقل (In Transit)؟ | **لا ينطبق (N/A)** | لا يتم نقل أي بيانات مستخدم عبر الإنترنت أو شبكات الاتصال. |
| هل توفر طريقة لطلب حذف البيانات؟ | **نعم (Yes)** | يمكن للمستخدم حذف كافة البيانات وسجل الأنماط مباشرة من داخل التطبيق. |

---

## 2. تفصيل فئات البيانات (Data Types Breakdown)

| فئة البيانات (Data Category) | هل تُجمع؟ | هل تُشارك؟ | الغرض ونوع المعالجة |
|---|---|---|---|
| **الموقع الجغرافي (Location)** | ❌ لا | ❌ لا | يتم فقط قراءة معرف البرج الخلوي الفني (Cell Identity) محلياً دون تحديد موقع GPS. |
| **المعلومات الشخصية (Personal info)** | ❌ لا | ❌ لا | لا يُطلب تسجيل دخول أو اسم أو بريد إلكتروني أو رقم هاتف. |
| **الصور والفيديوهات والملفات** | ❌ لا | ❌ لا | لا يتم الوصول إلى ملفات الوسائط. |
| **جهات الاتصال وسجل المكالمات** | ❌ لا | ❌ لا | لا يتم قراءة سجل المكالمات أو دفتر العناوين إطلاقاً. |
| **معرفات الأجهزة (Device / Other IDs)** | ❌ لا | ❌ لا | لا يتم جمع أو تخزين أو إرسال IMEI أو IMSI أو Android ID. |
| **نشاط التطبيق والتفضيلات (App Activity)** | ⚠️ محلياً فقط | ❌ لا | يُحفظ سجل الأنماط السابقة وآخر نمط شبكة مفضل في ذاكرة الجهاز (`SharedPreferences`) لتسهيل استرجاع الإعدادات، ولا يُرسل خارج الجهاز. |

---

## 3. إقرار الأذونات الحساسة (Sensitive Permission Justification)

### إذن: `android.permission.READ_PHONE_STATE`

عند مراجعة التطبيق في Google Play Console، يجب إدراج التبرير التالي حرفياً:

> **English Reviewer Justification (للمراجعين):**  
> *"The `READ_PHONE_STATE` permission is strictly required for the core functionality of the application, which operates as a cellular network diagnostic and radio mode switcher utility. The permission is exclusively utilized to:  
> 1. Detect the current active cellular network mode (GSM, WCDMA, LTE, NR 5G).  
> 2. Measure real-time signal strength (dBm) and cellular tower technical identity for diagnostic purposes.  
> 3. Verify radio state when switching network modes.  
> The application DOES NOT access, collect, record, or transmit phone numbers, call logs, cellular call status, or device hardware serials/IMEI. All preferences and history are stored strictly on-device using local storage."*

---

## 4. خطوات تعبئة النموذج في Google Play Console (Step-by-Step Submission)

1. الانتقال إلى **محتوى التطبيق (App Content)** > **سلامة البيانات (Data Safety)**.
2. **Data Collection and Security:**
   * اختر **No** للسؤال: "Does your app collect or share any of the required user data types?"
   * أو في حال اختيار الإقرار بسجل الأنماط المحلي:
     * اختر فئة **App info and performance > Other actions**.
     * حدد: **Collected: Yes**, **Shared: No**, **Processed ephemerally: No** (Stored locally on-device).
     * اختر الغرض: **App functionality**.
3. **Data Deletion:**
   * اختر **Yes** لأن المستخدم يستطيع حذف السجل بالكامل من إعدادات التطبيق أو عبر إلغاء تثبيت التطبيق.
4. **ربط سياسة الخصوصية:**
   * قم بإدراج الرابط العام المؤدي إلى ملف `docs/PRIVACY_POLICY.md` في خانة **Privacy Policy URL**.

---

## 5. قائمة التحقق قبل الرفع (Pre-submission Checklist)

- [x] إعلان `READ_PHONE_STATE` محصور في العمليات التشخيصية دون جمع بيانات شخصية.
- [x] عدم وجود حزم تتبع إعلاني أو تحليلي خفية في `pubspec.yaml`.
- [x] خلو الكود من استدعاءات `getDeviceId()` أو `getSubscriberId()` المحظورة.
- [x] توفير زر واضح في واجهة المستخدم لمسح سجل الأنماط (`clearPatternHistory`).
- [x] توافق وثيقة سياسة الخصوصية `PRIVACY_POLICY.md` مع إقرارات `DATA_SAFETY.md`.
