# 🏆 الموسوعة الهندسية الشاملة والتقرير الفني النهائي لمشروع NET Mode
### Advanced Cellular Network & Radio Testing Suite
**إدارة وتثبيت أنماط شبكات الهاتف الخلوي وفق أرقى المعايير العالمية لهندسة البرمجيات**

---

### 🎓 بطاقة تعريف المشروع الأكاديمي:
* **اسم المشروع:** NET Mode — أداة فحص وإدارة أنماط شبكات الاتصالات الخلوية
* **المنهجية الهندسية:** Agile Scrum / Kanban Driven Development
* **دستور الحوكمة الذكية:** Agent Directives (`GEMINI.md`)
* **بروتوكول الربط الذاتي:** Model Context Protocol (MCP) عبر سيرفرات `dart-mcp-server` و `github-mcp-server`
* **أداة إدارة وتتبع المهام:** لوحة Trello الرسمية (`NET Mode - Agile Board`)
* **المعمارية المعتمدة:** Clean Architecture & SOLID Principles
* **فريق العمل الهندسي:**
  1. **أحمد ياسين العماري** — مهندس المنصة ونظام أندرويد (Project Lead & Hardware Platform Engineer)
  2. **محمد علي / محمد الدعيس** — مهندس النطاق والمعمارية (Core Domain & Software Architect)
  3. **يوسف خيري** — مهندس طبقة البيانات وقنوات الاتصال (Data Layer & Telephony Storage Engineer)
  4. **مؤيد الصوفي** — مهندس الواجهات وتجربة المستخدم (UI/UX & Presentation State Engineer)
* **تحت إشراف الأستاذ الدكتور:** `د.م. ساهر الهمداني`

---

## 📑 الفهرس العام للموسوعة الهندسية:
* **الباب الأول:** خطة وسير العمل الهندسي الشامل من البداية حتى التسليم (Engineering Workflow Pipeline).
* **الباب الثاني:** ميثاق حوكمة الذكاء الاصطناعي والدستور المعماري (`GEMINI.md` & MCP).
* **الباب الثالث:** مواصفات متطلبات البرمجيات الرسمية (SRS - IEEE Std 830-1998) والحدود والنطاق (Scope & Boundaries).
* **الباب الرابع:** مصفوفة قصص المستخدمين الـ 24 كاملة (Agile User Stories & Acceptance Criteria).
* **الباب الخامس:** لوحة كانبان وتوزيع المهام الـ 24 تفصيلياً على المهندسين الأربعة مع ملفات كل مهمة والـ DoD.
* **الباب السادس:** المعمارية البرمجية وسريان البيانات (Clean Architecture & SOLID).
* **الباب السابع:** محرك النظام الأصلي وحلول سامسونج ويمن موبايل (`MainActivity.kt`).
* **الباب الثامن:** الهندسة الدفاعية ورصد وضع الطيران وحالة الشريحة.
* **الباب التاسع:** واجهة المستخدم والأوضاع الخلوية الخمسة المخصصة لليمن.
* **الباب العاشر:** إدارة التكوين، حماية فروع GitHub وسير العمل (Git Workflow).
* **الباب الحادي عشر:** دليل وسيناريو المناقشة الشفهية غداً أمام الدكتور ساهر الهمداني.

---

## 🚀 الباب الأول: خطة وسير العمل الهندسي الشامل من البداية حتى التسليم (Engineering Workflow Pipeline)

لتطبيق أرقى المعايير الهندسية المتبعة في كبرى شركات التقنية العالمية (مثل Google و Microsoft)، تم تنظيم دورة حياة تطوير المشروع (SDLC) في **مسار عمل تتابعي متكامل (End-to-End Engineering Pipeline)** يربط كل خطوة بسابقتها ولا يسمح بالانتقال العشوائي:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   مخطط سريان العمل الهندسي (Master Pipeline)            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
 1. التأسيس والحوكمة الذكية        ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ • تفعيل مهارات .agents/skills/  • كتابة دستور الموجهات GEMINI.md     │
 └──────────────────────────────────┬───────────────────────────────────┘
                                    │
 2. هندسة المتطلبات والتحليل       ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ • وثيقة SRS (IEEE 830-1998)     • قصص المستخدمين US-01 -> US-24      │
 └──────────────────────────────────┬───────────────────────────────────┘
                                    │
 3. التخطيط الرشيق وإدارة المهام   ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ • لوحة Trello (Agile Board)     • تقسيم المهام وتحديد شروط الـ DoD   │
 └──────────────────────────────────┬───────────────────────────────────┘
                                    │
 4. إدارة التكوين والفروع (Git)    ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ • إنشاء فروع المهام feature/... • تفعيل قواعد حماية الفرع main       │
 └──────────────────────────────────┬───────────────────────────────────┘
                                    │
 5. التنفيذ المعماري النظيف        ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ • Domain Layer (Pure Dart)      • Data Layer (MethodChannel)         │
 │ • Platform Native (Kotlin)      • Presentation UI (Dark Cyberpunk)   │
 └──────────────────────────────────┬───────────────────────────────────┘
                                    │
 6. التحقق والاختبارات وضمان الجودة ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ • Unit Tests (100% Pass)        • Widget Tests & محاكاة الطيران      │
 │ • فحص التحليل الساكن flutter analyze (No issues found)               │
 └──────────────────────────────────┬───────────────────────────────────┘
                                    │
 7. المراجعة والدمج والنشر النهائي ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ • فتح ومراجعة Pull Requests     • دمج الميزات في الفرع الرئيسي main  │
 │ • توثيق README العالمي          • تصدير التقرير الفني النهائي        │
 └──────────────────────────────────────────────────────────────────────┘
```

### المبادئ الهندسية الصارمة الحاكمة لسير العمل:
1. **لا كود بدون متطلب (No Code without Requirement):** كل سطر برمجي مكتوب في المشروع يعود في أصله إلى متطلب وظيفي (FR) مسجل في وثيقة الـ SRS وقصة مستخدم (US).
2. **عزل النطاق البرمجي (Domain Purity):** منطق أعمال الشبكات مفصول تماماً عن أي واجهات أو أطر عمل لضمان قابلية صيانته لعشرات السنين.
3. **معيار الإنجاز الصارم (Definition of Done - DoD):** لا تنتقل أي مهمة في Trello إلى خانة المكتمل إلا بعد اجتياز الفحص الآلي واليدوي وتغليف الاستثناءات.
4. **حوكمة الفروع وحماية الكود (Branch Governance):** منع الرفع المباشر إلى فرع `main` وإلزام الفريق بنظام مراجعة الكود (Code Review) عبر الـ Pull Requests.

---

## 🏛️ الباب الثاني: ميثاق حوكمة الذكاء الاصطناعي والدستور المعماري (`GEMINI.md` & MCP)

### 1. ميثاق ودستور المشروع (`GEMINI.md`):
تم تأسيس ميثاق إلزامي صارم لوكيل الذكاء الاصطناعي والفريق في ملف `GEMINI.md` لفرض المعايير التالية:
* **عزل طبقة النطاق (Domain Layer Purity):** حظر استيراد أي مكتبة تتبع Flutter UI أو حزم أندرويد نهائياً داخل `lib/domain/` لضمان بقاء منطق الأعمال كـ Pure Dart.
* **عزل قنوات البيانات (Data Layer Isolation):** حصر استدعاءات `MethodChannel` في `lib/data/` وتجريدها بنمط المستودع (Repository Pattern).
* **الهندسة الدفاعية (Defensive Design):** معالجة حالات رفض الصلاحيات، ووضع الطيران، واختلاف مودمات الشركات المصنعة استباقياً لمنع الانهيار.
* **حوكمة المهارات (`.agents/skills/`):** إلزام الوكيل بالرجوع لقواعد المهارات المعتمدة قبل اتخاذ أي قرار تنفيذي.

### 2. بروتوكول الربط الذاتي (Model Context Protocol - MCP):
تم ربط بيئة التطوير بسيرفرين رئيسيين:
1. **`dart-mcp-server`:** أتاح للذكاء الاصطناعي فحص الكود بالتحليل الساكن التلقائي (Static Analysis)، فحص شجرة الواجهات (Widget Tree Inspector)، وتشغيل محرك الاختبارات الآلي حتى تحقيق نتيجة `No issues found!`.
2. **`github-mcp-server`:** أتاح حوكمة الفروع، تتبع الـ Commits، وأتمتة مراجعة الكود قبل الدمج.

---

## 📋 الباب الثالث: مواصفات متطلبات البرمجيات الرسمية (SRS - IEEE Std 830-1998) والحدود والنطاق

تمت صياغة وثيقة الـ SRS استناداً إلى المعيار الدولي **IEEE Std 830-1998**؛ وفيما يلي التفصيل الدقيق لحدود النظام والمتطلبات:

### 3.1 حدود ونطاق العمل الهندسي (Scope & System Boundaries):
تحديد "حواف ونطاق النظام" بدقة يمنع التشتت البرمجي ويحدد بدقة ما يقدمه النظام وما يقع خارجه:

```
┌────────────────────────────────────────────────────────────────────────┐
│                       حدود ونطاق النظام (System Boundaries)             │
├───────────────────────────────────┬────────────────────────────────────┤
│    داخل نطاق العمل (In-Scope)      │    خارج نطاق العمل (Out-of-Scope)   │
├───────────────────────────────────┼────────────────────────────────────┤
│ • قراءة تليمتري المودم الحقيقي    │ • كسر حماية النظام الإجباري (Root) │
│   (LTE, EVDO, HSPA, 5G NR).       │   للأجهزة المقفلة عتادياً من المصنع│
│ • تجاوز حظر كود *#*#4636#*#*      │ • دعم بيئة أنظمة iOS نظراً لإغلاق  │
│   واستدعاء شاشات الراديو السرية.  │   شركة Apple لمودم الراديو تماماً. │
│ • التثبيت على الأنماط الخمسة      │ • الاتصال بخوادم وسيطة خارجية      │
│   المخصصة لشركات الاتصالات باليمن.│   (التطبيق يعمل Offline محلياً 100%)│
│ • رصد وضع الطيران بدقة ومنع       │ • تعديل أرقام الـ IMEI أو إجراء    │
│   الإبلاغ الكاذب عن الاتصال.      │   تعديلات غير قانونية على المودم.  │
│ • كشف جاهزية وحالة بطاقة SIM.     │                                    │
│ • تخزين التفضيلات محلياً Offline. │                                    │
└───────────────────────────────────┴────────────────────────────────────┘
```

### 3.2 القيود التصميمية والافتراضات (Design Constraints & Assumptions):
* **القيود العتادية والتوافقية (Hardware & OEM Constraints):**
  - يعمل التطبيق على هواتف أندرويد بدءاً من إصدار Android 5.0 (API 21) وحتى Android 14 (API 34).
  - صُممت مصفوفة استدعاء النيات لتتوافق مع واجهات: Samsung One UI، Xiaomi MIUI/HyperOS، وهواتف أندرويد الخام (Pixel / Motorola).
* **الافتراضات والاعتماديات (Assumptions & Dependencies):**
  - يُفترض وجود بطاقة SIM مفعلة تدعم الاتصال بالشبكات الخلوية اليمنية للاستفادة الكاملة من قراءة المشغل.
  - يُفترض أن المستخدم يمنح التطبيق إذن `READ_PHONE_STATE` لقراءة التردد ونوع الشبكة.

### 3.3 المتطلبات الوظيفية الرئيسية (Functional Requirements - FRs):
* `FR-01`: فحص واكتشاف مشغل الخدمة الحقيقي ونوع الشبكة اللحظية بدقة.
* `FR-02`: توفير اختصارات مباشرة وآمنة لفتح شاشات هندسة الراديو (Hidden RadioInfo Activities) تتخطى حظر لوحة الاتصال.
* `FR-03`: إتاحة تثبيت ترددات الفورجي (LTE Only) والأوضاع الهجينة لشركات الاتصالات باليمن.
* `FR-04`: الكشف الدقيق عن حالة بطاقة SIM والتفرقة بين الشريحة المتصلة والشريحة المفقودة.
* `FR-05`: الكشف الفوري عن وضع الطيران وإطفاء مؤشرات البث لمنع التقارير الكاذبة.
* `FR-06`: اعتراض استثناءات النظام الأمنية (Knox Security Policies) ومعالجتها بأمان.
* `FR-07`: تخزين الأنماط المفضلة وسجل التبديل محلياً دون أي خوادم خارجية (Offline-First).
* `FR-08`: توفير واجهة مستخدم تفاعلية بنمط داكن (Cyberpunk Navy) مع عداد إشارة مكون من 5 أعمدة مضيئة.

### 3.4 المتطلبات غير الوظيفية (Non-Functional Requirements - NFRs):
* **الأداء والسرعة (Performance):** استخراج بيانات الشبكة اللحظية وتحديث الواجهة في زمن استجابة لا يتجاوز **200 ملي ثانية**.
* **كفاءة الطاقة (Power Efficiency):** استهلاك طاقة البطارية أقل من **1% في الساعة** من خلال تجنب الاستعلام الدائم واعتماد التحديث الحدثي عند تنشيط الواجهة.
* **الموثوقية والصلابة (Reliability & Zero-Crash):** معالجة كتل الـ Intents واستدعاءات الراديو عبر `try-catch` شاملة، بحيث لا ينهار التطبيق (Zero Crashing) حتى في حال عدم توافق واجهة هاتف معين.
* **الأمان والخصوصية (Security & Privacy):** التطبيق يعمل بنمط **Offline-First** محلي بنسبة 100%، ولا يقوم بجمع أو إرسال أي بيانات تخص المستخدم أو موقع الهاتف لأي خادم خارجي.

---

## 📝 الباب الرابع: مصفوفة قصص المستخدمين الـ 24 (Agile User Stories)

| رقم القصة | العنوان والوصف | معيار القبول الهندسي (Acceptance Criteria) |
| :-: | :--- | :--- |
| **US-01** | تشغيل نية راديو سامسونج | **Given** هاتف One UI، **When** طلب فتح الراديو، **Then** تشغيل `RadioInfo` بنجاح. |
| **US-02** | سلسلة بدائل شاومي والأندرويد الخام | **Given** تعذر مسار سامسونج، **When** استدعاء البديل، **Then** فتح `TestingSettings`. |
| **US-03** | فك تشفير مسميات المودم | **Given** كود RIL رقمي، **When** قراءته، **Then** ترجمته لمسمى صريح مثل (4G LTE / 5G NR). |
| **US-04** | جسر قنوات المنصة | **Given** بيانات المودم، **When** نقلها، **Then** عبورها عبر `MethodChannel` بدون تسريب ذاكرة. |
| **US-05** | فحص الشريحة والطيران | **Given** تفعيل الطيران، **When** فحص الحالة، **Then** إرجاع `isAirplaneMode = true`. |
| **US-06** | اعتراض أخطاء التحصين الأمني | **Given** رفض إذن `MODIFY_PHONE_STATE`، **When** محاولة التغيير، **Then** اصطياد الاستثناء بهدوء. |
| **US-07** | كيان NetworkInfo النقي | **Given** تيليمتري الشبكة، **When** إنشاؤه، **Then** تكوين كائن Dart غير قابل للتعديل (Immutable). |
| **US-08** | كيان NetworkMode وأنماط اليمن | **Given** نمط شبكة، **When** تعريفه، **Then** ربطه بكود RIL المعياري ووصف المودم. |
| **US-09** | عقد مستودع الشبكة المجرد | **Given** معمارية نظيفة، **When** صياغة العقد، **Then** تجريده كـ Interface بدون أي مكتبات UI. |
| **US-10** | حالة استخدام لقطة الشبكة اللحظية | **Given** طلب تحديث، **When** استدعاء UseCase، **Then** إرجاع `NetworkInfo` نقي. |
| **US-11** | حالة استخدام فتح شاشات الراديو | **Given** ضغط زر الضبط، **When** التنفيذ، **Then** إطلاق النية المناسبة بأمان. |
| **US-12** | حزمة اختبارات النطاق الآلية | **Given** بيئة الاختبارات، **When** تشغيل `flutter test`، **Then** اجتياز 100% بنجاح. |
| **US-13** | تنفيذ مصدر بيانات الراديو | **Given** منصة أندرويد، **When** استدعاء القناة، **Then** معالجة `PlatformException` بأمان. |
| **US-14** | تنفيذ مستودع البيانات الحقيقي | **Given** بيانات خام HashMap، **When** استقبالها، **Then** تحويلها لكائنات Domain. |
| **US-15** | التخزين الدائم للنمط المفضل | **Given** اختيار المستخدم لنمط، **When** الحفظ، **Then** استرجاعه تلقائياً عند إعادة الفتح. |
| **US-16** | إدارة أذونات حالة الهاتف | **Given** طلب إذن `READ_PHONE_STATE`، **When** المنح أو الرفض، **Then** التعامل بدون انهيار. |
| **US-17** | معمارية توحيد الأخطاء والفشل | **Given** حدوث خطأ، **When** معالجته، **Then** ترجمته لـ `PlatformFailure` دون كراش. |
| **US-18** | إقرار أمان البيانات وسياسة الخصوصية | **Given** متطلبات المتجر، **When** التوثيق، **Then** إثبات أن كافة المعالجات تتم محلياً فقط. |
| **US-19** | نظام الثيم الداكن المتقدم | **Given** شاشات AMOLED، **When** فتح التطبيق، **Then** عرض ألوان Cyberpunk مريحة للعين. |
| **US-20** | بطاقة حالة التغطية وأعمدة الإشارة | **Given** إشارة الشبكة، **When** البث، **Then** إضاءة 5 أعمدة نيون تنطفئ في وضع الطيران. |
| **US-21** | الزر البارز لضبط المودم | **Given** شاشة التطبيق، **When** الضغط، **Then** تفاعل نقر غير متزامن مع إطار نيون. |
| **US-22** | التحديث اللحظي عبر دورة الحياة | **Given** عودة المستخدم، **When** تنشيط التطبيق، **Then** تحديث الواجهة فوراً عبر `WidgetsBindingObserver`. |
| **US-23** | محرك الإشعارات التفاعلية | **Given** تعذر التحويل الصامت، **When** الفشل، **Then** إظهار SnackBar يرشد المستخدم للبديل. |
| **US-24** | تجاوب الواجهة مع مختلف الشاشات | **Given** أجهزة مختلفة، **When** تدوير الشاشة، **Then** خلو الواجهة تماماً من أخطاء الـ Overflow. |

---

## 📊 الباب الخامس: لوحة كانبان وتوزيع المهام الـ 24 تفصيلياً على المهندسين الأربعة

تم تقسيم الـ 24 مهمة بالتساوي التام على أعضاء الفريق الأربعة (6 مهام لكل مهندس)، مع تحديد الملفات البرمجية الدقيقة واسم فرع Git لكل مهمة:

---

### 👨‍💻 المهندس الأول: أحمد ياسين العماري (`@ahmed-alammari`)
* **المسؤولية القيادية:** مهندس المنصة وهندسة المودم (Native Android & Hardware Platform Engineer).
* **المسار الهندسي (Epic 1):** `Native Platform & Radio RIL`.
* **الوسم في Trello:** `native-android`، `hardware-ril`.

#### المهام الست المسندة للمهندس أحمد العماري:
1. **Issue #1 (US-01): Samsung Radio Intent Launcher**
   - **الوصف الهندسي:** بناء دالة Intent صريحة لاستهداف شاشة `com.android.phone.settings.RadioInfo` لأجهزة سامسونج One UI.
   - **الملفات البرمجية:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
   - **فرع Git:** `feature/issue-1-samsung-radio-intent`
2. **Issue #2 (US-02): Xiaomi & AOSP Fallback Intent Chain**
   - **الوصف الهندسي:** بناء سلسلة البدائل التعاقبية لاستدعاء شاشة `RadioInfo` في شاومي وبديل `TestingSettings` لأندرويد الخام.
   - **الملفات البرمجية:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
   - **فرع Git:** `feature/issue-2-xiaomi-aosp-fallback`
3. **Issue #3 (US-03): Telephony RIL Modem Network Decoder**
   - **الوصف الهندسي:** فك تشفير وقراءة أكواد الـ RIL الخلوية الحقيقية من المودم عبر `TelephonyManager` وتصنيفها إلى (4G LTE, 5G NR, 3G EVDO).
   - **الملفات البرمجية:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
   - **فرع Git:** `feature/issue-3-ril-telephony-decoder`
4. **Issue #4 (US-04): Native MethodChannel Bridge Architecture**
   - **الوصف الهندسي:** تأسيس القناة البرمجية الموحدة `com.netmode.app/radio` وتبادل الرسائل والبيانات مع Flutter دون أي تسريب ذاكرة.
   - **الملفات البرمجية:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
   - **فرع Git:** `feature/issue-4-platform-method-channel`
5. **Issue #5 (US-05): SIM State & Airplane Mode Native Inspector**
   - **الوصف الهندسي:** الفحص اللحظي لمسجلات النظام لحالة وضع الطيران `AIRPLANE_MODE_ON` وحل مشكلة قراءة اسم يمن موبايل لشبكات CDMA عبر `SubscriptionManager`.
   - **الملفات البرمجية:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
   - **فرع Git:** `feature/issue-5-sim-airplane-inspector`
6. **Issue #6 (US-06): System Security Lockout & Exception Catching**
   - **الوصف الهندسي:** اعتراض استثناءات الأمان الصادرة عن Knox و `MODIFY_PHONE_STATE` وإرجاع استجابات آمنة للواجهة عبر الـ Fallback.
   - **الملفات البرمجية:** `android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt`
   - **فرع Git:** `feature/issue-6-security-exception-handler`

---

### 👨‍💻 المهندس الثاني: محمد علي / محمد الدعيس (`@mohammed-alduais`)
* **المسؤولية المعمارية:** مهندس النطاق والمعمارية البرمجية (Core Domain & Software Architect).
* **المسار الهندسي (Epic 2):** `Clean Architecture & Domain Logic`.
* **الوسم في Trello:** `clean-domain`، `core-logic`.

#### المهام الست المسندة للمهندس محمد الدعيس:
7. **Issue #7 (US-07): Pure NetworkInfo Entity Definition**
   - **الوصف الهندسي:** بناء كائن بيانات Dart نقي غير قابل للتعديل (Immutable) يحمل تيليمتري الشبكة (carrier, networkType, hasSimCard, isAirplaneMode).
   - **الملفات البرمجية:** `lib/domain/entities/network_info.dart`
   - **فرع Git:** `feature/issue-7-network-info-entity`
8. **Issue #8 (US-08): NetworkMode Presets & RIL Types Entity**
   - **الوصف الهندسي:** تعريف كيان الأنماط الخلوية المخصصة وتصنيفاتها (2G, 3G, 4G, 5G, Auto) وربطها برمز الـ RIL والوصف الفني.
   - **الملفات البرمجية:** `lib/domain/entities/network_mode.dart`
   - **فرع Git:** `feature/issue-8-network-mode-entity`
9. **Issue #9 (US-09): Abstract NetworkRepository Interface**
   - **الوصف الهندسي:** صياغة عقد المستودع المجرد لعزل طبقة النطاق وتطبيق مبدأ عكس التبعية (Dependency Inversion Principle).
   - **الملفات البرمجية:** `lib/domain/repositories/network_repository.dart`
   - **فرع Git:** `feature/issue-9-network-repository-contract`
10. **Issue #10 (US-10): Get Instant Network Snapshot UseCase**
    - **الوصف الهندسي:** بناء حالة استخدام مستقلة لجلب بيانات الشبكة اللحظية بنمط دالي نقي وفق مبدأ المسؤولية الواحدة (SRP).
    - **الملفات البرمجية:** `lib/domain/usecases/network_usecases.dart`
    - **فرع Git:** `feature/issue-10-get-snapshot-usecase`
11. **Issue #11 (US-11): Open Radio Settings Controller UseCase**
    - **الوصف الهندسي:** بناء حالة استخدام مستقلة لعزل طلب فتح شاشات الراديو الأصلية عن الواجهة.
    - **الملفات البرمجية:** `lib/domain/usecases/network_usecases.dart`
    - **فرع Git:** `feature/issue-11-open-radio-usecase`
12. **Issue #12 (US-12): Domain Unit Testing Suite (100% Pass)**
    - **الوصف الهندسي:** كتابة واجتياز اختبارات الوحدة الآلية الشاملة لطبقة النطاق باستخدام الـ Mock Repositories والتحقق من المساواة.
    - **الملفات البرمجية:** `test/domain/usecases/network_usecases_test.dart`
    - **فرع Git:** `feature/issue-12-domain-unit-tests`

---

### 👨‍💻 المهندس الثالث: يوسف خيري (`@youssef-khairi`)
* **المسؤولية التقنية:** مهندس طبقة البيانات والتخزين وسياسات الأمان (Data Layer & Telephony Storage Engineer).
* **المسار الهندسي (Epic 3):** `Data Layer, Storage & Security`.
* **الوسم في Trello:** `data-layer`، `storage-security`.

#### المهام الست المسندة للمهندس يوسف خيري:
13. **Issue #13 (US-13): Radio Device DataSource Implementation**
    - **الوصف الهندسي:** كتابة كلاس استدعاء الـ `MethodChannel` وتفكيك قواميس البيانات القادمة من أندرويد مع معالجة استثناءات `PlatformException`.
    - **الملفات البرمجية:** `lib/data/datasources/radio_device_datasource.dart`
    - **فرع Git:** `feature/issue-13-radio-datasource-impl`
14. **Issue #14 (US-14): Concrete NetworkRepository Implementation**
    - **الوصف الهندسي:** بناء المستودع الحقيقي `NetworkRepositoryImpl` وربط مصدر البيانات بتحويل الـ DTOs الخام إلى كيانات النطاق النقية.
    - **الملفات البرمجية:** `lib/data/repositories/network_repository_impl.dart`
    - **فرع Git:** `feature/issue-14-network-repository-impl`
15. **Issue #15 (US-15): Local Storage & Presets Persistence**
    - **الوصف الهندسي:** إدارة التخزين المحلي لاسترجاع النمط المفضل للمستخدم وسجل التبديل عند إعادة تشغيل التطبيق.
    - **الملفات البرمجية:** `lib/data/datasources/local_preferences_datasource.dart`
    - **فرع Git:** `feature/issue-15-local-storage-datasource`
16. **Issue #16 (US-16): Telephony Permissions Engine & Manifest Declarations**
    - **الوصف الهندسي:** إعلان وإدارة الصلاحيات في ملف `AndroidManifest.xml` ومعالجة حالات منح ورفض إذن `READ_PHONE_STATE`.
    - **الملفات البرمجية:** `android/app/src/main/AndroidManifest.xml`
    - **فرع Git:** `feature/issue-16-phone-state-permissions`
17. **Issue #17 (US-17): Unified Failures & Exception Architecture**
    - **الوصف الهندسي:** توحيد كلاسات معالجة الأخطاء والفشل (`PlatformFailure`, `PermissionFailure`) ومنع كراش التطبيق.
    - **الملفات البرمجية:** `lib/core/errors/failures.dart`
    - **فرع Git:** `feature/issue-17-error-failures-engine`
18. **Issue #18 (US-18): Google Play Data Safety Compliance Docs**
    - **الوصف الهندسي:** صياغة وثائق سياسة الخصوصية وأمان البيانات وإثبات أن معالجة التيليمتري تتم محلياً دون أي خوادم خارجية.
    - **الملفات البرمجية:** `docs/PRIVACY_POLICY.md`
    - **فرع Git:** `feature/issue-18-play-store-privacy-docs`

---

### 👨‍💻 المهندس الرابع: مؤيد الصوفي (`@moayed-alsofi`)
* **المسؤولية الإبداعية:** مهندس الواجهات وتجربة المستخدم وإدارة الحالة (UI/UX & Presentation State Engineer).
* **المسار الهندسي (Epic 4):** `Presentation Layer & UI/UX`.
* **الوسم في Trello:** `ui-ux`، `presentation-state`.

#### المهام الست المسندة للمهندس مؤيد الصوفي:
19. **Issue #19 (US-19): Dark Cyberpunk Theme & Design System**
    - **الوصف الهندسي:** بناء الثيم الليلي المتطور (Cyberpunk Dark Navy Palette) ومواءمة درجات التباين للشاشات الحديثة AMOLED.
    - **الملفات البرمجية:** `lib/presentation/theme/app_theme.dart` (أو `lib/main.dart`)
    - **فرع Git:** `feature/issue-19-dark-cyberpunk-theme`
20. **Issue #20 (US-20): Network Status & Tower Visualizer Card**
    - **الوصف الهندسي:** تصميم بطاقة حالة التغطية الحية وبناء عداد الإشارة المكون من 5 أعمدة نيون مضيئة تتفاعل مع حالة البث.
    - **الملفات البرمجية:** `lib/presentation/widgets/network_status_card.dart`
    - **فرع Git:** `feature/issue-20-network-status-card`
21. **Issue #21 (US-21): Prominent Radio Action Button**
    - **الوصف الهندسي:** تصميم وتطوير الزر الرئيسي البارز ذو الإطار النيوني السماوي (Outlined Button) لفتح شاشة المودم بتفاعل نقر غير متزامن.
    - **الملفات البرمجية:** `lib/presentation/widgets/radio_action_button.dart`
    - **فرع Git:** `feature/issue-21-radio-action-button`
22. **Issue #22 (US-22): Real-Time Refresh & Polling Trigger**
    - **الوصف الهندسي:** دمج مراقب دورة حياة التطبيق `WidgetsBindingObserver` مع مؤقت زمني خفيف لتحديث الواجهة تلقائياً عند عودة المستخدم.
    - **الملفات البرمجية:** `lib/presentation/screens/home_screen.dart`
    - **فرع Git:** `feature/issue-22-instant-refresh-action`
23. **Issue #23 (US-23): Contextual Feedback & SnackBar Engine**
    - **الوصف الهندسي:** برمجة الإشعارات العائمة التوجيهية (SnackBars) باللغة العربية لإرشاد المستخدم للخيار المطلوب اختياره من قائمة المودم.
    - **الملفات البرمجية:** `lib/presentation/screens/home_screen.dart`
    - **فرع Git:** `feature/issue-23-snackbar-feedback`
24. **Issue #24 (US-24): Responsive Layout & Orientation Adaptability**
    - **الوصف الهندسي:** ضمان التجاوب التام لواجهة التطبيق مع مختلف أحجام الشاشات وتدوير الجهاز وخلو الواجهة 100% من أخطاء الـ RenderFlex Overflow.
    - **الملفات البرمجية:** `lib/presentation/screens/home_screen.dart`
    - **فرع Git:** `feature/issue-24-responsive-orientation-ui`

---

## 🏗️ الباب السادس: المعمارية البرمجية وسريان البيانات (Clean Architecture)

```
┌──────────────────────────────────────────────────────────┐
│             Presentation Layer (Flutter UI)              │
│       HomeScreen - _NetworkStatusCard - Mode Cards       │
└────────────────────────────┬─────────────────────────────┘
                             │  (Calls)
┌────────────────────────────▼─────────────────────────────┐
│                 Domain Layer (Pure Dart)                 │
│      Use Cases: GetSnapshot, SetMode, OpenRadio          │
│      Entities: NetworkMode, NetworkInfo, NetworkGen      │
└────────────────────────────┬─────────────────────────────┘
                             │  (Implements)
┌────────────────────────────▼─────────────────────────────┐
│                 Data Layer (Repository)                  │
│       NetworkRepositoryImpl ──▶ RadioDeviceDataSource    │
└────────────────────────────┬─────────────────────────────┘
                             │  MethodChannel ('com.netmode.app/radio')
┌────────────────────────────▼─────────────────────────────┐
│              Platform Layer (Kotlin Native)              │
│    MainActivity.kt ──▶ TelephonyManager / Settings.Global│
└──────────────────────────────────────────────────────────┘
```

* **طبقة النطاق (`lib/domain/`):** خالية من أي استيراد لـ Flutter أو أندرويد؛ تضم الكيانات غير القابلة للتعديل (`NetworkMode`, `NetworkInfo`) وعقود المستودعات وحالات الاستخدام المستقلة.
* **طبقة البيانات (`lib/data/`):** تضم فئة `RadioDeviceDataSourceImpl` المتصلة عبر القناة `com.netmode.app/radio`، والمستودع `NetworkRepositoryImpl` الذي يحول البيانات الخام لكائنات نقية.
* **طبقة العرض (`lib/main.dart`):** واجهة مستخدم تفاعلية متطورة تطبق مراقب دورة الحياة `WidgetsBindingObserver` مع مؤقت زمني دوري لتحديث البيانات اللحظية دون تجميد الواجهة.

---

## ⚙️ الباب السابع: محرك النظام الأصلي وحلول سامسونج ويمن موبايل (`MainActivity.kt`)

1. **حل مشكلة شرائح يمن موبايل (CDMA):**
   * شرائح CDMA لا تبث اسم المشغل نصياً عبر `tm.networkOperatorName` فكانت تظهر كـ "No Carrier".
   * تم حلها بالاستعلام من `SubscriptionManager.getActiveSubscriptionInfoList()` وفحص كود الدولة والشبكة الوطني 421، ليظهر بدقة: **`Yemen Mobile`**.
2. **سلسلة النيات التعاقبية لتجاوز حجب كود سامسونج (OEM Fallback Matrix):**
   * استدعاء نافذة `RadioInfo` الأصلية برمجياً عبر سلسلة تعاقبية تتخطى حظر كود `*#*#4636#*#*`:
     - مسار سامسونج: `com.android.phone.settings.RadioInfo`
     - مسار شاومي: `com.android.settings.RadioInfo`
     - البديل الثالث: `com.android.settings.TestingSettings`
     - البديل الرابع: `Settings.ACTION_DATA_ROAMING_SETTINGS`
3. **الاستراتيجية المزدوجة وصلاحية `MODIFY_PHONE_STATE`:**
   * تمنع سامسونج Knox تحويل التردد في الخلفية بدون روت لأن الصلاحية محجوزة لتطبيقات النظام (`/system/priv-app`).
   * **لذا وفر التطبيق مسارين:**
     - في الأجهزة المروّتة (Root): تنفيذ أمر الـ Shell فورياً: `su -c cmd phone set-preferred-network-type [CODE]`.
     - في الأجهزة العادية: فتح نافذة المودم الأصلية بضغطة زر وتوجيه المستخدم للخيار المطلوب من القائمة المنسدلة.

---

## 🛡️ الباب الثامن: الهندسة الدفاعية ورصد وضع الطيران وحالة الشريحة

1. **حل معضلة وضع الطيران (Airplane Mode Logic):**
   * قراءة مسجل النظام الحقيقي في كوتلن:
     ```kotlin
     val isAirplaneMode = Settings.Global.getInt(context.contentResolver, Settings.Global.AIRPLANE_MODE_ON, 0) != 0
     ```
   * بناء شرط الاتصال الدفاعي في فلاتر:
     ```dart
     final isConnected = info != null &&
         info.hasSimCard &&
         !info.isAirplaneMode &&
         info.carrier != 'No Carrier' &&
         info.carrier != 'وضع الطيران';
     ```
   * **النتيجة الفورية:** عند تفعيل الطيران، تنطفئ أعمدة الإشارة السماوية وتتحول إلى رمادي داكن مطفأ، ويتحول نص الحالة فوراً إلى **"وضع الطيران (غير متصلة)"** باللون البرتقالي التحذيري، ويظهر النمط كـ **"الراديو متوقف"**.
2. **كشف الشريحة الفعلي:** إظهار شارة خضراء تفاعلية بأيقونة الشريحة الذهبية `الشريحة متصلة` عند وجودها، وشارة حمراء تحذيرية `الشريحة غير متصلة` عند نزعها.
3. **المزامنة اللحظية الحية:** دمج `WidgetsBindingObserver` لمراقبة عودة المستخدم من إعدادات المودم (`AppLifecycleState.resumed`) وتحديث الواجهة تلقائياً في التو واللحظة.

---

## 🎨 الباب التاسع: واجهة المستخدم والأوضاع الخمسة لليمن

| # | النمط في الواجهة | الخيار المقابل في المودم (RadioInfo) | الغرض والبيئة التقنية في اليمن |
| :-: | :--- | :--- | :--- |
| **1** | **Yemen Mobile+4G** | `CDMA+LTE/EVDO (PRL)` | تثبيت ودمج الفورجي مع الثري جي ليمن موبايل لبقاء الإنترنت والمكالمات معاً. |
| **2** | **Yemen Mobile 3G Only** | `CDMA/EVDO auto (PRL)` | قفل الهاتف على شبكة 3G فقط؛ لتوفير البطارية وفي المناطق الجبلية والريفية. |
| **3** | **sabafon + you** | `GSM/WCDMA/LTE (PRL)` | مخصص لشرائح سبأفون ويو العاملة بنظام GSM للتنقل السلس بين 4G و 3G دون انقطاع. |
| **4** | **VoLTE** | `LTE only` | قفل الهاتف الصارم على 4G فقط؛ لمنع التقطيع نهائياً أثناء ألعاب الأونلاين والتحميل المكثف. |
| **5** | **(Auto)** | `NR/LTE/CDMA/EvDo/GSM/WCDMA` | الوضع التلقائي الشامل لجميع الشبكات والترددات (5G/4G/3G/2G) دون قيود. |

---

## 🚀 الباب العاشر: إدارة التكوين، حماية فروع GitHub وسير العمل

1. **فروع العمل الرسمية للفريق على GitHub:**
   - فرع أحمد: `feature/issue-1-native-platform-and-intents`
   - فرع محمد: `feature/issue-2-domain-contracts-and-usecases`
   - فرع يوسف: `feature/issue-3-data-repository-and-method-channel`
   - فرع مؤيد: `feature/issue-4-presentation-ui-and-visualizer`
   - فرع الاختبارات: `feature/issue-5-permissions-and-edge-cases`
2. **الدمج والحماية على فرع `main`:**
   - دمج كافة الميزات والملفات واختبارات الجودة في فرع `main`.
   - تفعيل قواعد حماية الفرع (Branch Protection Rules) لاشتراط المراجعة وفتح الـ Pull Requests قبل الدمج.
3. **معرض الصور `img/` وملف `README.md`:**
   - تنظيم صور الشاشات الثلاث في مجلد `img/` وعرضها في `README.md` مع شارات الجودة وبيانات الفريق تحت إشراف `د.م. ساهر الهمداني`.

---

## 🎤 الباب الحادي عشر: سيناريو المناقشة الشفهية غداً أمام الدكتور ساهر الهمداني

عند بدء المناقشة، يتحدث كل مهندس بالترتيب التالي:

### 1. الباشمهندس أحمد ياسين العماري (Project Lead & Native Platform Engineer):
> *"بسم الله الرحمن الرحيم. أهلاً بك يا دكتور ساهر. فكرة مشروعنا NET Mode انطلقت لحل مشاكل شبكات الاتصالات في اليمن: تذبذب شبكات 4G و 3G، واختلاف تقنيات CDMA ليمن موبايل عن GSM لسبأفون ويو، وقيام سامسونج بحجب كود المودم `*#*#4636#*#*`.  
> دوري كـ Project Lead شمل إدارة سريان العمل الهندسي (Pipeline) وإدارة المستودع وحوكمة الفروع على GitHub وتطبيق قواعد حماية الفرع الرئيسي `main`.  
> وبرمجياً، توليت المسار الأول (Epic 1: Native Platform) بالمهام من Issue #1 إلى Issue #6 في `MainActivity.kt` بلغة Kotlin؛ حيث تجاوزت حظر كود سامسونج عبر سلسلة من 4 نيات تعاقبية (OEM Fallbacks)، وحللت مشكلة عدم بث الاسم لشرائح يمن موبايل CDMA بالاستعلام من `SubscriptionManager` والكود 421، وبرمجت كشف وضع الطيران من مسجلات النظام الحقيقية لمنع القراءات الكاذبة."*

### 2. الباشمهندس محمد علي / محمد الدعيس (Core Domain & Software Architect):
> *"دكتورنا الفاضل، قمت بتطبيق معمارية Clean Architecture ومبادئ SOLID، بالإضافة إلى توجيهات الذكاء الاصطناعي في ملف `GEMINI.md`.  
> توليت المسار الثاني (Epic 2: Domain Logic) بالمهام من Issue #7 إلى Issue #12؛ حيث قمت بعزل طبقة النطاق `lib/domain/` تماماً ككود Dart نقي خالي 100% من أي استيراد لـ Flutter أو أندرويد لضمان استقلالية منطق الأعمال.  
> صممت الكيانات غير القابلة للتعديل `NetworkMode` و `NetworkInfo` وعقود الـ Repositories وحالات الاستخدام المنفصلة (Use Cases).  
> وأدرت التخطيط في Trello بالربط المباشر مع متطلبات الـ SRS بمعيار IEEE 830، وطبقت معايير إنجاز صارمة (Definition of Done - DoD) تضمن عدم دمج أي مهمة إلا بعد استيفاء اختبارات الوحدة."*

### 3. الباشمهندس يوسف خيري (Data Layer & Telephony Storage Engineer):
> *"أهلاً دكتور. توليت المسار الثالث (Epic 3: Data Layer & Security) بالمهام من Issue #13 إلى Issue #18؛ حيث بنيت مستودع `NetworkRepositoryImpl` وطبقت نمط التجريد لعزل قنوات الاتصال بالمنصة.  
> أنشأت مصدر البيانات `RadioDeviceDataSourceImpl` وربطته بـ `MethodChannel` باسم `com.netmode.app/radio` لنقل بيانات المودم بين دارت وكوتلن بدون تجميد للواجهة وبشكل غير متزامن (Asynchronous)، مع إدارة وحفظ النمط المفضل للمستخدم محلياً وإدارة الصلاحيات في AndroidManifest."*

### 4. الباشمهندس مؤيد الصوفي (UI/UX & Presentation State Engineer):
> *"دكتورنا الكريم، توليت المسار الرابع (Epic 4: Presentation & UI/UX) بالمهام من Issue #19 إلى Issue #24؛ حيث ركزت على بناء تجربة مستخدم تفاعلية متطورة (Cyberpunk Dark Navy Theme) وفق معايير UI/UX Pro Max.  
> صممت بطاقة المراقبة الحية التي تحتوي على 5 أعمدة نيون مضيئة تتفاعل وتتوهج مع إشارة الشبكة وتنطفئ تماماً في وضع الطيران، وشارة ذكية لبطاقة SIM، والأنماط الخمسة المخصصة لمشغلي اليمن.  
> كما قمت بدمج فئة `WidgetsBindingObserver` مع دورة حياة التطبيق، مما جعل الواجهة تُحدث نفسها تلقائياً فور عودة المستخدم من إعدادات المودم أو فور تفعيل وضع الطيران دون الحاجة للمس الشاشة."*
