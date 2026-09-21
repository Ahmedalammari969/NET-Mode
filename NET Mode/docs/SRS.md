
# مواصفات متطلبات البرمجيات (Software Requirements Specification - SRS)
## المشروع: NET Mode (Advanced Cellular Network & Radio Testing Suite)
**المعيار المعتمد:** مستند إلى معيار IEEE Std 830-1998  
**الإصدار:** 2.6.0 (Unified Master Production SRS)  
**الحالة:** معتمد هندسياً للمتجر والتحكيم (Approved)  
**فريق العمل الهندسي:**
1. **أحمد العماري** (Native Android & Hardware Platform Engineer)
2. **محمد الدعيس** (Core Domain & Architecture Engineer)
3. **يوسف خيري** (Data Layer & Telephony Storage Engineer)
4. **مؤيد الصوفي** (UI/UX & Presentation State Engineer)

---

## 1. المقدمة ونطاق المشروع (Introduction & Project Scope)

### 1.1 وصف المشكلة الحقيقية (Problem Statement)
يواجه مستخدمو الهواتف الذكية وفنيو الاتصالات صعوبة بالغة وتشتتاً تقنياً عند محاولة ضبط نمط الشبكة الخلوية (مثل تثبيت الاتصال على 4G LTE فقط لمنع تراجع الهاتف التلقائي إلى 3G عند انخفاض الإشارة، أو التثبيت على 2G/3G لتوفير استهلاك البطارية). 
تعتمد الطرق التقليدية في أندرويد على إدخال أكواد اتصال هندسية معقدة عبر الـ Dialer مثل `*#*#4636#*#*`، والتي أصبحت محجوبة أو معطلة برمجياً من قبل معظم الشركات المصنعة (مثل Samsung OneUI و Xiaomi MIUI/HyperOS) ومشغلي الاتصالات، مما يحرم المستخدم والمطور من التحكم في استقرار الاتصال وسرعته.

### 1.2 الحل المقترح (Proposed Solution)
تطوير تطبيق محمول احترافي عالي الكفاءة مبني بإطار عمل Flutter بلغة Dart، مدعوماً بطبقة أصيلة متقدمة بلغة Kotlin في بيئة أندرويد، وفق مبادئ المعمارية النظيفة (Clean Architecture) ومبادئ SOLID الهندسية. 
يوفر التطبيق واجهة مستخدم تفاعلية متطورة بأسلوب داكن (Dark Slate / Cyberpunk) تتيح التبديل بنقرة زر واحدة بين الأنماط المختلفة عبر إطلاق نيات برمجية مباشرة (Explicit Native Intents) تتخطى قيود لوحة الاتصال، مع قراءة القياسات الحقيقية للإشارة (RIL Telemetry) وتخزين التفضيلات وسجل الأنماط محلياً دون أي خوادم خارجية.

### 1.3 المستخدمون المستهدفون (Target Users)
- **مطورو ومبرمجو تطبيقات الهواتف ومهندسو الفحص (Mobile App Developers & QA Engineers):** 
  - محاكاة واختبار سلوك التطبيقات ومزامنة البيانات في بيئات شبكية حقيقية مختلفة (تثبيت 2G/3G لاختبار زمن الاستجابة البطيء وحالات ضعف التغطية، أو تثبيت 4G/5G لاختبار البث الحي والـ WebSockets).
  - فحص استجابة آليات إعادة المحاولة (Retry Logic) واستعادة الاتصال بعد فقدان الإشارة دون الحاجة لشبكات افتراضية أو محاكيات ثقيلة.
- **سكان المناطق ذات التغطية المتذبذبة:** لمنع نزول التغطية تلقائياً من 4G/LTE إلى 3G أثناء تصفح الإنترنت أو العمل.
- **مجتمع ألعاب الأونلاين (Mobile Gamers):** لتثبيت واستقرار زمن الاستجابة (Ping) ومنع انقطاع الاتصال المفاجئ أثناء المباريات.
- **فنيو ومهندسو الشبكات الميدانيون (RF Field Technicians):** لقراءة حالة المودم الفعلي، نوع المشغل، والتردد الخلوي بدقة لحظية.
- **المستخدمون الراغبون في ترشيد الموارد:** التبديل السريع إلى 2G/3G لخفض استهلاك البطارية عند عدم الحاجة لبيانات سريعة.

### 1.4 حدود ونطاق العمل (Project Scope Boundaries)
* **داخل النطاق (In-Scope):**
  - فحص واكتشاف حالة المودم، مشغل الخدمة (Carrier)، ونوع الشبكة الحالية (5G NR, 4G LTE, 3G HSPA, 2G GSM, Wi-Fi, No Service).
  - توفير اختصارات مباشرة وآمنة لفتح شاشات هندسة الراديو (Hidden RadioInfo Activities) لسامسونج، شاومي، وأندرويد الخام.
  - حفظ أنماط الشبكة المفضلة محلياً كـ Profiles مسترجعة تلقائياً.
  - دعم مؤشرات استقرار الاتصال وسجل التبديل اللحظي للتغطية لاختبارات المطورين.
  - معالجة حالات عدم توفر الشريحة، وضع الطيران، وحظر الحماية الأمنية للنظام.
* **خارج النطاق (Out-of-Scope):**
  - كسر حماية النظام الإجباري (Rooting) في الأجهزة المقفلة كلياً على مستوى الهاردوير من المصنع.
  - دعم بيئة iOS نظراً لإغلاق شركة Apple لطبقات الـ Cellular Core APIs بشكل صارم ومنع أي وصول خارجي لإعدادات الراديو.

---

## 2. المعمارية البرمجية ومصفوفة التوافق (Architecture & Compatibility)

### 2.1 منظور وهيكلية النظام (System Architecture Perspective)
تم تقسيم النظام إلى أربع طبقات هندسية صارمة ومنفصلة المسؤوليات لتفادي الاعتماديات المتبادلة:


```

+---------------------------------------------------------------------------------+
|                    Presentation Layer (مؤيد الصوفي)                            |
|        - ThemeConfig (Cyberpunk/Dark Slate), HomeScreen, StatusCards            |
+----------------------------------------+----------------------------------------+
|
v
+---------------------------------------------------------------------------------+
|                      Domain Layer (محمد الدعيس)                                 |
|  - Entities: NetworkInfo, NetworkMode, SignalStrengthMetrics                    |
|  - Contracts: NetworkRepository                                                 |
|  - UseCases: GetSnapshotUseCase, OpenRadioSettingsUseCase, PresetManagerUseCase |
+----------------------------------------+----------------------------------------+
|
v
+---------------------------------------------------------------------------------+
|                       Data Layer (يوسف خيري)                                   |
|  - NetworkRepositoryImpl, RadioDeviceDataSourceImpl, LocalPreferencesDataSource |
|  - Failures & Exception Handlers, Security Policy Mappings                      |
+----------------------------------------+----------------------------------------+
| (MethodChannel: com.netmode.app/radio)
v
+---------------------------------------------------------------------------------+
|                  Native Platform Layer (أحمد العماري)                           |
|  - MainActivity.kt, TelephonyManager, RIL Mapping Engine, Samsung/Xiaomi Intents|
+---------------------------------------------------------------------------------+

```

### 2.2 مصفوفة البدائل وسلسلة الاستدعاء الذكية (OEM Fallback Engine Matrix)
تلتزم طبقة المنصة بسلسلة استدعاءات تعاقبية تمنع انهيار التطبيق مهما كانت واجهة المصنّع:

| المصنّع المستهدف | الواجهة الأساسية (Primary Component) | المسار البديل الأول (Fallback 1) | المسار البديل الثاني (Fallback 2) |
| :--- | :--- | :--- | :--- |
| **Samsung (OneUI)** | `com.android.phone.settings.RadioInfo` | `com.samsung.android.app.telephonyui` | `android.settings.NETWORK_OPERATOR_SETTINGS` |
| **Xiaomi (MIUI/HyperOS)** | `com.android.settings.RadioInfo` | `com.android.settings.TestingSettings` | `android.settings.DATA_ROAMING_SETTINGS` |
| **Stock / Pixel / Moto** | `com.android.settings.RadioInfo` | Intent Action: `TESTING` | `android.settings.WIRELESS_SETTINGS` |
| **أجهزة أخرى / غير معروف** | فحص حزمة التثبيت الافتراضية | تشغيل نافذة إعدادات الشبكة العامة | تنبيه المستخدم عبر SnackBar توجيهي |

---

## 3. المتطلبات الوظيفية الشاملة (Functional Requirements)
موزعة بالتساوي ومطابقة بالكامل لقصص المستخدمين الـ 24 المعتمدة:

### 3.1 وحدة المنصة وهندسة الراديو (Platform & Native Module) — [أحمد العماري]
- **FR-01 (مطابق لـ US-01): استدعاء قائمة الراديو لهواتف سامسونج**  
  إطلاق نية برمجية صريحة للمكون `com.android.phone/com.android.phone.settings.RadioInfo` براية `FLAG_ACTIVITY_NEW_TASK`.
- **FR-02 (مطابق لـ US-02): مسار النية البديل لأجهزة شاومي والأندرويد الخام**  
  تشغيل مسارات `com.android.settings.RadioInfo` وبديل `TestingSettings` في حال تعذر مسار سامسونج.
- **FR-03 (مطابق لـ US-03): قراءة وتصنيف نوع اتصال المودم الحقيقي (RIL)**  
  استخراج نوع الاتصال من `TelephonyManager.getDataNetworkType` وتصنيف الأكواد لبيانات واضحة (4G LTE, 5G NR, 3G, 2G).
- **FR-04 (مطابق لـ US-04): قناة اتصال آمنة ومستقرة عبر MethodChannel**  
  تأسيس قناة `com.netmode.app/radio` مع ضمان عزل الاستدعاءات عن الـ UI Thread لتفادي تجمد الشاشة.
- **FR-05 (مطابق لـ US-05): فحص حالة الشريحة SIM ووضع الطيران محلياً**  
  التحقق من `SIM_STATE_READY` وحالة `AIRPLANE_MODE_ON` وإرجاع النتائج في كائن موحد.
- **FR-06 (مطابق لـ US-06): اعتراض أخطاء حظر النظام والتحصين الأمني**  
  التقاط استثناءات `SecurityException` الناتجة عن Knox أو واجهات الحماية وتمرير قيمة `false` لإعلام الواجهة بأمان.

### 3.2 وحدة النطاق والمعمارية المجردة (Core Domain Module) — [محمد الدعيس]
- **FR-07 (مطابق لـ US-07): كيان معلومات الشبكة اللحظية (NetworkInfo)**  
  بناء كيان Dart نقي يحمل خصائص غير قابلة للتعديل (`carrier`, `networkType`, `isSimReady`, `isAirplaneMode`) مع المساواة القيمية.
- **FR-08 (مطابق لـ US-08): كيان أنماط الشبكة القياسية (NetworkMode)**  
  تعريف كيان يحتوي الأنماط المتاحة (LTE Only, NR Only, GSM Only, Auto) وأكواد RIL المناظرة لكل وضع لدعم سيناريوهات فحص التطبيقات للمطورين.
- **FR-09 (مطابق لـ US-09): صياغة عقد المستودع المجرد (NetworkRepository)**  
  توفير واجهة برمجية مجردة تفصل تماماً بين متطلبات الأعمال وتفاصيل المنصات وقواعد البيانات.
- **FR-10 (مطابق لـ US-10): حالة استخدام جلب قياسات الشبكة اللحظية**  
  بناء حالة استخدام مستقلة تطبق `call()` لجلب `NetworkInfo` وفق مبدأ المسؤولية الواحدة.
- **FR-11 (مطابق لـ US-11): حالة استخدام فتح إعدادات الراديو**  
  بناء كلاس مستقل يوجه أمر فتح الإعدادات ويستلم نتيجة الفتح لتمريرها لطبقة العرض.
- **FR-12 (مطابق لـ US-12): بيئة اختبارات الوحدة الآلية الشاملة**  
  توفير تغطية اختبارات بنسبة نجاح 100% لكافة كيانات وحالات استخدام طبقة النطاق باستخدام الـ Mock Repositories.

### 3.3 وحدة البيانات والتخزين المحلي والأذونات (Data & Storage Module) — [يوسف خيري]
- **FR-13 (مطابق لـ US-13): كلاس مصدر بيانات استدعاء القناة الأصلية**  
  تنفيذ `RadioDeviceDataSourceImpl` مع التقاط أخطاء `PlatformException` وإرجاع بيانات افتراضية آمنة تمنع الـ Crash.
- **FR-14 (مطابق لـ US-14): كلاس المستودع الفعلي (NetworkRepositoryImpl)**  
  تنفيذ عقد `NetworkRepository` وتحويل خرائط البيانات القادمة من القناة إلى كيانات نطاقية معتمدة.
- **FR-15 (مطابق لـ US-15): التخزين المحلي لتفضيلات وسجل الأنماط**  
  حفظ واسترجاع النمط المفضل للمستخدم وسجل التبديل في الذاكرة المحلية للجهاز لإعادة تطبيقه تلقائياً عند الاختبار والاستخدام اليومي.
- **FR-16 (مطابق لـ US-16): إدارة وفحص أذونات قراءة حالة الهاتف**  
  طلب والتعامل مع إذن `READ_PHONE_STATE` باحترافية، وتوفير البدائل التوضيحية في حال رفض المستخدم للصلاحية.
- **FR-17 (مطابق لـ US-17): بنية موحدة لمعالجة وتصنيف الأخطاء (Failures)**  
  تصنيف الإخفاقات لكائنات واضحة (`PlatformFailure`, `PermissionFailure`) دون تصدير أخطاء تقنية مبهمة للواجهة.
- **FR-18 (مطابق لـ US-18): توثيق سياسة الخصوصية وأمان البيانات للمتجر**  
  إعداد إقرار أمان البيانات المعتمد لـ Google Play الذي يؤكد عدم تسجيل أو إرسال أي بيانات مستخدم خارج الهاتف.

### 3.4 وحدة واجهة المستخدم والعرض التفاعلي (UI/UX & Presentation) — [مؤيد الصوفي]
- **FR-19 (مطابق لـ US-19): بناء السمة الداكنة المتقدمة (Dark Slate Theme)**  
  ضبط ألوان التطبيق بنظام داكن موحد بألوان مريحة للعين وخافضة لاستهلاك شاشات AMOLED.
- **FR-20 (مطابق لـ US-20): بطاقة المؤشرات المرئية للبرج وحالة التغطية**  
  عرض اسم المشغل ونوع التغطية مع مؤشر دوران تفاعلي أثناء جلب البيانات أو تحديثها.
- **FR-21 (مطابق لـ US-21): زر الإجراء التفاعلي البارز لفتح LTE Only**  
  زر بارز ومريح ينفذ أمر فتح قائمة الراديو بسرعة وبشكل غير متزامن دون تجميد الشاشة.
- **FR-22 (مطابق لـ US-22): زر التحديث الفوري اللحظي وإعادة الفحص**  
  زر تحديث دائري أسفل الشاشة لإعادة قراءة حالة الشبكة والمودم فوراً وتحديث الـ State، وهو ذو أهمية قصوى للمطورين أثناء فحص التنقل بين الأنماط.
- **FR-23 (مطابق لـ US-23): نظام التنبيهات المنبثقة التوجيهية (SnackBars)**  
  إظهار رسائل تنبيه إرشادية باللغة العربية عند تعذر الفتح التلقائي لأي سبب أمني في الجهاز.
- **FR-24 (مطابق لـ US-24): التجاوب الكامل مع الشاشات وتدوير الجهاز**  
  ضمان استجابة وتكيف كافة عناصر الواجهة مع الشاشات الصغيرة والكبيرة وخلو التطبيق من أخطاء الـ Overflow.

---

## 4. المتطلبات غير الوظيفية (Non-Functional Requirements)

### 4.1 الأداء والفاعلية (Performance & Efficiency)
- **NFR-01 (زمن الاستجابة):** قراءة ومعالجة بيانات الشبكة في زمن يقل عن 150 ملي ثانية.
- **NFR-02 (سرعة الإقلاع):** زمن تشغيل التطبيق على الأجهزة المتوسطة أقل من ثانية واحدة (Cold Start < 1.0s).
- **NFR-03 (صفر استهلاك في الخلفية):** لا يحتوي التطبيق على أي Services خلفية دائمة، مما يجعل استهلاك البطارية والذاكرة في الخلفية 0%.

### 4.2 الموثوقية والمعمارية الهندسية (Architecture & Reliability)
- **NFR-04 (عزل المعمارية ومبادئ SOLID):**
  - **S (Single Responsibility):** كل UseCase وكلاس بيانات مسؤول عن إجراء ذري واحد.
  - **O (Open/Closed):** إمكانية دعم شركات تصنيع هواتف جديدة دون تعديل طبقة النطاق.
  - **L (Liskov Substitution):** استبدال المستودعات الحقيقية بمستودعات وهمية (Mocks) في بيئات الفحص بسلاسة.
  - **I (Interface Segregation):** خلو عقود المستودعات من أي دوال غير مستخدمة.
  - **D (Dependency Inversion):** اعتماد طبقات الواجهة والبيانات على التجريدات (Abstractions).
- **NFR-05 (تغطية الاختبارات):** تحقيق تغطية اختبارات وحدة (Unit Test Coverage) بنسبة 100% لكامل منطق الأعمال.

### 4.3 الأمان وسياسات متجر Google Play (Security & Store Compliance)
- **NFR-06 (المعالجة المحلية الحصرية - Data Safety):** حصر معالجة وتخزين التفضيلات داخل الذاكرة المحلية للجهاز، وعدم الاتصال بأي سيرفر خارجي.
- **NFR-07 (التوقيع وحزم الإنتاج):** تصدير التطبيق بصيغة Android App Bundle (.aab) وموقعاً بمفتاح تشفير دائم (Release Keystore) مستهدفاً Android 15 (API 35).

---

## 5. مصفوفة تتبع المتطلبات وتوزيع الملفات الهندسية (RACI & Traceability Matrix)

| رقم المتطلب | رقم القصة | المهندس المسؤول | مسار الملف البرمجي المنفذ للوظيفة |
| :---: | :---: | :---: | :--- |
| **FR-01** | US-01 | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` |
| **FR-02** | US-02 | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`<br>`android/app/src/main/AndroidManifest.xml` |
| **FR-03** | US-03 | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` |
| **FR-04** | US-04 | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`<br>`lib/data/datasources/radio_device_datasource.dart` |
| **FR-05** | US-05 | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` |
| **FR-06** | US-06 | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` |
| **FR-07** | US-07 | **محمد الدعيس** | `lib/domain/entities/network_info.dart` |
| **FR-08** | US-08 | **محمد الدعيس** | `lib/domain/entities/network_mode.dart` |
| **FR-09** | US-09 | **محمد الدعيس** | `lib/domain/repositories/network_repository.dart` |
| **FR-10** | US-10 | **محمد الدعيس** | `lib/domain/usecases/network_usecases.dart` |
| **FR-11** | US-11 | **محمد الدعيس** | `lib/domain/usecases/network_usecases.dart` |
| **FR-12** | US-12 | **محمد الدعيس** | `test/domain/usecases/network_usecases_test.dart` |
| **FR-13** | US-13 | **يوسف خيري** | `lib/data/datasources/radio_device_datasource.dart` |
| **FR-14** | US-14 | **يوسف خيري** | `lib/data/repositories/network_repository_impl.dart` |
| **FR-15** | US-15 | **يوسف خيري** | `lib/data/datasources/local_preferences_datasource.dart`<br>`pubspec.yaml` |
| **FR-16** | US-16 | **يوسف خيري** | `android/app/src/main/AndroidManifest.xml`<br>`lib/core/permissions/permission_handler.dart` |
| **FR-17** | US-17 | **يوسف خيري** | `lib/core/errors/failures.dart`<br>`lib/core/errors/exceptions.dart` |
| **FR-18** | US-18 | **يوسف خيري** | `docs/PRIVACY_POLICY.md`<br>`docs/DATA_SAFETY.md` |
| **FR-19** | US-19 | **مؤيد الصوفي** | `lib/presentation/theme/app_theme.dart`<br>`lib/main.dart` |
| **FR-20** | US-20 | **مؤيد الصوفي** | `lib/presentation/widgets/network_status_card.dart`<br>`lib/main.dart` |
| **FR-21** | US-21 | **مؤيد الصوفي** | `lib/presentation/widgets/radio_action_button.dart`<br>`lib/main.dart` |
| **FR-22** | US-22 | **مؤيد الصوفي** | `lib/presentation/screens/home_screen.dart`<br>`lib/main.dart` |
| **FR-23** | US-23 | **مؤيد الصوفي** | `lib/presentation/screens/home_screen.dart`<br>`lib/main.dart` |
| **FR-24** | US-24 | **مؤيد الصوفي** | `lib/presentation/screens/home_screen.dart`<br>`lib/main.dart` |

---

## 6. مصفوفة الاستثناءات وحالات الحافة (Edge Cases & Fault Tolerance)

| كود الاستثناء | سيناريو حالة الحافة (Edge Case) | السلوك والقرار الهندسي المتخذ في النظام |
| :---: | :--- | :--- |
| **EX-01** | تفعيل وضع الطيران (Airplane Mode On) أثناء التشغيل. | قراءة إعدادات النظام وعرض "وضع الطيران نشط" وإيقاف قراءة المودم بأمان دون انهيار. |
| **EX-02** | تشغيل الهاتف دون وجود شريحة اتصال (No SIM Card). | إظهار نص واضح "لا توجد شريحة اتصال" مع إبقاء زر فحص الراديو متاحاً للفحص الهندسي واختبارات المطورين. |
| **EX-03** | فرض الحظر الأمني الكامل (Security Lockdown) من النظام. | التقاط أخطاء `SecurityException` وعرض شريط SnackBar توجيهي للمستخدم لدخول الإعدادات يدوياً. |
| **EX-04** | تشغيل التطبيق على أجهزة لوحية (Tablets) تعمل بـ WiFi فقط. | التحقق من دعم العتاد الخلوي مسبقاً وتفادي استدعاء قنوات المودم لتجنب الـ Null Pointers. |

```