import os
import base64
import subprocess

workspace_dir = r"D:\FOR\A\eng\NET Mode\NET Mode"
html_path = os.path.join(workspace_dir, "report.html")
pdf_path = os.path.join(workspace_dir, "NET_Mode_Final_Report.pdf")

app_screen_path = os.path.join(workspace_dir, "app_screen.png")
device_screen_path = os.path.join(workspace_dir, "device_screen.png")

with open(app_screen_path, "rb") as f:
    app_screen_b64 = base64.b64encode(f.read()).decode("utf-8")

with open(device_screen_path, "rb") as f:
    device_screen_b64 = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>تقرير مشروع NET Mode النهائي</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap');
        
        @page {{
            size: A4;
            margin: 18mm 15mm 18mm 15mm;
            @bottom-right {{
                content: "صفحة " counter(page);
                font-family: 'Tajawal', sans-serif;
                font-size: 10pt;
                color: #64748b;
            }}
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Tajawal', 'Segoe UI', Tahoma, sans-serif;
            background-color: #ffffff;
            color: #0f172a;
            line-height: 1.8;
            font-size: 11pt;
        }}

        .page-break {{
            page-break-after: always;
            break-after: page;
        }}

        /* Cover Page */
        .cover-page {{
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0369a1 100%);
            color: #ffffff;
            border-radius: 16px;
        }}

        .cover-header {{
            margin-top: 40px;
        }}

        .badge-tag {{
            display: inline-block;
            background: rgba(56, 189, 248, 0.2);
            color: #38bdf8;
            border: 1px solid #38bdf8;
            padding: 6px 18px;
            border-radius: 20px;
            font-size: 12pt;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 20px;
        }}

        .cover-title {{
            font-size: 38pt;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 10px;
            letter-spacing: 1px;
        }}

        .cover-subtitle {{
            font-size: 20pt;
            font-weight: 700;
            color: #38bdf8;
            margin-bottom: 20px;
        }}

        .cover-desc {{
            font-size: 13pt;
            color: #cbd5e1;
            max-width: 650px;
            line-height: 1.8;
        }}

        .cover-tech {{
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 30px;
        }}

        .tech-box {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 10px 24px;
            border-radius: 12px;
            font-size: 12pt;
            font-weight: 600;
            color: #f8fafc;
        }}

        .cover-footer {{
            width: 100%;
            display: flex;
            justify-content: space-around;
            background: rgba(0, 0, 0, 0.35);
            padding: 24px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
        }}

        .meta-card {{
            text-align: center;
        }}

        .meta-label {{
            font-size: 11pt;
            color: #94a3b8;
            margin-bottom: 6px;
        }}

        .meta-val {{
            font-size: 15pt;
            font-weight: 800;
            color: #ffffff;
        }}

        /* Content Pages */
        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 8px;
            margin-bottom: 24px;
            font-size: 9pt;
            color: #64748b;
        }}

        h1 {{
            font-size: 20pt;
            font-weight: 800;
            color: #0369a1;
            margin-bottom: 16px;
            border-right: 5px solid #0284c7;
            padding-right: 12px;
        }}

        h2 {{
            font-size: 15pt;
            font-weight: 700;
            color: #1e293b;
            margin-top: 22px;
            margin-bottom: 12px;
        }}

        h3 {{
            font-size: 12pt;
            font-weight: 700;
            color: #0284c7;
            margin-top: 16px;
            margin-bottom: 8px;
        }}

        p {{
            margin-bottom: 12px;
            text-align: justify;
            color: #334155;
        }}

        .card-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-right: 4px solid #0284c7;
            padding: 14px 18px;
            border-radius: 8px;
            margin-bottom: 16px;
        }}

        .alert-box {{
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            border-right: 4px solid #2563eb;
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 16px;
            font-size: 10.5pt;
            color: #1e40af;
        }}

        .warning-box {{
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-right: 4px solid #d97706;
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 16px;
            font-size: 10.5pt;
            color: #92400e;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 18px 0;
            font-size: 10pt;
        }}

        th {{
            background-color: #0f172a;
            color: #ffffff;
            font-weight: 700;
            padding: 10px 12px;
            text-align: right;
            border: 1px solid #0f172a;
        }}

        td {{
            padding: 10px 12px;
            border: 1px solid #cbd5e1;
            color: #1e293b;
        }}

        tr:nth-child(even) {{
            background-color: #f1f5f9;
        }}

        .badge-chip {{
            display: inline-block;
            background: #e0f2fe;
            color: #0369a1;
            padding: 2px 8px;
            border-radius: 4px;
            font-family: monospace;
            font-weight: 700;
            font-size: 9.5pt;
        }}

        code {{
            background: #f1f5f9;
            color: #0f172a;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: Consolas, monospace;
            font-size: 9.5pt;
            border: 1px solid #e2e8f0;
        }}

        pre {{
            background: #0f172a;
            color: #e2e8f0;
            padding: 14px;
            border-radius: 8px;
            font-family: Consolas, monospace;
            font-size: 9pt;
            overflow-x: auto;
            margin: 14px 0;
            direction: ltr;
            text-align: left;
            line-height: 1.5;
        }}

        .images-grid {{
            display: flex;
            justify-content: space-around;
            gap: 20px;
            margin: 20px 0;
        }}

        .screen-container {{
            flex: 1;
            text-align: center;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 12px;
        }}

        .screen-img {{
            max-height: 480px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            border: 2px solid #0f172a;
        }}

        .screen-caption {{
            font-size: 10pt;
            font-weight: 700;
            color: #0369a1;
            margin-top: 10px;
        }}
        
        ul, ol {{
            margin-right: 24px;
            margin-bottom: 14px;
        }}

        li {{
            margin-bottom: 6px;
            color: #334155;
        }}
    </style>
</head>
<body>

    <!-- ══════════ الغلاف (Cover Page) ══════════ -->
    <div class="cover-page page-break">
        <div class="cover-header">
            <div class="badge-tag">مشروع تخرج / تقرير هندسي متقدم</div>
            <div class="cover-title">NET Mode</div>
            <div class="cover-subtitle">إدارة وتثبيت أنماط شبكات الهاتف الخلوي</div>
            <div class="cover-desc">
                تطبيق احترافي لإدارة وتثبيت أنماط الشبكات للهواتف الذكية مع دعم خاص لشركات الاتصالات والترددات في الجمهورية اليمنية (CDMA/EVDO & GSM/LTE).
            </div>
            <div class="cover-tech">
                <div class="tech-box">Flutter Framework</div>
                <div class="tech-box">Kotlin Native</div>
                <div class="tech-box">Clean Architecture</div>
            </div>
        </div>

        <div class="cover-footer">
            <div class="meta-card">
                <div class="meta-label">إعداد الطالب</div>
                <div class="meta-val">أحمد ياسين العماري</div>
            </div>
            <div class="meta-card">
                <div class="meta-label">إشراف الدكتور</div>
                <div class="meta-val">سليمان الشوصي</div>
            </div>
            <div class="meta-card">
                <div class="meta-label">العام الأكاديمي</div>
                <div class="meta-val">2026 م</div>
            </div>
        </div>
    </div>

    <!-- ══════════ الصفحة 1: المقدمة والأهداف ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الأول: المقدمة التنفيذية</span>
        </div>

        <h1>1. المقدمة التنفيذية وأهداف المشروع</h1>
        
        <p>
            تعد شبكات الاتصال الخلوية الركيزة الأساسية للاتصالات الرقمية المعاصرة. وتتميز البيئة اليمنية بخصوصية تقنية استثنائية؛ حيث تتوزع التغطية بين مشغل يعمل بالنظام الهجين <b>CDMA/EVDO و 4G LTE</b> (شركة يمن موبايل)، ومشغلين يعملون بالنظام الدولي <b>GSM/WCDMA/LTE</b> (شركتي سبأفون ويو).
        </p>

        <div class="alert-box">
            <b>المعضلة الهندسية في السوق المحلي:</b> يعاني المشتركون من تكرار هبوط نمط الاتصال تلقائياً من 4G عالي السرعة إلى 3G أو انقطاع بث الإنترنت أثناء المكالمات الهاتفية، فضلاً عن قيام واجهات الهواتف الحديثة (خاصة سامسونج One UI) بحجب إمكانية قفل النمط على الفورجي فقط من قائمة الإعدادات العادية، وحظر الأكواد السرية في لوحة الاتصال.
        </div>

        <h2>الأهداف الأساسية للمشروع:</h2>
        <ul>
            <li><b>إدارة وتثبيت الترددات الخلوية:</b> إتاحة التثبيت الصارم على نمط الجيل الرابع (VoLTE/LTE Only) أو دمج الأنماط الهجينة لمنع انقطاع الاتصال.</li>
            <li><b>مواءمة الشبكات اليمنية:</b> دعم كامل لترددات شرائح CDMA وشرائح GSM مع حل مشاكل فقدان اسم المشغل.</li>
            <li><b>تجاوز حجب الأكواد السرية:</b> استدعاء شاشة فحص المودم (RadioInfo) برمجياً عبر الـ Intents الأصلية دون الحاجة لكتابة كود <code>*#*#4636#*#*</code>.</li>
            <li><b>مراقبة لحظية ذكية:</b> عرض قوة الإشارة، نوع الشبكة الفعلي، وضع الطيران، وحالة بطاقة SIM في واجهة عصرية متطورة.</li>
        </ul>

        <h2>القيمة المضافة للمستخدم:</h2>
        <div class="card-box">
            يوفر تطبيق <b>NET Mode</b> تجربة مستخدم رائدة تجمع بين بساطة واجهات Flutter وقوة الاتصال المباشر مع طبقة العتاد عبر Kotlin، مما يمنح المستخدم سيطرة كاملة ومباشرة على رقاقة المودم الراديوي.
        </div>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الصفحة 2: المعمارية البرمجية ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الثاني: المعمارية البرمجية</span>
        </div>

        <h1>2. المعمارية البرمجية وسريان البيانات</h1>

        <p>
            تم بناء المشروع بالاعتماد على معمارية <b>Clean Architecture</b> ومبادئ <b>SOLID</b>، بهدف فصل منطق الأعمال النقي عن واجهات العرض وأكواد النظام الأصلية.
        </p>

        <div class="card-box">
            <b>1. طبقة النطاق (Domain Layer - Pure Dart):</b>
            <p>طبقة نقية بنسبة 100% خالية من أي استيراد لمكتبات Flutter أو Android. تشتمل على الكيانات الأساسية:</p>
            <ul>
                <li><code>NetworkMode</code>: يحمل معرّف النمط، اسمه الظاهر، كود المودم الداخلي (RIL Code)، والجيل الخلوي.</li>
                <li><code>NetworkInfo</code>: كيان يحمل بيانات التيليمتري اللحظية (المشغل، نوع الاتصال، حالة الشريحة، وضع الطيران).</li>
                <li><code>Use Cases</code>: تضم حالات الاستخدام المنفصلة (GetSnapshot, SetMode, OpenRadio, ManagePreferred).</li>
            </ul>
        </div>

        <div class="card-box">
            <b>2. طبقة البيانات (Data Layer):</b>
            <p>تتضمن مستودع البيانات <code>NetworkRepositoryImpl</code> ومصدر البيانات <code>RadioDeviceDataSource</code>، الذي يتصل مباشرة بنظام أندرويد عبر قناة اتصال مشتركة:</p>
            <pre>static const _channel = MethodChannel('com.netmode.app/radio');</pre>
        </div>

        <div class="card-box">
            <b>3. طبقة العرض (Presentation Layer - Flutter UI):</b>
            <p>واجهة تفاعلية مبنية بثيم داكن فخم (Cyberpunk Navy) مع دعم التحديث التلقائي الفوري عبر <code>WidgetsBindingObserver</code> عند العودة من الخلفية ومؤقت دوري خفيف كل 3 ثوانٍ.</p>
        </div>

        <h2>مخطط سريان البيانات (Data Flow):</h2>
        <pre>
 [ Flutter UI ] ────▶ [ Use Cases ] ────▶ [ Repository ]
       ▲                                         │
       │                                         ▼
 [ Reactive State ] ◀─── [ MethodChannel ] ◀─── [ Kotlin Native ]
        </pre>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الصفحة 3: التحليل الأمني وسامسونج ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الثالث: التحليل الأمني وأندرويد</span>
        </div>

        <h1>3. التحليل الأمني لنظام أندرويد وواجهة سامسونج</h1>

        <p>
            تفرض أنظمة أندرويد الحديثة (Android 11 وما فوق) وحماية سامسونج <b>Knox</b> قيوداً أمنية بالغة الصرامة على تعديل ترددات المودم الخلوي في الخلفية.
        </p>

        <h2>لماذا تمنع أنظمة أندرويد التحويل الصامت المباشر؟</h2>
        <ul>
            <li>الصلاحية المسؤولة عن تحويل نمط المودم هي: <code>android.permission.MODIFY_PHONE_STATE</code>.</li>
            <li>تُصنف هذه الصلاحية أمنياً كـ <b>(signature|privileged)</b>؛ أي أنها محجوزة حصرياً لتطبيقات النظام المدمجة في الروم الرسمي داخل <code>/system/priv-app</code>.</li>
            <li>إذا حاول أي تطبيق عادي استدعاء دالة تغيير النمط برمجياً بدون روت، يرمي النظام فوراً استثناء أمني:</li>
        </ul>

        <pre>SecurityException: Neither user nor current process has MODIFY_PHONE_STATE</pre>

        <h2>استراتيجية التطبيق المزدوجة الذكية (Hybrid Strategy):</h2>
        
        <div class="alert-box">
            <b>أ) في الأجهزة التي تملك صلاحيات الروت (Root / Magisk):</b><br>
            يقوم التطبيق بالتحويل الصامت المباشر للترددات في الخلفية عبر سطر أوامر Root Shell دون أي تدخل يدوي:
            <br><code>su -c cmd phone set-preferred-network-type [CODE]</code>
        </div>

        <div class="warning-box">
            <b>ب) في الأجهزة العادية (بدون روت - Non-Root):</b><br>
            يقوم التطبيق بفتح نافذة المودم الداخلية السرية <b>Phone info</b> تلقائياً بضغطة زر واحدة عبر Intent محمي، ويرشد المستخدم عبر إشعار عائم بالخيار المطابق لاختياره في القائمة المنسدلة.
        </div>

        <h2>آلية تجاوز حجب كود (*#*#4636#*#*):</h2>
        <p>تحظر سامسونج كتابة الكود في لوحة الاتصال، فقام التطبيق باستدعاء شاشة الراديو مباشرة عبر تسلسل الـ Intents التالي في <code>MainActivity.kt</code>:</p>
        <pre>
val targets = listOf(
    Intent().setComponent(ComponentName("com.android.phone", "com.android.phone.settings.RadioInfo")),
    Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.RadioInfo")),
    Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.TestingSettings")),
    Intent(Settings.ACTION_DATA_ROAMING_SETTINGS)
)
        </pre>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الصفحة 4: وضع الطيران والشريحة ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الرابع: الهندسة الدفاعية للشبكة</span>
        </div>

        <h1>4. الهندسة الدفاعية: معالجة وضع الطيران وكشف الشريحة</h1>

        <h2>معالجة وضع الطيران (Airplane Mode Logic):</h2>
        <p>
            في معظم التطبيقات التقليدية، عند تشغيل وضع الطيران تظل بطاقة الـ SIM داخل الدرج، فتقرأ التطبيقات وجود الشريحة وتظهر كذباً أن "الشبكة متصلة". تم حل هذا العيب جذرياً من خلال بنية دفاعية ثلاثية:
        </p>

        <ol>
            <li><b>الفحص المباشر في Kotlin:</b>
                <pre>val isAirplaneMode = Settings.Global.getInt(context.contentResolver, Settings.Global.AIRPLANE_MODE_ON, 0) != 0</pre>
            </li>
            <li><b>التصدير الآمن للبيانات:</b> إرجاع <code>isAirplaneMode = true</code> مع تسمية المشغل بـ "وضع الطيران" ونوع الشبكة بـ "الراديو متوقف".</li>
            <li><b>المنطق الدفاعي في واجهة Flutter:</b>
                <pre>
final isConnected = info != null &&
    info.hasSimCard &&
    !info.isAirplaneMode &&
    info.carrier != 'No Carrier' &&
    info.carrier != 'وضع الطيران';
                </pre>
            </li>
        </ol>

        <div class="card-box">
            <b>سلوك الواجهة الفوري عند تفعيل الطيران:</b>
            <ul>
                <li>تتحول حالة الشبكة العلوية إلى <b>"وضع الطيران (غير متصلة)"</b> باللون البرتقالي التحذيري.</li>
                <li>تنطفئ أعمدة الإشارة السماوية المتوهجة تماماً وتتحول إلى رمادي داكن مطفأ.</li>
                <li>تظهر كبسولة النمط بعبارة <b>"الراديو متوقف"</b>.</li>
            </ul>
        </div>

        <h2>كشف بطاقة الـ SIM واسم المشغل لشبكات CDMA:</h2>
        <ul>
            <li><b>حل مشكلة يمن موبايل:</b> لا تبث شرائح CDMA اسم المشغل النصي عبر الدوال التقليدية؛ لذا تم استخدام <code>SubscriptionManager.getActiveSubscriptionInfoList()</code> مع التحقق من الكود الوطني 421، مما ضمن إظهار <b>Yemen Mobile</b> بدقة.</li>
            <li><b>شارة الشريحة التفاعلية:</b> تظهر شارة خضراء أنيقة بأيقونة الرقاقة الذهبية <b>"الشريحة متصلة"</b> في حال وجودها، وتتحول لشارة حمراء تحذيرية <b>"الشريحة غير متصلة"</b> عند نزعها.</li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الصفحة 5: دليل الأنماط الخمسة ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الخامس: أنماط الشبكة لليمن</span>
        </div>

        <h1>5. جدول الأنماط الخمسة المخصصة لشركات الاتصالات</h1>

        <p>تم تحديد وبرمجة 5 أوضاع رئيسية تغطي كافة الاحتياجات الميدانية لشبكات الاتصالات في اليمن:</p>

        <table>
            <thead>
                <tr>
                    <th style="width: 5%;">#</th>
                    <th style="width: 25%;">اسم النمط بالتطبيق</th>
                    <th style="width: 35%;">الخيار المقابل في المودم (RadioInfo)</th>
                    <th style="width: 35%;">الفائدة التشغيلية وبيئة الاستخدام</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>1</b></td>
                    <td><span class="badge-chip">Yemen Mobile+4G</span></td>
                    <td><code>CDMA+LTE/EVDO (PRL)</code></td>
                    <td>تثبيت ودمج الفورجي مع الثري جي ليمن موبايل لضمان بقاء الإنترنت السريع متاحاً مع استقبال المكالمات.</td>
                </tr>
                <tr>
                    <td><b>2</b></td>
                    <td><span class="badge-chip">Yemen Mobile 3G Only</span></td>
                    <td><code>CDMA/EVDO auto (PRL)</code></td>
                    <td>إجبار الهاتف على شبكة 3G فقط؛ خيار مثالي لتوفير استهلاك البطارية أو في القرى والمناطق الريفية.</td>
                </tr>
                <tr>
                    <td><b>3</b></td>
                    <td><span class="badge-chip">sabafon + you</span></td>
                    <td><code>GSM/WCDMA/LTE (PRL)</code></td>
                    <td>مخصص لشرائح سبأفون و يو العاملة بمعايير GSM؛ يدعم التنقل السلس بين 4G و 3G دون انقطاع.</td>
                </tr>
                <tr>
                    <td><b>4</b></td>
                    <td><span class="badge-chip">VoLTE</span></td>
                    <td><code>LTE only</code></td>
                    <td>قفل الهاتف الصارم على 4G فقط؛ يمنع نهائياً النزول لـ 3G وهو الخيار الأفضل أثناء ألعاب الأونلاين والتحميل.</td>
                </tr>
                <tr>
                    <td><b>5</b></td>
                    <td><span class="badge-chip">(Auto)</span></td>
                    <td><code>NR/LTE/CDMA/EvDo/GSM/WCDMA</code></td>
                    <td>الوضع التلقائي العام الشامل؛ يعيد الهاتف للوضع الافتراضي ليتصل بأي شبكة متاحة (5G/4G/3G/2G) تلقائياً.</td>
                </tr>
            </tbody>
        </table>

        <h2>الصلاحيات المعتمدة في ملف <code>AndroidManifest.xml</code>:</h2>
        <ul>
            <li><code>android.permission.READ_PHONE_STATE</code>: لقراءة بارامترات بطاقة SIM وهوية الشبكة.</li>
            <li><code>android.permission.ACCESS_NETWORK_STATE</code>: لمراقبة حالة الاتصال بالإنترنت والبيانات.</li>
            <li><code>android.permission.MODIFY_PHONE_STATE</code>: لدعم أوامر النظام والروت المباشرة.</li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الصفحة 6: دليل الاستخدام مع الصور ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب السادس: واجهة المستخدم ودليل التشغيل</span>
        </div>

        <h1>6. تشريح واجهة المستخدم ودليل الاستخدام العملي</h1>

        <div class="images-grid">
            <div class="screen-container">
                <img class="screen-img" src="data:image/png;base64,{app_screen_b64}" alt="شاشة التطبيق الرئيسية">
                <div class="screen-caption">الشكل (1): واجهة تطبيق NET Mode الرئيسية</div>
            </div>
            <div class="screen-container">
                <img class="screen-img" src="data:image/png;base64,{device_screen_b64}" alt="شاشة Phone info">
                <div class="screen-caption">الشكل (2): شاشة المودم الأصلية Phone Info</div>
            </div>
        </div>

        <h2>خطوات الاستخدام الميداني خطوة بخطوة:</h2>
        <ol>
            <li><b>فتح التطبيق ومراقبة التغطية:</b> بمجرد تشغيل التطبيق، تُظهر البطاقة العلوية اسم المشغل (Yemen Mobile)، نوع الشبكة الفعلي (4G LTE)، حالة الشريحة المتصلة، وتوهج أعمدة الإشارة الزرقاء (الشكل 1).</li>
            <li><b>اختيار النمط المطلوب:</b> يضغط المستخدم على النمط المراد تفعيله من القائمة الخمسة (مثل <b>Yemen Mobile+4G</b>).</li>
            <li><b>الانتقال لشاشة المودم:</b> يفتح التطبيق تلقائياً شاشة <b>Phone info</b> الأصلية (الشكل 2) دون الحاجة لكتابة كود الاتصال، مع إظهار إشعار سفلي يرشد المستخدم للاسم التقني.</li>
            <li><b>التثبيت من قائمة المودم:</b> ينزل المستخدم إلى خيار <b>Set Preferred Network Type</b> ويختار الخيار المقابل (مثل <code>CDMA+LTE/EVDO (PRL)</code>).</li>
            <li><b>التحديث التلقائي:</b> عند العودة للتطبيق، يقوم مراقب دورة الحياة بتحديث الواجهة فوراً لتعكس النمط الجديد المثبت.</li>
        </ol>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الصفحة 7: الخاتمة والتوصيات ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب السابع: الخاتمة والتوصيات</span>
        </div>

        <h1>7. الخاتمة والتوصيات الهندسية</h1>

        <p>
            يمثل مشروع <b>NET Mode</b> حلاً تقنياً متكاملاً يتغلب على تحديات تذبذب الاتصال الخلوي في البيئة اليمنية، ويجمع بين أحدث معايير هندسة البرمجيات والتكامل المباشر مع طبقة العتاد لنظام أندرويد.
        </p>

        <h2>أهم النتائج المحققة في المشروع:</h2>
        <div class="card-box">
            <ul>
                <li><b>تطبيق معمارية برمجية قياسية:</b> بناء المشروع وفق مبادئ Clean Architecture و SOLID مع فصل كامل لطبقة النطاق (Pure Dart).</li>
                <li><b>حل جذري لمعضلة مشغلي اليمن:</b> دعم كامل لشرائح CDMA و GSM وإظهار اسم يمن موبايل بدقة.</li>
                <li><b>تجاوز حظر الأكواد السرية:</b> استدعاء شاشة Phone Info مباشرة عبر الـ Intents متجاوزاً حجب كود <code>*#*#4636#*#*</code> في هواتف سامسونج.</li>
                <li><b>هندسة دفاعية متقدمة:</b> معالجة دقيقة لوضع الطيران واكتشاف بطاقة الـ SIM لمنع التقارير الخاطئة.</li>
                <li><b>موثوقية وجودة برمجية:</b> اجتياز كافة اختبارات الوحدات (Unit Tests) واختبارات الواجهة (Widget Tests) بنسبة نجاح 100% وبدون أي تحذيرات في التحليل الساكن.</li>
            </ul>
        </div>

        <h2>التوصيات الهندسية للتطوير المستقبلي:</h2>
        <ul>
            <li><b>دعم ترددات الجيل الخامس (5G Standalone):</b> توسيع الأنماط لتشمل تكوينات 5G المخصصة فور إطلاقها في اليمن.</li>
            <li><b>أداة الشاشة الرئيسية (Home Screen Widget):</b> تطوير ويدجت سريع يتيح للمستخدم التبديل السريع دون فتح التطبيق.</li>
            <li><b>سجل جودة الإشارة (Signal Analytics):</b> إضافة ميزة رسم بياني يرصد استقرار الإشارة بوحدة (dBm) ومواقع الأبراج.</li>
        </ul>

        <div style="margin-top: 40px; text-align: center; border-top: 1px solid #e2e8f0; padding-top: 20px;">
            <p style="font-size: 11pt; font-weight: 700; color: #0369a1;">تم بحمد الله وتوفيقه</p>
            <p style="font-size: 10pt; color: #64748b;">إعداد الطالب: أحمد ياسين العماري — إشراف الدكتور: سليمان الشوصي</p>
        </div>
    </div>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML generated successfully at:", html_path)

# تحويل الـ HTML إلى PDF عبر محرك Microsoft Edge بدون واجهة (Headless)
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_exe,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={pdf_path}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_path):
    print("PDF generated successfully at:", pdf_path)
    print("Size in bytes:", os.path.getsize(pdf_path))
else:
    print("PDF generation failed:", res.stderr)
