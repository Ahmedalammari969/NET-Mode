# وثيقة قصص المستخدمين وتوزيع المهام والملفات الهندسية (Agile User Stories & File Mapping)
## مشروع تطبيق: NET Mode (Cellular Network & Radio Testing Suite)
**المنهجية المتبعة:** Agile / Scrum Framework  
**عدد أعضاء الفريق:** 4 مهندسين برمجيات  
**إجمالي القصص الهندسية:** 24 قصة مستخدم موزعة بالتساوي (6 قصص لكل عضو) مع تحديد مسارات الملفات المسؤولة لكل مهمة بدقة.

---

## 1. جدول توزيع الأدوار والمسؤوليات (Team Roles Distribution)

| رقم العضو | اسم المهندس المسؤول | الدور التخصصي الهندسي (Engineering Role) | نطاق المسؤولية البرمجية (Scope of Work) |
| :---: | :--- | :--- | :--- |
| **M-1** | **أحمد العماري** | **Native Android & Platform Engineer** | تطوير Kotlin، طبقة الـ RIL، مصفوفة النيات لهواتف سامسونج وشاومي، وقنوات الاتصال الأصلية (MethodChannel). |
| **M-2** | **محمد الدعيس** | **Core Domain & Architecture Engineer** | تطبيق مبادئ Clean Architecture، بناء الكيانات (Entities)، حالات الاستخدام (Use Cases)، واختبارات الوحدة المنطقية. |
| **M-3** | **يوسف خيري** | **Data Layer & Telephony Storage Engineer** | تنفيذ مستودعات البيانات، إدارة الأذونات، التخزين المحلي للتفضيلات، وسياسات أمان متجر Google Play. |
| **M-4** | **مؤيد الصوفي** | **UI/UX & Presentation State Engineer** | تصميم واجهات Flutter الداكنة، إدارة الحالة (State Management)، التفاعل البصري، والتجاوب مع أبعاد الشاشات المختلفة. |

---

## 2. الجدول العام الشامل لقصص المستخدمين مع الملفات البرمجية المسؤولة

| رقم القصة | عنوان القصة الهندسية | المهندس المسؤول | الملفات المحددة للتعديل / الإنشاء (Files to Modify / Create) | نوع التعديل والوظيفة البرمجية |
| :---: | :--- | :---: | :--- | :--- |
| **US-01** | استدعاء قائمة الراديو المباشرة لأجهزة سامسونج | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` | بناء دالة Intent مخصصة تستهدف `com.android.phone.settings.RadioInfo`. |
| **US-02** | مسار النية البديل لأجهزة شاومي والأندرويد الخام | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`<br>`android/app/src/main/AndroidManifest.xml` | إضافة سلسلة الاستدعاء لمسارات `com.android.settings.RadioInfo` وضبط النشاطات. |
| **US-03** | قراءة وتصنيف نوع اتصال المودم الحقيقي من الـ RIL | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` | استدعاء `TelephonyManager` وتصنيف أكواد الشبكة (LTE, NR, HSPA) لقيم نصية. |
| **US-04** | تأسيس نفق اتصال آمن وخفيف عبر MethodChannel | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`<br>`lib/data/datasources/radio_device_datasource.dart` | تسجيل وضبط معالج القناة الموحدة `com.netmode.app/radio`. |
| **US-05** | فحص حالة وجود شريحة الـ SIM ووضع الطيران محلياً | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` | استعلام `Settings.Global.AIRPLANE_MODE_ON` و `SIM_STATE_READY`. |
| **US-06** | اعتراض أخطاء حظر النظام وتمرير الإشارات بدقة | **أحمد العماري** | `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` | تغليف الاستدعاءات بكتل `try/catch` للتعامل مع `SecurityException` في OneUI. |
| **US-07** | تصميم وتجريد كيان معلومات الشبكة اللحظية | **محمد الدعيس** | `lib/domain/entities/network_info.dart` | بناء كائن بيانات غير قابل للتغيير (Immutable Entity) مع معايير المساواة. |
| **US-08** | تصميم كيان أنماط الشبكة وقيم أكواد RIL المتوافقة | **محمد الدعيس** | `lib/domain/entities/network_mode.dart` | تعريف كيان الأنماط وثوابت أوضاع الشبكة القياسية (LTE Only, NR, GSM). |
| **US-09** | صياغة عقد مستودع الشبكات المجرد (Repository Interface) | **محمد الدعيس** | `lib/domain/repositories/network_repository.dart` | إنشاء Abstract Class يحدد العمليات الأساسية دون أي تبعية للمنصة. |
| **US-10** | بناء حالة استخدام جلب قياسات الشبكة الفورية | **محمد الدعيس** | `lib/domain/usecases/network_usecases.dart` | كتابة `GetInstantNetworkSnapshotUseCase` المسؤولة عن قراءة القياسات اللحظية. |
| **US-11** | بناء حالة استخدام فتح إعدادات الراديو الهندسية | **محمد الدعيس** | `lib/domain/usecases/network_usecases.dart` | كتابة `OpenRadioSettingsUseCase` لتمرير أمر الفتح عبر المستودع المجرد. |
| **US-12** | بناء وتشغيل اختبارات الوحدة الآلية لطبقة النطاق | **محمد الدعيس** | `test/domain/usecases/network_usecases_test.dart` | كتابة حالات فحص واختبارات آلية بالـ Mock للتأكد من اجتياز المنطق بنسبة 100%. |
| **US-13** | تنفيذ كلاس مصدر بيانات استدعاء القناة الأصلية | **يوسف خيري** | `lib/data/datasources/radio_device_datasource.dart` | استدعاء دوال المنصة وفك حزم الـ Map المرجعة والتعامل مع استثناءات المنصة. |
| **US-14** | تنفيذ كلاس المستودع الفعلي (NetworkRepositoryImpl) | **يوسف خيري** | `lib/data/repositories/network_repository_impl.dart` | تطبيق عقد `NetworkRepository` وتحويل الـ Data DTOs إلى Domain Entities. |
| **US-15** | بناء مصدر التخزين المحلي لتفضيلات نمط الشبكة | **يوسف خيري** | `lib/data/datasources/local_preferences_datasource.dart`<br>`pubspec.yaml` | حفظ واسترجاع النمط المفضل للمستخدم في الذاكرة التخزينية للهاتف. |
| **US-16** | فحص وإدارة أذونات قراءة الهاتف الحساسة | **يوسف خيري** | `android/app/src/main/AndroidManifest.xml`<br>`lib/core/permissions/permission_handler.dart` | تسجيل أذونات `READ_PHONE_STATE` ومعالجة حالات منح أو رفض الصلاحية برمجياً. |
| **US-17** | بناء منظومة التقاط الاستثناءات ومنع الانهيار | **يوسف خيري** | `lib/core/errors/failures.dart`<br>`lib/core/errors/exceptions.dart` | إنشاء كلاسات مخصصة للأخطاء (`PlatformFailure`, `PermissionFailure`). |
| **US-18** | صياغة توثيق أمان البيانات وسياسة الخصوصية للمتجر | **يوسف خيري** | `docs/PRIVACY_POLICY.md`<br>`docs/DATA_SAFETY.md` | توثيق عدم جمع البيانات محلياً وصياغة بنود الامتثال لسياسات Google Play. |
| **US-19** | بناء السمة الداكنة المتقدمة (Dark Theme / Cyberpunk) | **مؤيد الصوفي** | `lib/presentation/theme/app_theme.dart`<br>`lib/main.dart` | تعريف نظام الألوان الداكن المريح للعين وتوحيد خطوط وسمات التطبيق. |
| **US-20** | بطاقة المؤشرات المرئية للبرج ونوع التغطية مع التحميل | **مؤيد الصوفي** | `lib/presentation/widgets/network_status_card.dart`<br>`lib/main.dart` | بناء بطاقة واجهة أنيقة لعرض اسم المشغل ونوع التغطية ومؤشر التحميل. |
| **US-21** | زر الإجراء التفاعلي البارز لفتح إعدادات LTE Only | **مؤيد الصوفي** | `lib/presentation/widgets/radio_action_button.dart`<br>`lib/main.dart` | تصميم الزر الأساسي بلون أزرق بارز مع استجابة بصرية ونقر غير متزامن. |
| **US-22** | زر التحديث الفوري اللحظي وإعادة استعلام الشبكة | **مؤيد الصوفي** | `lib/presentation/screens/home_screen.dart`<br>`lib/main.dart` | بناء زر التحديث اللحظي وإعادة استعلام حالة التغطية وتحديث الشاشة. |
| **US-23** | نظام الرسائل والتنبيهات المنبثقة التفاعلية (SnackBars) | **مؤيد الصوفي** | `lib/presentation/screens/home_screen.dart`<br>`lib/main.dart` | إضافة شريط إشعار فوري وتوجيهي للمستخدم عند تعذر الفتح التلقائي. |
| **US-24** | التجاوب مع أحجام الشاشات المختلفة وأبعاد الأجهزة | **مؤيد الصوفي** | `lib/presentation/screens/home_screen.dart`<br>`lib/main.dart` | ضبط الهيكل ليكون متجاوباً بالكامل وخالياً من أي أخطاء تجاوز حواف الشاشة. |

---

## 3. تفاصيل قصص المستخدمين والشروط الهندسية لكل عضو

### المجموعة الأولى: مهام المهندس أحمد العماري (Native Android & Platform)

#### [US-01] استدعاء قائمة الراديو المباشرة لأجهزة سامسونج
- **الملف المسؤول:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
- **نص القصة:** كمستخدم لهاتف Samsung Galaxy، أريد فتح شاشة RadioInfo مباشرة عبر المكون الرسمي `com.android.phone.settings.RadioInfo` لتثبيت LTE Only دون الحاجة لأكواد الاتصال المحجوبة.
- **معايير القبول البرمجية:**
  1. إنشاء Intent موجه صراحة للمكون المذكور مع إضافة `Intent.FLAG_ACTIVITY_NEW_TASK`.
  2. التعامل الفوري مع استثناء `ActivityNotFoundException` والتمرير للمسار التالي بسلاسة.

#### [US-02] مسار النية البديل لأجهزة شاومي والأندرويد الخام
- **الملف المسؤول:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` و `android/app/src/main/AndroidManifest.xml`
- **نص القصة:** كمستخدم لأجهزة شاومي أو أندرويد خام، أريد من التطبيق استخدام مسارات الحزمة القياسية `com.android.settings` في حال فشل مسار سامسونج لضمان تشغيل الميزة عالمياً.
- **معايير القبول البرمجية:**
  1. فحص مسار `com.android.settings.RadioInfo`.
  2. إتاحة بديل `TestingSettings` في حال وجود طبقات حماية إضافية من نظام MIUI/HyperOS.

#### [US-03] قراءة وتصنيف نوع اتصال المودم الحقيقي من الـ RIL
- **الملف المسؤول:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
- **نص القصة:** كفني شبكات، أريد قراءة نوع الاتصال الخلوي بدقة من `TelephonyManager` لتمييز 4G LTE عن 5G NR و 3G.
- **معايير القبول البرمجية:**
  1. قراءة `getDataNetworkType` وتصنيف الأكواد إلى نصوص دقيقة.
  2. جلب اسم مشغل الخدمة من `networkOperatorName` أو `simOperatorName`.

#### [US-04] تأسيس نفق اتصال آمن وخفيف عبر MethodChannel
- **الملف المسؤول:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt` و `lib/data/datasources/radio_device_datasource.dart`
- **نص القصة:** كمهندس معماري للمنصة، أريد قناة اتصال برمجية موحدة وخفيفة تسمى `com.netmode.app/radio` لنقل الأوامر والبيانات بأمان.
- **معايير القبول البرمجية:**
  1. ضمان عدم تجميد الـ Main UI Thread أثناء تنفيذ الاستدعاءات.
  2. إغلاق القناة وتنظيف الموارد لتجنب تسريب الذاكرة (Memory Leak).

#### [US-05] فحص حالة وجود شريحة الـ SIM ووضع الطيران محلياً
- **الملف المسؤول:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
- **نص القصة:** كمستخدم، أريد أن يكتشف التطبيق حالة إدخال الشريحة أو تفعيل وضع الطيران لتفادي عرض بيانات مضللة.
- **معايير القبول البرمجية:**
  1. قراءة حالة `SIM_STATE_READY`.
  2. قراءة إعدادات النظام العامة لوضع الطيران وإرجاعها في قاموس البيانات المشترك.

#### [US-06] اعتراض أخطاء حظر النظام وتمرير الإشارات بدقة
- **الملف المسؤول:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
- **نص القصة:** كمطور واجهات، أريد استلام قيمة واضحة في حال حظر النظام للوصول الهرمي لشاشات الراديو لتوجيه المستخدم بالشكل السليم.
- **معايير القبول البرمجية:**
  1. التقاط استثناءات `SecurityException` بكتل آمنة.
  2. إرجاع القيمة المنطقية `false` في حال استنفاد كل البدائل الممكنة دون انهيار التطبيق.

---

### المجموعة الثانية: مهام المهندس محمد الدعيس (Core Domain & Architecture)

#### [US-07] تصميم وتجريد كيان معلومات الشبكة اللحظية
- **الملف المسؤول:** `lib/domain/entities/network_info.dart`
- **نص القصة:** كمهندس معماري للنطاق، أريد كياناً نقياً بلغة Dart يمثل قياسات الشبكة (Carrier Name, Network Type, Sim State) بدون أي ارتباط بـ Flutter SDK.
- **معايير القبول البرمجية:**
  1. تعريف حقول الكيان كـ `final` مع خاصية التجريد التام.
  2. تطبيق الـ Value Equality عبر تجاوز `operator ==` و `hashCode`.

#### [US-08] تصميم كيان أنماط الشبكة وقيم أكواد RIL المتوافقة
- **الملف المسؤول:** `lib/domain/entities/network_mode.dart`
- **نص القصة:** كمطور منطق، أريد كائن `NetworkMode` يحتوي على مسميات الأنماط الشائعة وأكواد RIL المناظرة لها لتوحيد تعريف الأنماط في النظام.
- **معايير القبول البرمجية:**
  1. توفير ثوابت واضحة للأنماط: (LTE Only, GSM Only, WCDMA Preferred, NR Only).
  2. ربط كل نمط بالمعرف الرقمي الخاص به في طبقة الاتصال.

#### [US-09] صياغة عقد مستودع الشبكات المجرد (Repository Interface)
- **الملف المسؤول:** `lib/domain/repositories/network_repository.dart`
- **نص القصة:** كمهندس معمارية، أريد واجهة مجردة (Abstract Contract) تحدد وظائف النظام لتحقيق مبدأ عكس التبعية (Dependency Inversion).
- **معايير القبول البرمجية:**
  1. تعريف دالة `getInstantNetworkSnapshot()` ترجع `Future<NetworkInfo>`.
  2. تعريف دالة `openRadioTestingSettings()` ترجع `Future<bool>`.

#### [US-10] بناء حالة استخدام جلب قياسات الشبكة الفورية
- **الملف المسؤول:** `lib/domain/usecases/network_usecases.dart`
- **نص القصة:** كمطور أعمال، أريد حالة استخدام `GetInstantNetworkSnapshotUseCase` تطبق مبدأ المسؤولية الواحدة لجلب بيانات الشبكة اللحظية.
- **معايير القبول البرمجية:**
  1. كتابة دالة `call()` بنمط دالي نقي.
  2. عزل المنطق عن طريقة جلب البيانات وتوجيهه فقط نحو المستودع.

#### [US-11] بناء حالة استخدام فتح إعدادات الراديو الهندسية
- **الملف المسؤول:** `lib/domain/usecases/network_usecases.dart`
- **نص القصة:** كمطور منطق، أريد حالة استخدام `OpenRadioSettingsUseCase` مخصصة لإطلاق أمر الفتح بمسؤولية مستقلة.
- **معايير القبول البرمجية:**
  1. فصل أمر فتح الإعدادات تماماً عن حالة فحص القياسات.
  2. إرجاع حالة النجاح أو الفشل للواجهة بصورة مبسطة.

#### [US-12] بناء وتشغيل اختبارات الوحدة الآلية لطبقة النطاق
- **الملف المسؤول:** `test/domain/usecases/network_usecases_test.dart`
- **نص القصة:** كمهندس جودة (QA)، أريد كتابة وتمرير اختبارات آلية لحالات الاستخدام عبر Mock Repository للتحقق من سلامة المنطق البرمجي.
- **معايير القبول البرمجية:**
  1. محاكاة الـ Repository والتحقق من صحة كائن `NetworkInfo` المرجع.
  2. التحقق من نجاح الاختبارات بأمر `flutter test` بنسبة 100%.

---

### المجموعة الثالثة: مهام المهندس يوسف خيري (Data Layer & Telephony Storage)

#### [US-13] تنفيذ كلاس مصدر بيانات استدعاء القناة الأصلية
- **الملف المسؤول:** `lib/data/datasources/radio_device_datasource.dart`
- **نص القصة:** كمهندس بيانات، أريد كلاس يتعامل مباشرة مع `MethodChannel` ويحول الاستجابات الخام إلى قواميس بيانات آمنة.
- **معايير القبول البرمجية:**
  1. التقاط استثناء `PlatformException` وإرجاع قيم افتراضية لمنع توقف التطبيق.
  2. التحقق من صحة المفاتيح المستلمة من لغة Kotlin.

#### [US-14] تنفيذ كلاس المستودع الفعلي (NetworkRepositoryImpl)
- **الملف المسؤول:** `lib/data/repositories/network_repository_impl.dart`
- **نص القصة:** كمطور طبقة البيانات، أريد تنفيذ عقد `NetworkRepository` وتحويل استجابات القناة إلى كيانات `NetworkInfo`.
- **معايير القبول البرمجية:**
  1. تطبيق جميع دوال الواجهة المجردة بالكامل.
  2. تحويل البيانات (Mapping) بدون حدوث استثناءات عدم التوافق النوعي.

#### [US-15] بناء مصدر التخزين المحلي لتفضيلات نمط الشبكة
- **الملف المسؤول:** `lib/data/datasources/local_preferences_datasource.dart` و `pubspec.yaml`
- **نص القصة:** كمستخدم، أريد حفظ خياري المفضل لنمط الشبكة في ذاكرة الجهاز لاسترجاعه لاحقاً.
- **معايير القبول البرمجية:**
  1. توفير دوال حفظ واسترجاع النمط المفضل محلياً.
  2. استرجاع القيمة الافتراضية في حال كانت هذه هي المرة الأولى للتشغيل.

#### [US-16] فحص وإدارة أذونات قراءة الهاتف الحساسة
- **الملف المسؤول:** `android/app/src/main/AndroidManifest.xml` و `lib/core/permissions/permission_handler.dart`
- **نص القصة:** كمستخدم، أريد من التطبيق طلب إذن `READ_PHONE_STATE` باحترافية وتوضيح السبب التقني للحفاظ على الخصوصية.
- **معايير القبول البرمجية:**
  1. إعلان الأذونات بشكل رسمي في ملف المانيفست.
  2. التأكد من معالجة حالة الرفض وعدم انهيار التطبيق.

#### [US-17] بناء منظومة التقاط الاستثناءات ومنع الانهيار
- **الملف المسؤول:** `lib/core/errors/failures.dart` و `lib/core/errors/exceptions.dart`
- **نص القصة:** كمهندس استقرار البرمجيات، أريد بنية موحدة لإدارة وتصنيف استثناءات النظام لمنع حدوث أي Crash للمستخدم.
- **معايير القبول البرمجية:**
  1. تعريف كلاسات الإخفاق القياسية (`PlatformFailure`, `DeviceIncompatibilityFailure`).
  2. تمرير رسائل توضيحية لطبقة العرض بدلاً من رمي الاستثناء في وجه المستخدم.

#### [US-18] صياغة توثيق أمان البيانات وسياسة الخصوصية للمتجر
- **الملف المسؤول:** `docs/PRIVACY_POLICY.md` و `docs/DATA_SAFETY.md`
- **نص القصة:** كمسؤول نشر التطبيق، أريد توثيق سياسة الخصوصية وأمان البيانات لتلبية اشتراطات متجر Google Play بدقة.
- **معايير القبول البرمجية:**
  1. إيضاح أن قراءة حالة الشبكة تتم على الجهاز حصراً دون أي نقل أو تخزين خارجي.
  2. استيفاء متطلبات إقرار أمان البيانات (Data Safety Declarations).

---

### المجموعة الرابعة: مهام المهندس مؤيد الصوفي (UI/UX & Presentation State)

#### [US-19] بناء السمة الداكنة المتقدمة (Dark Theme / Cyberpunk)
- **الملف المسؤول:** `lib/presentation/theme/app_theme.dart` و `lib/main.dart`
- **نص القصة:** كمستخدم، أريد واجهة داكنة مريحة للعين بألوان عصرية متناسقة (`#0F172A` و `#38BDF8`).
- **معايير القبول البرمجية:**
  1. تطبيق ثيم داكن رسمي في إعدادات `MaterialApp`.
  2. توحيد درجات الألوان لجميع العناصر والبطاقات.

#### [US-20] بطاقة المؤشرات المرئية للبرج ونوع التغطية مع التحميل
- **الملف المسؤول:** `lib/presentation/widgets/network_status_card.dart` و `lib/main.dart`
- **نص القصة:** كمستخدم، أريد بطاقة مرئية أنيقة تعرض اسم شركة الاتصالات ونوع الشبكة الحالية مع مؤشر التحميل.
- **معايير القبول البرمجية:**
  1. إظهار مؤشر دوران (`CircularProgressIndicator`) أثناء جلب البيانات.
  2. عرض اسم المشغل ونوع التقنية بشكل عريض ومركزي عند اكتمال الجلب.

#### [US-21] زر الإجراء التفاعلي البارز لفتح إعدادات LTE Only
- **الملف المسؤول:** `lib/presentation/widgets/radio_action_button.dart` و `lib/main.dart`
- **نص القصة:** كمستخدم، أريد زراً تفاعلياً بارزاً ومريحاً بعنوان "فتح إعدادات الراديو (LTE Only)" للوصول السريع بنقرة واحدة.
- **معايير القبول البرمجية:**
  1. زر بتصميم مميز (`ElevatedButton`) بأيقونة مناسبة.
  2. استجابة نقر غير متزامنة دون تعليق الواجهة.

#### [US-22] زر التحديث الفوري اللحظي وإعادة استعلام الشبكة
- **الملف المسؤول:** `lib/presentation/screens/home_screen.dart` و `lib/main.dart`
- **نص القصة:** كمستخدم، أريد زر تحديث سريع لتجديد قراءة الشبكة فوراً عند الانتقال لمكان آخر.
- **معايير القبول البرمجية:**
  1. زر تحديث دائري بأسفل الواجهة مع تلميح نصي (Tooltip).
  2. إعادة استعلام مصدر البيانات وتحديث الواجهة مباشرة عبر `setState`.

#### [US-23] نظام الرسائل والتنبيهات المنبثقة التفاعلية (SnackBars)
- **الملف المسؤول:** `lib/presentation/screens/home_screen.dart` و `lib/main.dart`
- **نص القصة:** كمستخدم، أريد ظهور شريط تنبيه منبثق (SnackBar) في حال تعذر فتح شاشة الراديو لمعرفة المشكلة.
- **معايير القبول البرمجية:**
  1. إظهار `SnackBar` تلقائياً إذا أعادت دالة الفتح قيمة `false`.
  2. صياغة رسالة توجيهية واضحة باللغة العربية.

#### [US-24] التجاوب مع أحجام الشاشات المختلفة وأبعاد الأجهزة
- **الملف المسؤول:** `lib/presentation/screens/home_screen.dart` و `lib/main.dart`
- **نص القصة:** كمستخدم، أريد أن تتكيف عناصر الشاشة بمرونة مع أبعاد الهواتف المختلفة ودون حدوث تجاوز للحواف.
- **معايير القبول البرمجية:**
  1. استخدام عناصر التوسيط والحشو المرن (`Center`, `Padding`).
  2. خلو الشاشة تماماً من أخطاء الـ `RenderFlex overflow`.