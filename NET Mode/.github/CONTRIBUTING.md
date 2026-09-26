# 🚀 دليل المساهمة والعمل الجماعي لفريق مشروع NET Mode
## (Team Git & Trello Collaboration Guide)

مرحباً بك في فريق عمل **NET Mode**! هذا الدليل مخصص لأعضاء الفريق:
- **أحمد العماري** (Native Platform & Android Lead)
- **محمد الدعيس** (Clean Architecture & Domain Logic Lead)
- **يوسف خيري** (Data Layer, Storage & Security Lead)
- **مؤيد الصوفي** (UI/UX & Presentation Lead)

---

## 📌 القواعد الذهبية للفريق (Golden Rules)
1. **ممنوع الرفع المباشر على فرع `main` مطلقاً.**
2. **كل مهمة لها فرع خاص بها (Branch)** يتم إنشاؤه من أحدث نسخة لـ `main`.
3. **لا يُدمج أي فرع إلا بعد عمل Pull Request (PR)** واجتياز الفحص الآلي.
4. **بطاقة Trello يجب أن تعكس حالتك اللحظية** (In Progress عند بدء العمل، In Review عند فتح الـ PR، Done بعد الدمج).

---

## 🛠️ دورة العمل خطوة بخطوة (Step-by-Step Workflow)

### 1️⃣ اختيار المهمة من Trello
1. ادخل إلى لوحة **Trello** الخاصة بمشروع NET Mode.
2. اذهب إلى قائمة **To Do**، واختر البطاقة المسندة إليك (مثلاً: `Issue #7: Pure NetworkInfo Entity Definition`).
3. انقل البطاقة إلى قائمة **In Progress**.
4. تأكد أنك لا تضع أكثر من بطاقة واحدة في **In Progress** في نفس الوقت.

---

### 2️⃣ تجهيز الفرع الجديد على جهازك (Create Branch)
افتح الـ Terminal داخل مجلد المشروع ونفّذ:

```bash
# 1. الانتقال إلى الفرع الرئيسي
git checkout main

# 2. سحب آخر التحديثات التي دمجها باقي الفريق
git pull origin main

# 3. إنشاء فرعك الخاص والانتقال إليه مباشرة (استخدم التسمية المعيارية)
git checkout -b feature/issue-7-network-info-entity
```

> **صيغة تسمية الفروع:**  
> `feature/issue-<رقم المهمة>-<اسم-المهمة-باختصار>`

---

### 3️⃣ العمل وكتابة الكود والتحقق
أثناء كتابة الكود:
1. التزم بالطبقة الخاصة بك في **Clean Architecture**.
2. تأكد من خلو مشروعك من الأخطاء:
```bash
# فحص الكود والتأكد من عدم وجود أخطاء لانتينغ
flutter analyze

# تشغيل الاختبارات
flutter test
```

---

### 4️⃣ حفظ التعديلات وعمل Commit
عندما تنهي جزءاً من مهمتك أو المهمة كاملة:

```bash
# 1. رؤية الملفات المعدلة
git status

# 2. إضافة الملفات المعدلة
git add .

# 3. كتابة رسالة توضيحية احترافية تتضمن رقم الـ Issue
git commit -m "feat(domain): implement NetworkInfo entity with equality support [Issue #7]"
```

---

### 5️⃣ رفع الفرع إلى GitHub (Push)
ارفع فرعك إلى المستودع البعيد:

```bash
# في المرة الأولى لرفع الفرع:
git push -u origin feature/issue-7-network-info-entity

# في المرات اللاحقة على نفس الفرع يكفيك كتابة:
git push
```

---

### 6️⃣ فتح Pull Request وربطه مع Trello
1. ادخل على مستودع المشروع في GitHub:  
   `https://github.com/Ahmedalammari969/NET-Mode`
2. ستجد زراً أصفر يظهر تلقائياً: **"Compare & pull request"**، اضغط عليه.
3. اكتب عنواناً واضحاً، مثلاً: `feat(domain): Issue #7 - Pure NetworkInfo Entity Definition`.
4. املأ القالب المعروض:
   - ضع رابط بطاقة Trello الخاصة بك.
   - اكتب رقم الـ Issue (مثال: `Closes #7`).
   - اختر أعضاء الفريق لمراجعة الكود (Reviewers).
5. اضغط **Create pull request**.
6. اذهب فوراً إلى **Trello** وانقل بطاقتك من **In Progress** إلى **In Review / PR** وضع رابط الـ PR داخل البطاقة كتعليق.

---

### 7️⃣ مراجعة الكود والدمج (Code Review & Merge)
1. يقوم قائد المسار أو الزميل بمراجعة الكود في GitHub والاطلاع على الفحص الآلي (GitHub Actions CI).
2. عند الموافقة (Approve):
   - يتم الضغط على **Merge pull request**.
3. في **Trello**: انقل البطاقة إلى **Done** 🚀.
4. على جهازك: ارجع للرئيسي واحذف الفرع القديم المنتهي:
```bash
git checkout main
git pull origin main
git branch -d feature/issue-7-network-info-entity
```
