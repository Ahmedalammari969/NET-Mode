# مهام المشروع وسير عمل Git

## مهام الـ Kanban الخمس (GitHub Issues)

1. **Issue #1: Project Setup & Platform Configuration**
   - **الوصف:** إعداد مشروع Flutter، تجهيز الصلاحيات في `AndroidManifest.xml` وتكوين معمارية Clean Architecture.
   - **Label:** `setup`

2. **Issue #2: Network State Domain Model & Repository Contract**
   - **الوصف:** بناء كائنات النطاق المجردة (`NetworkInfo`, `NetworkMode`) وعقود الـ Repository بدون أي مكتبات خارجية.
   - **Label:** `domain`

3. **Issue #3: Platform Channels & Local Storage Implementation**
   - **الوصف:** تنفيذ طبقة البيانات للاتصال بخدمات الأندرويد الأصلية وحفظ التفضيلات عبر محرك محلي.
   - **Label:** `data`

4. **Issue #4: UI/UX Pro Max Dashboard & Signal Visualizer**
   - **الوصف:** تصميم شاشة التطبيق الرئيسية والداكنة ومؤشرات قوة الإشارة والتحكم بالأنماط.
   - **Label:** `ui`

5. **Issue #5: Permissions & Edge Cases Handling**
   - **الوصف:** معالجة رفض الأذونات، وضع الطيران، وفقدان الاتصال مع إضافة اختبارات التحقق.
   - **Label:** `enhancement`

---

## سير عمل Git الإلزامي (Git Workflow)

```bash
# 1. المزامنة من الفرع الرئيسي
git checkout main
git pull origin main

# 2. إنشاء فرع للمهمة (مثال لمهمة الـ Domain)
git checkout -b feature/issue-2-network-domain

# 3. تسجيل التغييرات بـ Commit وفق المعيار
git add .
git commit -m "feat: define NetworkMode entity and repository contracts (#2)"

# 4. الرفع إلى المستودع
git push -u origin feature/issue-2-network-domain