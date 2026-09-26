# لوحة مهام كانبان وسير عمل Git الهندسي (Kanban Board & Git Workflow)
## مشروع تطبيق: NET Mode (Cellular Network & Radio Testing Suite)
**المنهجية:** Agile Scrum / Kanban Driven Development  
**فريق العمل:** أحمد العماري، محمد الدعيس، يوسف خيري، مؤيد الصوفي  
**إجمالي المهام الهندسية (Issues):** 24 مهمة موزعة على 4 حزم عمل رئيسية (Milestones)

---

## 1. هيكل لوحة كانبان وتوزيع مهام الـ Issues

### المسار الأول: طبقة المنصة وهندسة الراديو (Epic 1: Native Platform & Radio RIL)
**المسؤول (Assignee):** أحمد العماري (`@ahmed-alammari`)  
**الوسم (Label):** `native-android`, `hardware-ril`

1. **Issue #1 (US-01): Samsung Radio Intent Launcher**
   - **الوصف:** بناء دالة Intent مخصصة تستهدف `com.android.phone.settings.RadioInfo` لأجهزة OneUI.
   - **الملف:** `android/app/src/main/kotlin/.../MainActivity.kt`
   - **الفرع:** `feature/issue-1-samsung-radio-intent`
2. **Issue #2 (US-02): Xiaomi & AOSP Fallback Intent Chain**
   - **الوصف:** استدعاء مسار `com.android.settings.RadioInfo` وبديل `TestingSettings` لأجهزة شاومي والأندرويد الخام.
   - **الملف:** `android/app/src/main/kotlin/.../MainActivity.kt`
   - **الفرع:** `feature/issue-2-xiaomi-aosp-fallback`
3. **Issue #3 (US-03): Telephony RIL Modem Network Decoder**
   - **الوصف:** قراءة وتصنيف أكواد المودم الحقيقية من `TelephonyManager` لمسميات واضحة (4G LTE, 5G NR).
   - **الملف:** `android/app/src/main/kotlin/.../MainActivity.kt`
   - **الفرع:** `feature/issue-3-ril-telephony-decoder`
4. **Issue #4 (US-04): Native MethodChannel Bridge Architecture**
   - **الوصف:** إعداد القناة الموحدة `com.netmode.app/radio` ونقل البيانات دون تسريب ذاكرة.
   - **الملف:** `android/app/src/main/kotlin/.../MainActivity.kt`
   - **الفرع:** `feature/issue-4-platform-method-channel`
5. **Issue #5 (US-05): SIM State & Airplane Mode Native Inspector**
   - **الوصف:** قراءة إعدادات النظام اللحظية لوضع الطيران وجاهزية شريحة الاتصال.
   - **الملف:** `android/app/src/main/kotlin/.../MainActivity.kt`
   - **الفرع:** `feature/issue-5-sim-airplane-inspector`
6. **Issue #6 (US-06): System Security Lockout & Exception Catching**
   - **الوصف:** التقاط أخطاء Knox و Security Policies وإرجاع استجابات آمنة للواجهة.
   - **الملف:** `android/app/src/main/kotlin/.../MainActivity.kt`
   - **الفرع:** `feature/issue-6-security-exception-handler`

---

### المسار الثاني: معمارية النطاق والمنطق المجرد (Epic 2: Clean Architecture & Domain Logic)
**المسؤول (Assignee):** محمد الدعيس (`@mohammed-alduais`)  
**الوسم (Label):** `clean-domain`, `core-logic`

7. **Issue #7 (US-07): Pure NetworkInfo Entity Definition**
   - **الوصف:** بناء كائن بيانات Dart نقي غير قابل للتعديل يمثل قياسات الشبكة والمودم.
   - **الملف:** `lib/domain/entities/network_info.dart`
   - **الفرع:** `feature/issue-7-network-info-entity`
8. **Issue #8 (US-08): NetworkMode Presets & RIL Types Entity**
   - **الوصف:** تعريف كيان الأنماط (LTE Only, NR, GSM) وربطها بأكواد أندرويد المعيارية.
   - **الملف:** `lib/domain/entities/network_mode.dart`
   - **الفرع:** `feature/issue-8-network-mode-entity`
9. **Issue #9 (US-09): Abstract NetworkRepository Interface**
   - **الوصف:** صياغة عقد المستودع المجرد لعزل النطاق وتطبيق مبدأ عكس التبعية (DIP).
   - **الملف:** `lib/domain/repositories/network_repository.dart`
   - **الفرع:** `feature/issue-9-network-repository-contract`
10. **Issue #10 (US-10): Get Instant Network Snapshot UseCase**
    - **الوصف:** تنفيذ حالة استخدام جلب بيانات الشبكة اللحظية بنمط دالي نقي وفق مبدأ SRP.
    - **الملف:** `lib/domain/usecases/network_usecases.dart`
    - **الفرع:** `feature/issue-10-get-snapshot-usecase`
11. **Issue #11 (US-11): Open Radio Settings Controller UseCase**
    - **الوصف:** بناء حالة استخدام مستقلة لعزل طلب فتح شاشات الراديو عن الواجهة.
    - **الملف:** `lib/domain/usecases/network_usecases.dart`
    - **الفرع:** `feature/issue-11-open-radio-usecase`
12. **Issue #12 (US-12): Domain Unit Testing Suite (100% Pass)**
    - **الوصف:** كتابة واجتياز اختبارات الوحدة الآلية لطبقة النطاق باستخدام Mock Repositories.
    - **الملف:** `test/domain/usecases/network_usecases_test.dart`
    - **الفرع:** `feature/issue-12-domain-unit-tests`

---

### المسار الثالث: طبقة البيانات والتخزين وسياسات الأمان (Epic 3: Data Layer, Storage & Security)
**المسؤول (Assignee):** يوسف خيري (`@youssef-khairi`)  
**الوسم (Label):** `data-layer`, `storage-security`

13. **Issue #13 (US-13): Radio Device DataSource Implementation**
    - **الوصف:** كتابة كلاس استدعاء `MethodChannel` وتفكيك قواميس البيانات مع معالجة `PlatformException`.
    - **الملف:** `lib/data/datasources/radio_device_datasource.dart`
    - **الفرع:** `feature/issue-13-radio-datasource-impl`
14. **Issue #14 (US-14): Concrete NetworkRepository Implementation**
    - **الوصف:** ربط المستودع الحقيقي بمصدر البيانات وتحويل DTOs إلى كيانات Domain.
    - **الملف:** `lib/data/repositories/network_repository_impl.dart`
    - **الفرع:** `feature/issue-14-network-repository-impl`
15. **Issue #15 (US-15): Local Storage & Presets Persistence**
    - **الوصف:** حفظ واسترجاع النمط المفضل وسجل الأنماط محلياً في ذاكرة التخزين الدائمة.
    - **الملف:** `lib/data/datasources/local_preferences_datasource.dart`
    - **الفرع:** `feature/issue-15-local-storage-datasource`
16. **Issue #16 (US-16): Telephony Permissions Engine & Manifest Declarations**
    - **الوصف:** إدارة أذونات `READ_PHONE_STATE` ومعالجة حالات المنح والرفض دون أخطاء.
    - **الملف:** `android/app/src/main/AndroidManifest.xml`
    - **الفرع:** `feature/issue-16-phone-state-permissions`
17. **Issue #17 (US-17): Unified Failures & Exception Architecture**
    - **الوصف:** توحيد كلاسات الأخطاء (`PlatformFailure`, `PermissionFailure`) ومنع الانهيار.
    - **الملف:** `lib/core/errors/failures.dart`
    - **الفرع:** `feature/issue-17-error-failures-engine`
18. **Issue #18 (US-18): Google Play Data Safety Compliance Docs**
    - **الوصف:** صياغة إقرار أمان البيانات وسياسة الخصوصية التي تؤكد المعالجة المحلية فقط.
    - **الملف:** `docs/PRIVACY_POLICY.md`
    - **الفرع:** `feature/issue-18-play-store-privacy-docs`

---

### المسار الرابع: واجهة المستخدم وتجربة الاستخدام (Epic 4: Presentation Layer & UI/UX)
**المسؤول (Assignee):** مؤيد الصوفي (`@moayed-alsofi`)  
**الوسم (Label):** `ui-ux`, `presentation-state`

19. **Issue #19 (US-19): Dark Cyberpunk Theme & Design System**
    - **الوصف:** تكوين الثيم الداكن الاحترافي ومكتبة الألوان المريحة للعين وتوفير طاقة شاشات AMOLED.
    - **الملف:** `lib/presentation/theme/app_theme.dart`
    - **الفرع:** `feature/issue-19-dark-cyberpunk-theme`
20. **Issue #20 (US-20): Network Status & Tower Visualizer Card**
    - **الوصف:** بناء بطاقة حالة التغطية لعرض المشغل ونوع التقنية ومؤشر التحميل الدائري.
    - **الملف:** `lib/presentation/widgets/network_status_card.dart`
    - **الفرع:** `feature/issue-20-network-status-card`
21. **Issue #21 (US-21): Prominent Radio Action Button**
    - **الوصف:** تصميم زر الفتح السريع لـ LTE Only بتأثيرات بصرية ونقر غير متزامن.
    - **الملف:** `lib/presentation/widgets/radio_action_button.dart`
    - **الفرع:** `feature/issue-21-radio-action-button`
22. **Issue #22 (US-22): Real-Time Refresh & Polling Trigger**
    - **الوصف:** برمجة زر التحديث اللحظي للبيانات الخلوية وإعادة بناء الشاشة فورياً عبر `setState`.
    - **الملف:** `lib/presentation/screens/home_screen.dart`
    - **الفرع:** `feature/issue-22-instant-refresh-action`
23. **Issue #23 (US-23): Contextual Feedback & SnackBar Engine**
    - **الوصف:** إظهار إشعارات منبثقة تفاعلية باللغة العربية عند تعذر الفتح التلقائي للقائمة.
    - **الملف:** `lib/presentation/screens/home_screen.dart`
    - **الفرع:** `feature/issue-23-snackbar-feedback`
24. **Issue #24 (US-24): Responsive Layout & Orientation Adaptability**
    - **الوصف:** ضمان تجاوب واجهة التطبيق مع مختلف أحجام الشاشات وتدوير الجهاز وخلوه من أخطاء الـ Overflow.
    - **الملف:** `lib/presentation/screens/home_screen.dart`
    - **الفرع:** `feature/issue-24-responsive-orientation-ui`

---

## 2. بروتوكول وسير عمل Git القياسي (Standard Git Workflow)

لكل عضو من الفريق، يتم تنفيذ المهام وفق دورة حياة Git الصارمة التالية:

### الخطوة 1: المزامنة وسحب آخر تحديثات من الفرع الرئيسي
```bash
git checkout main
git pull origin main
```

### الخطوة 2: إنشاء الفرع المستقل للمهمة (Branch Creation)
يتم تفريع كود الميزة بالاسم المعياري المرتبط برقم الـ Issue:
```bash
# مثال لمحمد الدعيس للعمل على Issue 7:
git checkout -b feature/issue-7-network-info-entity

# مثال لمؤيد الصوفي للعمل على Issue 20:
git checkout -b feature/issue-20-network-status-card
```

### الخطوة 3: التطوير والتحقق الهندسي المحلي
قبل عمل Commit، يتأكد المطور من سلامة الكود والاختبارات:
```bash
flutter analyze
flutter test
```

### الخطوة 4: التجهيز وحفظ التعديلات (Commit Standards)
صيغة رسالة الـ Commit الاحترافية وفق المعيار المعتمد (Conventional Commits):
```bash
git add .
git commit -m "feat(domain): implement pure NetworkInfo entity and equality tests [Closes #7]"
```

### الخطوة 5: رفع الفرع إلى المستودع السحابي (Push to GitHub)
```bash
git push -u origin feature/issue-7-network-info-entity
```

### الخطوة 6: فتح ومراجعة طلب الدمج (Pull Request Workflow)
1. الدخول على GitHub وفتح **Pull Request** موجه من `feature/issue-X-...` نحو `main` (أو `develop`).
2. إضافة مراجعين (Reviewers) من الفريق.
3. التأكد من نجاح اختبارات الـ CI التلقائية (GitHub Actions).
4. عند الموافقة يتم الدمج (Squash and merge أو Create a merge commit).
5. تنظيف الفرع المحلي بعد الدمج:
```bash
git checkout main
git pull origin main
git branch -d feature/issue-7-network-info-entity
```

---

## 3. دليل تطبيق لوحة كانبان على Trello بالتفصيل (Trello Board Setup)

لتنسيق العمل الجماعي بين أعضاء الفريق الأربعة (أحمد، محمد، يوسف، مؤيد)، يتم إنشاء لوحة Trello وضبطها كالتالي:

### 1. إعداد أعمدة اللوحة (Trello Lists)
أنشئ 5 قوائم رئيسية بالترتيب:
1. 📋 **Backlog (المخزون العام):** تُوضع فيه جميع بطاقات الـ 24 Issue غير المجدولة حالياً.
2. ⏳ **To Do (جاهز للتنفيذ):** المهام المجدولة للأسبوع أو الدورة الحالية وتنتظر بدء العمل.
3. 🚀 **In Progress (قيد التنفيذ):** **قاعدة ذهبية:** لا يجوز للعضو وضع أكثر من بطاقة واحدة في هذا العمود.
4. 👀 **In Review / PR (قيد المراجعة):** البطاقات التي تم رفع فروعها على GitHub وفُتح لها Pull Request وتنتظر موافقة الزميل.
5. ✅ **Done (تم الإنجاز):** المهام التي تم دمج الـ PR الخاص بها في `main` واجتازت الاختبارات.

### 2. تصنيف وتلوين البطاقات (Labels)
- 🟢 **أخضر (Native Android):** مهام أحمد العماري (Issues #1 to #6)
- 🔵 **أزرق (Clean Domain):** مهام محمد الدعيس (Issues #7 to #12)
- 🟣 **بنفسجي (Data & Security):** مهام يوسف خيري (Issues #13 to #18)
- 🟠 **برتقالي (UI/UX):** مهام مؤيد الصوفي (Issues #19 to #24)

### 3. مكونات بطاقة الـ Trello النموذجية
عند إنشاء بطاقة لكل مهمة، اجعل محتواها كالآتي:
- **العنوان:** `[Issue #7] Pure NetworkInfo Entity Definition`
- **العضو المسند (Member):** إضافة حساب العضو المسؤول.
- **التصنيف (Label):** `Clean Domain`.
- **الوصف (Description):**
  - مسار الملف: `lib/domain/entities/network_info.dart`
  - اسم الفرع المقترح: `feature/issue-7-network-info-entity`
  - معايير القبول (Checklist):
    - [ ] كتابة كلاس الـ Entity
    - [ ] اختبار `flutter analyze`
    - [ ] رفع الفرع وفتح PR
- **المرفقات (Attachments):** بمجرد فتح الـ PR على GitHub، يقوم المطور بنسخ رابط الـ PR ولصقه داخل البطاقة.

### 4. دورة المزامنة اليومية بين Trello و Git:
```
[Trello: To Do]
       │
       ▼ (يسحب العضو البطاقة)
[Trello: In Progress] ───────► (ينشئ الفرع: git checkout -b feature/...)
                                    │
                                    ▼ (يكتب الكود ويرفع: git push)
[Trello: In Review / PR] ◄──── (يفتح Pull Request على GitHub)
       │
       ▼ (يراجع الزملاء ويدمجون الكود)
[Trello: Done] ✅
```