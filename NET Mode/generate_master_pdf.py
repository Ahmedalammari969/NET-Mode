# -*- coding: utf-8 -*-
import os
import base64
import subprocess

workspace_dir = r"D:\FOR\A\eng\NET Mode\NET Mode"
html_path = os.path.join(workspace_dir, "report_master.html")
pdf_path = os.path.join(workspace_dir, "NET_Mode_Master_Report.pdf")
final_pdf_path = os.path.join(workspace_dir, "NET_Mode_Final_Report.pdf")

app_screen_path = os.path.join(workspace_dir, "img", "app_screen.png")
device_screen_path = os.path.join(workspace_dir, "img", "device_screen.png")
screen_airplane_path = os.path.join(workspace_dir, "img", "screen_airplane.png")

with open(app_screen_path, "rb") as f:
    app_screen_b64 = base64.b64encode(f.read()).decode("utf-8")

with open(device_screen_path, "rb") as f:
    device_screen_b64 = base64.b64encode(f.read()).decode("utf-8")

with open(screen_airplane_path, "rb") as f:
    airplane_screen_b64 = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>الموسوعة الهندسية الشاملة - مشروع NET Mode</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&family=Cairo:wght@400;600;700;800;900&display=swap');
        
        @page {{
            size: A4;
            margin: 16mm 14mm 16mm 14mm;
            @bottom-right {{
                content: "صفحة " counter(page);
                font-family: 'Tajawal', sans-serif;
                font-size: 9pt;
                color: #64748b;
            }}
            @bottom-left {{
                content: "NET Mode — هندسة البرمجيات | إشراف د.م. ساهر الهمداني";
                font-family: 'Tajawal', sans-serif;
                font-size: 8.5pt;
                color: #94a3b8;
            }}
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Tajawal', 'Cairo', 'Segoe UI', Tahoma, sans-serif;
            background-color: #ffffff;
            color: #0f172a;
            line-height: 1.75;
            font-size: 10.5pt;
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
            padding: 35px 20px;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0369a1 100%);
            color: #ffffff;
            border-radius: 14px;
        }}

        .cover-header {{
            margin-top: 30px;
        }}

        .badge-tag {{
            display: inline-block;
            background: rgba(56, 189, 248, 0.2);
            color: #38bdf8;
            border: 1px solid #38bdf8;
            padding: 6px 18px;
            border-radius: 20px;
            font-size: 11pt;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 18px;
        }}

        .cover-title {{
            font-size: 34pt;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 8px;
            letter-spacing: 1px;
            font-family: 'Cairo', sans-serif;
        }}

        .cover-subtitle {{
            font-size: 18pt;
            font-weight: 700;
            color: #38bdf8;
            margin-bottom: 16px;
        }}

        .cover-desc {{
            font-size: 12pt;
            color: #cbd5e1;
            max-width: 650px;
            line-height: 1.75;
        }}

        .cover-tech {{
            display: flex;
            gap: 16px;
            justify-content: center;
            margin-top: 24px;
            flex-wrap: wrap;
        }}

        .tech-box {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 8px 18px;
            border-radius: 10px;
            font-size: 10.5pt;
            font-weight: 600;
            color: #f8fafc;
        }}

        .cover-footer {{
            width: 100%;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            background: rgba(0, 0, 0, 0.35);
            padding: 18px;
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 15px;
        }}

        .meta-card {{
            text-align: center;
        }}

        .meta-label {{
            font-size: 9pt;
            color: #94a3b8;
            margin-bottom: 4px;
        }}

        .meta-val {{
            font-size: 12pt;
            font-weight: 800;
            color: #ffffff;
        }}

        .meta-role {{
            font-size: 8.5pt;
            color: #38bdf8;
            margin-top: 2px;
        }}

        .supervisor-banner {{
            width: 100%;
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.4);
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 12px;
            font-size: 11pt;
            font-weight: 700;
            color: #ffffff;
        }}

        /* Content Pages */
        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 6px;
            margin-bottom: 20px;
            font-size: 8.5pt;
            color: #64748b;
        }}

        h1 {{
            font-size: 17pt;
            font-weight: 800;
            color: #0369a1;
            margin-bottom: 14px;
            border-right: 5px solid #0284c7;
            padding-right: 10px;
            font-family: 'Cairo', sans-serif;
        }}

        h2 {{
            font-size: 13pt;
            font-weight: 700;
            color: #1e293b;
            margin-top: 18px;
            margin-bottom: 10px;
            font-family: 'Cairo', sans-serif;
        }}

        h3 {{
            font-size: 11pt;
            font-weight: 700;
            color: #0284c7;
            margin-top: 14px;
            margin-bottom: 6px;
        }}

        p {{
            margin-bottom: 10px;
            text-align: justify;
            color: #334155;
            font-size: 10pt;
        }}

        .card-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-right: 4px solid #0284c7;
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 14px;
            font-size: 10pt;
        }}

        .card-box-accent {{
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-right: 4px solid #16a34a;
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 14px;
            font-size: 10pt;
        }}

        .alert-box {{
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            border-right: 4px solid #2563eb;
            padding: 10px 14px;
            border-radius: 8px;
            margin-bottom: 14px;
            font-size: 9.5pt;
            color: #1e40af;
        }}

        .warning-box {{
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-right: 4px solid #d97706;
            padding: 10px 14px;
            border-radius: 8px;
            margin-bottom: 14px;
            font-size: 9.5pt;
            color: #92400e;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 14px 0;
            font-size: 9pt;
        }}

        th {{
            background-color: #0f172a;
            color: #ffffff;
            font-weight: 700;
            padding: 8px 10px;
            text-align: right;
            border: 1px solid #0f172a;
        }}

        td {{
            padding: 8px 10px;
            border: 1px solid #cbd5e1;
            color: #1e293b;
        }}

        tr:nth-child(even) {{
            background-color: #f8fafc;
        }}

        .badge-chip {{
            display: inline-block;
            background: #e0f2fe;
            color: #0369a1;
            padding: 2px 7px;
            border-radius: 4px;
            font-family: monospace;
            font-weight: 700;
            font-size: 8.5pt;
        }}

        .badge-green {{
            display: inline-block;
            background: #dcfce7;
            color: #15803d;
            padding: 2px 7px;
            border-radius: 4px;
            font-family: monospace;
            font-weight: 700;
            font-size: 8.5pt;
        }}

        .badge-purple {{
            display: inline-block;
            background: #f3e8ff;
            color: #7e22ce;
            padding: 2px 7px;
            border-radius: 4px;
            font-family: monospace;
            font-weight: 700;
            font-size: 8.5pt;
        }}

        code {{
            background: #f1f5f9;
            color: #0f172a;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: Consolas, monospace;
            font-size: 8.5pt;
            border: 1px solid #e2e8f0;
        }}

        pre {{
            background: #0f172a;
            color: #e2e8f0;
            padding: 12px;
            border-radius: 8px;
            font-family: Consolas, monospace;
            font-size: 8pt;
            overflow-x: auto;
            margin: 10px 0;
            direction: ltr;
            text-align: left;
            line-height: 1.45;
        }}

        .images-grid-three {{
            display: flex;
            justify-content: space-between;
            gap: 12px;
            margin: 16px 0;
        }}

        .screen-container {{
            flex: 1;
            text-align: center;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 8px;
        }}

        .screen-img {{
            max-height: 380px;
            width: auto;
            border-radius: 6px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            border: 2px solid #0f172a;
        }}

        .screen-caption {{
            font-size: 8.5pt;
            font-weight: 700;
            color: #0369a1;
            margin-top: 8px;
        }}
        
        ul, ol {{
            margin-right: 22px;
            margin-bottom: 12px;
            font-size: 9.5pt;
        }}

        li {{
            margin-bottom: 5px;
            color: #334155;
        }}

        .grid-two {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 12px;
        }}

        .engineer-card {{
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 10px 14px;
            background: #f8fafc;
            margin-bottom: 12px;
        }}

        .engineer-title {{
            font-weight: 800;
            font-size: 11pt;
            color: #0284c7;
            margin-bottom: 4px;
        }}

        .engineer-sub {{
            font-size: 8.5pt;
            color: #64748b;
            margin-bottom: 8px;
        }}

        .issue-item {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-right: 3px solid #0284c7;
            padding: 6px 10px;
            border-radius: 4px;
            margin-bottom: 6px;
            font-size: 8.5pt;
        }}
    </style>
</head>
<body>

    <!-- ══════════ الغلاف (Cover Page) ══════════ -->
    <div class="cover-page page-break">
        <div class="cover-header">
            <div class="badge-tag">مشروع تخرج / تقرير هندسة البرمجيات المحكّم</div>
            <div class="cover-title">NET Mode</div>
            <div class="cover-subtitle">Advanced Cellular Network & Radio Testing Suite</div>
            <div class="cover-desc">
                منظومة برمجية متقدمة لإدارة وتثبيت أنماط شبكات الهاتف الخلوي في اليمن وفق معمارية Clean Architecture ومبادئ SOLID، مع الربط الذاتي بالذكاء الاصطناعي عبر بروتوكول MCP وحوكمة مهام Trello.
            </div>
            <div class="cover-tech">
                <div class="tech-box">Flutter Framework</div>
                <div class="tech-box">Kotlin Native</div>
                <div class="tech-box">Clean Architecture</div>
                <div class="tech-box">Model Context Protocol (MCP)</div>
                <div class="tech-box">Agile / Kanban Trello</div>
            </div>
        </div>

        <div style="width: 100%;">
            <div class="supervisor-banner">
                تحت إشراف الأستاذ الدكتور: د.م. ساهر الهمداني
            </div>

            <div class="cover-footer">
                <div class="meta-card">
                    <div class="meta-label">مهندس المنصة والعتاد (Lead)</div>
                    <div class="meta-val">أحمد العماري</div>
                    <div class="meta-role">Native Android & Hardware</div>
                </div>
                <div class="meta-card">
                    <div class="meta-label">مهندس المعمارية والنطاق</div>
                    <div class="meta-val">محمد الدعيس</div>
                    <div class="meta-role">Core Domain Architect</div>
                </div>
                <div class="meta-card">
                    <div class="meta-label">مهندس البيانات والتخزين</div>
                    <div class="meta-val">يوسف خيري</div>
                    <div class="meta-role">Data Layer & Security</div>
                </div>
                <div class="meta-card">
                    <div class="meta-label">مهندس الواجهات وتجربة المستخدم</div>
                    <div class="meta-val">مؤيد الصوفي</div>
                    <div class="meta-role">UI/UX & Presentation State</div>
                </div>
            </div>
        </div>
    </div>

    <!-- ══════════ الباب 1: سريان العمل الهندسي ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الأول: خطة وسريان العمل الهندسي</span>
        </div>

        <h1>1. خطة وسريان العمل الهندسي الشامل (Master Workflow Pipeline)</h1>
        
        <p>
            لتطبيق أرقى المعايير الهندسية المعتمدة في كبرى شركات التقنية العالمية (مثل Google و Microsoft)، تم تنظيم دورة حياة تطوير المشروع (SDLC) في <b>مسار عمل تتابعي متكامل (End-to-End Engineering Pipeline)</b> يربط كل مرحلة برمجية بسابقتها وفق المنهجية الرشيقة (Agile Scrum / Kanban):
        </p>

        <div class="alert-box">
            <b>مبدأ الربط الهندسي الصارم:</b> كل ميزة في التطبيق تنطلق من ميثاق حوكمة (GEMINI.md) ➔ تُوثق في متطلب رسمي (SRS) ➔ تُفصل كقصة مستخدم (US) ➔ تُدار في بطاقة كانبان (Trello) مع شروط إنجاز (DoD) ➔ تُبرمج في فرع منفصل (Git Feature Branch) ➔ تُختبر آلياً وتُدمج بعد مراجعة الكود.
        </div>

        <h2>المخطط التتابعي لسير العمل (Engineering Pipeline Diagram):</h2>
        <pre>
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
        </pre>

        <h2>المبادئ الهندسية الأربعة الحاكمة للمشروع:</h2>
        <ul>
            <li><b>1. لا كود بدون متطلب (No Code without Requirement):</b> لا يتم كتابة أي كود قبل توثيقه في SRS و User Story.</li>
            <li><b>2. نقاء النطاق البرمجي (Domain Purity):</b> منطق أعمال المودم معزول كلياً عن أطر العمل لضمان صيانته واستقراره.</li>
            <li><b>3. معايير الإنجاز الصارمة (Definition of Done - DoD):</b> لا تنتقل البطاقة لـ Done إلا بعد تغليف الأخطاء واجتياز الفحص.</li>
            <li><b>4. حوكمة فروع Git (Branch Governance):</b> حظر التعديل المباشر على <code>main</code> واعتماد الـ Pull Request وموافقة القائد.</li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 2: بروتوكول MCP وحوكمة الذكاء الاصطناعي ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الثاني: بروتوكول MCP وحوكمة الذكاء الاصطناعي</span>
        </div>

        <h1>2. بروتوكول الربط الذاتي المتقدم (MCP) ودستور الحوكمة (`GEMINI.md`)</h1>

        <p>
            في المشاريع البرمجية العالمية لا يُترك الذكاء الاصطناعي كأداة كتابة نصوص عادية، بل يتم دمجه عبر بروتوكول <b>Model Context Protocol (MCP)</b> وتأطيره بدستور هندسي صارم.
        </p>

        <h2>2.1 ميثاق ودستور المشروع المعماري (`GEMINI.md`):</h2>
        <div class="card-box">
            تم إنشاء ملف <code>GEMINI.md</code> كدستور إلزامي للوكيل الذكي وللفريق، ينص على القواعد الخمس التالية:
            <ol>
                <li><b>Domain Layer Purity:</b> حظر استيراد أي مكتبة تتبع Flutter UI أو حزم أندرويد داخل <code>lib/domain/</code> (Strictly Zero Flutter/Android imports).</li>
                <li><b>Data Layer Isolation:</b> عزل قنوات الاتصال بالمنصة عبر أنماط DAO و Repository Pattern.</li>
                <li><b>Presentation Layer:</b> بناء واجهة تفاعلية حديثة تطبق معايير UI/UX Pro Max وإدارة حالة واضحة.</li>
                <li><b>Agent Directives:</b> إلزام الوكيل بالرجوع لقواعد المهارات المعتمدة في <code>.agents/skills/</code> قبل اتخاذ أي قرار.</li>
                <li><b>Defensive Design:</b> المعالجة الاستباقية لرفض الصلاحيات، ووضع الطيران، واختلاف مودمات الشركات المصنعة.</li>
            </ol>
        </div>

        <h2>2.2 بروتوكول الربط الذاتي (Model Context Protocol - MCP):</h2>
        <p>
            بروتوكول <b>MCP</b> هو معيار قياسي عالمي مفتوح يتيح للوكيل الذكي الاتصال المباشر والحي بأدوات التطوير وبيئة النظام ومستودع الكود. تم في المشروع ربط سيرفرين رئيسيين:
        </p>

        <div class="grid-two">
            <div class="card-box-accent">
                <h3>سيرفر أدوات دارت وفلاتر (dart-mcp-server)</h3>
                <ul>
                    <li><b>التحليل الساكن التلقائي (Static Analysis):</b> فحص كود Dart ومطابقته لمعايير Clean Architecture حتى الوصول إلى <code>No issues found!</code>.</li>
                    <li><b>فحص شجرة الويدجت (Widget Tree):</b> فحص تسلسل العناصر والتأكد من خلوها من أخطاء الـ Overflow.</li>
                    <li><b>محرك الاختبارات الآلي (Test Runner):</b> تنفيذ اختبارات الـ Unit والـ Widget المؤتمتة (11/11 Passed).</li>
                    <li><b>تشخيص وقت التشغيل (Runtime Diagnostics):</b> فحص استدعاءات <code>MethodChannel</code> ومنع تسريب الذاكرة.</li>
                </ul>
            </div>

            <div class="card-box">
                <h3>سيرفر منصة جيت هب (github-mcp-server)</h3>
                <ul>
                    <li><b>إدارة حوكمة الفروع (Branch Governance):</b> فحص الفروع المرفوعة ومطابقتها لمهام كانبان وتريلو.</li>
                    <li><b>مزامنة تاريخ الـ Commits:</b> التأكد من تطابق سجل التغييرات مع صيغة الـ Conventional Commits.</li>
                    <li><b>تأسيس حماية الفرع الرئيسي:</b> فحص التوافق وتجهيز مسار الدمج عبر Pull Requests لمنع التعديل المباشر على <code>main</code>.</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 3: مواصفات المتطلبات والحدود ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الثالث: وثيقة المتطلبات وحدود النظام</span>
        </div>

        <h1>3. مواصفات متطلبات البرمجيات (SRS - IEEE Std 830-1998) والحدود والنطاق</h1>

        <h2>3.1 حدود ونطاق العمل الهندسي (Scope & System Boundaries):</h2>
        <p>
            تحديد حواف ونطاق النظام بدقة يمنع التشتت البرمجي ويحدد بدقة ما يقع داخل مسؤولية النظام (In-Scope) وما يقع خارجه (Out-of-Scope):
        </p>

        <table>
            <thead>
                <tr>
                    <th style="width: 50%;">داخل نطاق العمل (In-Scope)</th>
                    <th style="width: 50%;">خارج نطاق العمل (Out-of-Scope)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>• قراءة تيليمتري المودم الحقيقي (4G LTE, 3G EVDO, HSPA, 5G NR).</td>
                    <td>• كسر حماية النظام الإجباري (Root) للأجهزة المقفلة عتادياً من المصنع.</td>
                </tr>
                <tr>
                    <td>• تجاوز حظر كود <code>*#*#4636#*#*</code> واستدعاء شاشات الراديو السرية.</td>
                    <td>• دعم بيئة أنظمة iOS نظراً لإغلاق شركة Apple لمودم الراديو تماماً.</td>
                </tr>
                <tr>
                    <td>• التثبيت على الأنماط الخمسة المخصصة لشركات الاتصالات باليمن.</td>
                    <td>• الاتصال بخوادم وسيطة خارجية (التطبيق يعمل محلياً Offline بنسبة 100%).</td>
                </tr>
                <tr>
                    <td>• رصد وضع الطيران بدقة ومنع الإبلاغ الكاذب عن الاتصال.</td>
                    <td>• تعديل أرقام الـ IMEI أو إجراء تعديلات غير قانونية على المودم الخلوي.</td>
                </tr>
                <tr>
                    <td>• كشف جاهزية وحالة بطاقة الـ SIM والتخزين المحلي للتفضيلات.</td>
                    <td>• التدخل في فوترة المكالمات أو شحن الرصيد لشركات الاتصالات.</td>
                </tr>
            </tbody>
        </table>

        <h2>3.2 المتطلبات الوظيفية الرئيسية (Functional Requirements - FRs):</h2>
        <div class="card-box">
            <ul>
                <li><b>FR-01:</b> فحص واكتشاف مشغل الخدمة الحقيقي ونوع الشبكة اللحظية بدقة.</li>
                <li><b>FR-02:</b> توفير اختصارات مباشرة لفتح شاشات هندسة الراديو (Hidden RadioInfo) تتخطى حظر لوحة الاتصال.</li>
                <li><b>FR-03:</b> إتاحة تثبيت ترددات الفورجي (LTE Only) والأوضاع الهجينة لشركات الاتصالات باليمن.</li>
                <li><b>FR-04:</b> الكشف الدقيق عن حالة بطاقة SIM والتفرقة بين الشريحة المتصلة والمفقودة.</li>
                <li><b>FR-05:</b> الكشف الفوري عن وضع الطيران وإطفاء مؤشرات البث لمنع التقارير الكاذبة.</li>
                <li><b>FR-06:</b> اعتراض استثناءات النظام الأمنية (Knox Security Policies) ومعالجتها بأمان.</li>
                <li><b>FR-07:</b> تخزين الأنماط المفضلة محلياً دون أي خوادم خارجية (Offline-First).</li>
                <li><b>FR-08:</b> توفير واجهة مستخدم تفاعلية بنمط داكن (Cyberpunk Navy) مع عداد إشارة مكون من 5 أعمدة مضيئة.</li>
            </ul>
        </div>

        <h2>3.3 المتطلبات غير الوظيفية (Non-Functional Requirements - NFRs):</h2>
        <ul>
            <li><b>الأداء (Performance):</b> استخراج تيليمتري الشبكة وتحديث الواجهة في زمن استجابة أقل من <b>200 ملي ثانية</b>.</li>
            <li><b>كفاءة الطاقة (Power Efficiency):</b> استهلاك طاقة البطارية أقل من <b>1% في الساعة</b> عبر الاعتماد على التحديث الحدثي اللحظي.</li>
            <li><b>الموثوقية (Reliability & Zero-Crash):</b> تغليف كافة الـ Intents بكتل <code>try-catch</code> تضمن عدم انهيار التطبيق تحت أي ظرف.</li>
            <li><b>الأمان والخصوصية (Security & Privacy):</b> التطبيق محلي 100%، خالي من أي أدوات تتبع أو مشاركة للبيانات مع خوادم طرف ثالث.</li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 4: قصص المستخدمين الـ 24 ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الرابع: مصفوفة قصص المستخدمين</span>
        </div>

        <h1>4. مصفوفة قصص المستخدمين الـ 24 (Agile User Stories)</h1>

        <p>تم تحويل متطلبات الـ SRS إلى 24 قصة مستخدم بصيغة معايير القبول الهندسية (Given - When - Then):</p>

        <table>
            <thead>
                <tr>
                    <th style="width: 10%;">القصة</th>
                    <th style="width: 30%;">العنوان والهدف</th>
                    <th style="width: 60%;">معيار القبول الهندسي (Acceptance Criteria)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>US-01</b></td>
                    <td>تشغيل نية راديو سامسونج</td>
                    <td><b>Given</b> هاتف سامسونج One UI، <b>When</b> طلب فتح الراديو، <b>Then</b> تشغيل <code>RadioInfo</code> بنجاح.</td>
                </tr>
                <tr>
                    <td><b>US-02</b></td>
                    <td>سلسلة بدائل شاومي والأندرويد الخام</td>
                    <td><b>Given</b> تعذر مسار سامسونج، <b>When</b> استدعاء البديل، <b>Then</b> فتح <code>TestingSettings</code> بنجاح.</td>
                </tr>
                <tr>
                    <td><b>US-03</b></td>
                    <td>فك تشفير مسميات المودم</td>
                    <td><b>Given</b> كود RIL رقمي، <b>When</b> قراءته، <b>Then</b> ترجمته لمسمى صريح مثل (4G LTE / 5G NR).</td>
                </tr>
                <tr>
                    <td><b>US-04</b></td>
                    <td>جسر قنوات المنصة</td>
                    <td><b>Given</b> بيانات المودم، <b>When</b> نقلها، <b>Then</b> عبورها عبر <code>MethodChannel</code> بدون تسريب ذاكرة.</td>
                </tr>
                <tr>
                    <td><b>US-05</b></td>
                    <td>فحص الشريحة والطيران</td>
                    <td><b>Given</b> تفعيل الطيران، <b>When</b> فحص الحالة، <b>Then</b> إرجاع <code>isAirplaneMode = true</code> فورياً.</td>
                </tr>
                <tr>
                    <td><b>US-06</b></td>
                    <td>اعتراض أخطاء التحصين الأمني</td>
                    <td><b>Given</b> رفض إذن <code>MODIFY_PHONE_STATE</code>، <b>When</b> محاولة التغيير، <b>Then</b> اصطياد الاستثناء بأمان.</td>
                </tr>
                <tr>
                    <td><b>US-07</b></td>
                    <td>كيان NetworkInfo النقي</td>
                    <td><b>Given</b> تيليمتري الشبكة، <b>When</b> إنشاؤه، <b>Then</b> تكوين كائن Dart نقي غير قابل للتعديل (Immutable).</td>
                </tr>
                <tr>
                    <td><b>US-08</b></td>
                    <td>كيان NetworkMode وأنماط اليمن</td>
                    <td><b>Given</b> نمط شبكة، <b>When</b> تعريفه، <b>Then</b> ربطه بكود RIL المعياري ووصف المودم.</td>
                </tr>
                <tr>
                    <td><b>US-09</b></td>
                    <td>عقد مستودع الشبكة المجرد</td>
                    <td><b>Given</b> معمارية نظيفة، <b>When</b> صياغة العقد، <b>Then</b> تجريده كـ Interface بدون أي مكتبات UI.</td>
                </tr>
                <tr>
                    <td><b>US-10</b></td>
                    <td>حالة استخدام لقطة الشبكة اللحظية</td>
                    <td><b>Given</b> طلب تحديث، <b>When</b> استدعاء UseCase، <b>Then</b> إرجاع <code>NetworkInfo</code> نقي بدون تجميد.</td>
                </tr>
                <tr>
                    <td><b>US-11</b></td>
                    <td>حالة استخدام فتح شاشات الراديو</td>
                    <td><b>Given</b> ضغط زر الضبط، <b>When</b> التنفيذ، <b>Then</b> إطلاق النية المناسبة بأمان عبر الـ Fallback.</td>
                </tr>
                <tr>
                    <td><b>US-12</b></td>
                    <td>حزمة اختبارات النطاق الآلية</td>
                    <td><b>Given</b> بيئة الاختبارات، <b>When</b> تشغيل <code>flutter test</code>، <b>Then</b> اجتياز 100% من الاختبارات بنجاح.</td>
                </tr>
                <tr>
                    <td><b>US-13</b></td>
                    <td>تنفيذ مصدر بيانات الراديو</td>
                    <td><b>Given</b> منصة أندرويد، <b>When</b> استدعاء القناة، <b>Then</b> معالجة <code>PlatformException</code> بأمان.</td>
                </tr>
                <tr>
                    <td><b>US-14</b></td>
                    <td>تنفيذ مستودع البيانات الحقيقي</td>
                    <td><b>Given</b> بيانات خام HashMap، <b>When</b> استقبالها، <b>Then</b> تحويلها لكائنات Domain نقية.</td>
                </tr>
                <tr>
                    <td><b>US-15</b></td>
                    <td>التخزين الدائم للنمط المفضل</td>
                    <td><b>Given</b> اختيار المستخدم لنمط، <b>When</b> الحفظ، <b>Then</b> استرجاعه تلقائياً عند إعادة فتح التطبيق.</td>
                </tr>
                <tr>
                    <td><b>US-16</b></td>
                    <td>إدارة أذونات حالة الهاتف</td>
                    <td><b>Given</b> طلب إذن <code>READ_PHONE_STATE</code>، <b>When</b> المنح أو الرفض، <b>Then</b> التعامل بمرونة بدون كراش.</td>
                </tr>
                <tr>
                    <td><b>US-17</b></td>
                    <td>معمارية توحيد الأخطاء والفشل</td>
                    <td><b>Given</b> حدوث خطأ، <b>When</b> معالجته، <b>Then</b> ترجمته لـ <code>PlatformFailure</code> دون إيقاف التطبيق.</td>
                </tr>
                <tr>
                    <td><b>US-18</b></td>
                    <td>إقرار أمان البيانات وسياسة الخصوصية</td>
                    <td><b>Given</b> متطلبات المتجر، <b>When</b> التوثيق، <b>Then</b> إثبات أن كافة المعالجات تتم محلياً فقط.</td>
                </tr>
                <tr>
                    <td><b>US-19</b></td>
                    <td>نظام الثيم الداكن المتقدم</td>
                    <td><b>Given</b> شاشات AMOLED، <b>When</b> فتح التطبيق، <b>Then</b> عرض ألوان Cyberpunk مريحة للعين وتوفر الطاقة.</td>
                </tr>
                <tr>
                    <td><b>US-20</b></td>
                    <td>بطاقة حالة التغطية وأعمدة الإشارة</td>
                    <td><b>Given</b> إشارة الشبكة، <b>When</b> البث، <b>Then</b> إضاءة 5 أعمدة نيون تنطفئ في وضع الطيران.</td>
                </tr>
                <tr>
                    <td><b>US-21</b></td>
                    <td>الزر البارز لضبط المودم</td>
                    <td><b>Given</b> شاشة التطبيق، <b>When</b> الضغط، <b>Then</b> تفاعل نقر غير متزامن مع إطار نيون بارز.</td>
                </tr>
                <tr>
                    <td><b>US-22</b></td>
                    <td>التحديث اللحظي عبر دورة الحياة</td>
                    <td><b>Given</b> عودة المستخدم، <b>When</b> تنشيط التطبيق، <b>Then</b> تحديث الواجهة فوراً عبر <code>WidgetsBindingObserver</code>.</td>
                </tr>
                <tr>
                    <td><b>US-23</b></td>
                    <td>محرك الإشعارات التفاعلية</td>
                    <td><b>Given</b> تعذر التحويل الصامت، <b>When</b> الفشل، <b>Then</b> إظهار SnackBar يرشد المستخدم للبديل.</td>
                </tr>
                <tr>
                    <td><b>US-24</b></td>
                    <td>تجاوب الواجهة مع مختلف الشاشات</td>
                    <td><b>Given</b> أجهزة مختلفة، <b>When</b> تدوير الشاشة، <b>Then</b> خلو الواجهة تماماً من أخطاء الـ Overflow.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 5: كانبان وتريلو للمهندسين الأربعة ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الخامس: لوحة كانبان وتوزيع المهام الـ 24</span>
        </div>

        <h1>5. لوحة كانبان وتوزيع المهام الـ 24 تفصيلياً على المهندسين الأربعة</h1>

        <p>
            تم تقسيم الـ 24 مهمة بالتساوي التام على أعضاء الفريق الأربعة في لوحة <b>NET Mode - Agile Board</b>، بحيث يتولى كل مهندس مساراً هندسياً (Epic) يشتمل على 6 مهام كاملة مع ملفاتها وفروعها وشروط إنجازها (DoD):
        </p>

        <!-- المهندس الأول: أحمد العماري -->
        <div class="engineer-card">
            <div class="engineer-title">1. المهندس أحمد ياسين العماري — مهندس المنصة والعتاد (Lead)</div>
            <div class="engineer-sub">المسار الهندسي (Epic 1): Native Platform & Radio RIL | الوسم في Trello: <code>native-android</code>, <code>hardware-ril</code></div>
            
            <div class="issue-item">
                <b>Issue #1 (US-01): Samsung Radio Intent Launcher</b><br>
                • الوصف: بناء نية صريحة لاستهداف <code>com.android.phone.settings.RadioInfo</code> لأجهزة سامسونج One UI.<br>
                • الملفات: <code>android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt</code> | الفرع: <code>feature/issue-1-samsung-radio-intent</code>
            </div>
            <div class="issue-item">
                <b>Issue #2 (US-02): Xiaomi & AOSP Fallback Intent Chain</b><br>
                • الوصف: بناء سلسلة البدائل لاستدعاء <code>RadioInfo</code> في شاومي وبديل <code>TestingSettings</code> لأندرويد الخام.<br>
                • الملفات: <code>android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt</code> | الفرع: <code>feature/issue-2-xiaomi-aosp-fallback</code>
            </div>
            <div class="issue-item">
                <b>Issue #3 (US-03): Telephony RIL Modem Network Decoder</b><br>
                • الوصف: فك تشفير وتصنيف أكواد المودم الخلوية من <code>TelephonyManager</code> إلى (4G LTE, 5G NR, 3G EVDO).<br>
                • الملفات: <code>android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt</code> | الفرع: <code>feature/issue-3-ril-telephony-decoder</code>
            </div>
            <div class="issue-item">
                <b>Issue #4 (US-04): Native MethodChannel Bridge Architecture</b><br>
                • الوصف: تأسيس القناة الموحدة <code>com.netmode.app/radio</code> ونقل البيانات دون أي تسريب ذاكرة.<br>
                • الملفات: <code>android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt</code> | الفرع: <code>feature/issue-4-platform-method-channel</code>
            </div>
            <div class="issue-item">
                <b>Issue #5 (US-05): SIM State & Airplane Mode Native Inspector</b><br>
                • الوصف: فحص مسجلات وضع الطيران <code>AIRPLANE_MODE_ON</code> وحل قراءة اسم يمن موبايل لشبكات CDMA عبر <code>SubscriptionManager</code>.<br>
                • الملفات: <code>android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt</code> | الفرع: <code>feature/issue-5-sim-airplane-inspector</code>
            </div>
            <div class="issue-item">
                <b>Issue #6 (US-06): System Security Lockout & Exception Catching</b><br>
                • الوصف: اعتراض استثناءات Knox و <code>MODIFY_PHONE_STATE</code> وإرجاع استجابات آمنة للواجهة عبر الـ Fallback.<br>
                • الملفات: <code>android/app/src/main/kotlin/com/example/net_mode/MainActivity.kt</code> | الفرع: <code>feature/issue-6-security-exception-handler</code>
            </div>
        </div>

        <!-- المهندس الثاني: محمد الدعيس -->
        <div class="engineer-card">
            <div class="engineer-title">2. المهندس محمد علي / محمد الدعيس — مهندس المعمارية والنطاق</div>
            <div class="engineer-sub">المسار الهندسي (Epic 2): Clean Architecture & Domain Logic | الوسم في Trello: <code>clean-domain</code>, <code>core-logic</code></div>
            
            <div class="issue-item">
                <b>Issue #7 (US-07): Pure NetworkInfo Entity Definition</b><br>
                • الوصف: بناء كائن Dart نقي غير قابل للتعديل (Immutable) يحمل تيليمتري الشبكة (carrier, networkType, hasSimCard, isAirplaneMode).<br>
                • الملفات: <code>lib/domain/entities/network_info.dart</code> | الفرع: <code>feature/issue-7-network-info-entity</code>
            </div>
            <div class="issue-item">
                <b>Issue #8 (US-08): NetworkMode Presets & RIL Types Entity</b><br>
                • الوصف: تعريف كيان الأنماط الخلوية المخصصة وتصنيفاتها (2G, 3G, 4G, 5G, Auto) وربطها برمز الـ RIL والوصف الفني.<br>
                • الملفات: <code>lib/domain/entities/network_mode.dart</code> | الفرع: <code>feature/issue-8-network-mode-entity</code>
            </div>
            <div class="issue-item">
                <b>Issue #9 (US-09): Abstract NetworkRepository Interface</b><br>
                • الوصف: صياغة عقد المستودع المجرد لعزل طبقة النطاق وتطبيق مبدأ عكس التبعية (Dependency Inversion).<br>
                • الملفات: <code>lib/domain/repositories/network_repository.dart</code> | الفرع: <code>feature/issue-9-network-repository-contract</code>
            </div>
            <div class="issue-item">
                <b>Issue #10 (US-10): Get Instant Network Snapshot UseCase</b><br>
                • الوصف: بناء حالة استخدام مستقلة لجلب بيانات الشبكة اللحظية بنمط دالي نقي وفق مبدأ المسؤولية الواحدة (SRP).<br>
                • الملفات: <code>lib/domain/usecases/network_usecases.dart</code> | الفرع: <code>feature/issue-10-get-snapshot-usecase</code>
            </div>
            <div class="issue-item">
                <b>Issue #11 (US-11): Open Radio Settings Controller UseCase</b><br>
                • الوصف: بناء حالة استخدام مستقلة لعزل طلب فتح شاشات الراديو الأصلية عن الواجهة.<br>
                • الملفات: <code>lib/domain/usecases/network_usecases.dart</code> | الفرع: <code>feature/issue-11-open-radio-usecase</code>
            </div>
            <div class="issue-item">
                <b>Issue #12 (US-12): Domain Unit Testing Suite (100% Pass)</b><br>
                • الوصف: كتابة واجتياز اختبارات الوحدة الآلية الشاملة لطبقة النطاق والتحقق من التغطية والمساواة البنيوية.<br>
                • الملفات: <code>test/domain/usecases/network_usecases_test.dart</code> | الفرع: <code>feature/issue-12-domain-unit-tests</code>
            </div>
        </div>
    </div>

    <div class="page-break"></div>

    <!-- تكملة الباب 5: يوسف خيري ومؤيد الصوفي -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الخامس: لوحة كانبان (تابع: المهندسين 3 و 4)</span>
        </div>

        <!-- المهندس الثالث: يوسف خيري -->
        <div class="engineer-card">
            <div class="engineer-title">3. المهندس يوسف خيري — مهندس طبقة البيانات والتخزين والأمان</div>
            <div class="engineer-sub">المسار الهندسي (Epic 3): Data Layer, Storage & Security | الوسم في Trello: <code>data-layer</code>, <code>storage-security</code></div>
            
            <div class="issue-item">
                <b>Issue #13 (US-13): Radio Device DataSource Implementation</b><br>
                • الوصف: كتابة كلاس استدعاء <code>MethodChannel</code> وتفكيك قواميس البيانات مع معالجة <code>PlatformException</code>.<br>
                • الملفات: <code>lib/data/datasources/radio_device_datasource.dart</code> | الفرع: <code>feature/issue-13-radio-datasource-impl</code>
            </div>
            <div class="issue-item">
                <b>Issue #14 (US-14): Concrete NetworkRepository Implementation</b><br>
                • الوصف: بناء المستودع الحقيقي <code>NetworkRepositoryImpl</code> وتحويل الـ DTOs الخام إلى كيانات النطاق النقية.<br>
                • الملفات: <code>lib/data/repositories/network_repository_impl.dart</code> | الفرع: <code>feature/issue-14-network-repository-impl</code>
            </div>
            <div class="issue-item">
                <b>Issue #15 (US-15): Local Storage & Presets Persistence</b><br>
                • الوصف: إدارة التخزين المحلي لاسترجاع النمط المفضل وسجل التبديل عند إعادة تشغيل التطبيق.<br>
                • الملفات: <code>lib/data/datasources/local_preferences_datasource.dart</code> | الفرع: <code>feature/issue-15-local-storage-datasource</code>
            </div>
            <div class="issue-item">
                <b>Issue #16 (US-16): Telephony Permissions Engine & Manifest Declarations</b><br>
                • الوصف: إعلان وإدارة الصلاحيات في <code>AndroidManifest.xml</code> ومعالجة حالات منح ورفض إذن <code>READ_PHONE_STATE</code>.<br>
                • الملفات: <code>android/app/src/main/AndroidManifest.xml</code> | الفرع: <code>feature/issue-16-phone-state-permissions</code>
            </div>
            <div class="issue-item">
                <b>Issue #17 (US-17): Unified Failures & Exception Architecture</b><br>
                • الوصف: توحيد كلاسات معالجة الأخطاء والفشل (<code>PlatformFailure</code>, <code>PermissionFailure</code>) ومنع كراش التطبيق.<br>
                • الملفات: <code>lib/core/errors/failures.dart</code> | الفرع: <code>feature/issue-17-error-failures-engine</code>
            </div>
            <div class="issue-item">
                <b>Issue #18 (US-18): Google Play Data Safety Compliance Docs</b><br>
                • الوصف: صياغة سياسة الخصوصية وأمان البيانات وإثبات أن معالجة التيليمتري تتم محلياً 100% دون خوادم خارجية.<br>
                • الملفات: <code>docs/PRIVACY_POLICY.md</code> | الفرع: <code>feature/issue-18-play-store-privacy-docs</code>
            </div>
        </div>

        <!-- المهندس الرابع: مؤيد الصوفي -->
        <div class="engineer-card">
            <div class="engineer-title">4. المهندس مؤيد الصوفي — مهندس الواجهات وتجربة المستخدم (UI/UX)</div>
            <div class="engineer-sub">المسار الهندسي (Epic 4): Presentation Layer & UI/UX | الوسم في Trello: <code>ui-ux</code>, <code>presentation-state</code></div>
            
            <div class="issue-item">
                <b>Issue #19 (US-19): Dark Cyberpunk Theme & Design System</b><br>
                • الوصف: بناء الثيم الليلي المتطور (Cyberpunk Dark Navy Palette) ومواءمة التباين لشاشات AMOLED.<br>
                • الملفات: <code>lib/presentation/theme/app_theme.dart</code> (أو <code>lib/main.dart</code>) | الفرع: <code>feature/issue-19-dark-cyberpunk-theme</code>
            </div>
            <div class="issue-item">
                <b>Issue #20 (US-20): Network Status & Tower Visualizer Card</b><br>
                • الوصف: تصميم بطاقة التغطية وبناء عداد الإشارة المكون من 5 أعمدة نيون مضيئة تتفاعل مع حالة البث اللاسلكي.<br>
                • الملفات: <code>lib/presentation/widgets/network_status_card.dart</code> | الفرع: <code>feature/issue-20-network-status-card</code>
            </div>
            <div class="issue-item">
                <b>Issue #21 (US-21): Prominent Radio Action Button</b><br>
                • الوصف: تصميم الزر الرئيسي البارز ذو الإطار النيوني السماوي (Outlined Button) لفتح شاشة المودم بنقر غير متزامن.<br>
                • الملفات: <code>lib/presentation/widgets/radio_action_button.dart</code> | الفرع: <code>feature/issue-21-radio-action-button</code>
            </div>
            <div class="issue-item">
                <b>Issue #22 (US-22): Real-Time Refresh & Polling Trigger</b><br>
                • الوصف: دمج مراقب دورة حياة التطبيق <code>WidgetsBindingObserver</code> مع مؤقت زمني لتحديث الواجهة فور عودة المستخدم.<br>
                • الملفات: <code>lib/presentation/screens/home_screen.dart</code> | الفرع: <code>feature/issue-22-instant-refresh-action</code>
            </div>
            <div class="issue-item">
                <b>Issue #23 (US-23): Contextual Feedback & SnackBar Engine</b><br>
                • الوصف: برمجة الإشعارات العائمة التوجيهية (SnackBars) لإرشاد المستخدم للخيار المطلوب في قائمة المودم.<br>
                • الملفات: <code>lib/presentation/screens/home_screen.dart</code> | الفرع: <code>feature/issue-23-snackbar-feedback</code>
            </div>
            <div class="issue-item">
                <b>Issue #24 (US-24): Responsive Layout & Orientation Adaptability</b><br>
                • الوصف: ضمان تجاوب الواجهة مع مختلف أحجام الشاشات وتدوير الجهاز وخلوها 100% من أخطاء الـ RenderFlex Overflow.<br>
                • الملفات: <code>lib/presentation/screens/home_screen.dart</code> | الفرع: <code>feature/issue-24-responsive-orientation-ui</code>
            </div>
        </div>

        <h2>معايير الإنجاز الصارمة في Trello (Definition of Done - DoD):</h2>
        <div class="card-box">
            تم إلزام الفريق بعدم نقل أي بطاقة في تريلو من <code>In Progress</code> إلى <code>Done</code> إلا بعد استيفاء الشروط الأربعة التالية:
            <ol>
                <li>تغليف الدوال بكتل <code>try / catch</code> شاملة واعتراض استثناءات <code>SecurityException</code>.</li>
                <li>ربط المهمة بفرع Git مخصص يحمل نفس كود المهمة: <code>feature/issue-X-...</code>.</li>
                <li>الالتزام بنمط رسائل الـ Commit المعيارية (Conventional Commits).</li>
                <li>اجتياز اختبارات التحقق الآلي والتحليل الساكن <code>flutter analyze</code> بنتيجة خالية من الأخطاء.</li>
            </ol>
        </div>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 6: المعمارية البرمجية ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب السادس: المعمارية البرمجية وسريان البيانات</span>
        </div>

        <h1>6. المعمارية البرمجية وسريان البيانات (Clean Architecture & SOLID)</h1>

        <p>
            تعتمد المنظومة على معمارية <b>Clean Architecture</b> ومبادئ <b>SOLID</b>، بهدف فصل منطق الأعمال النقي عن واجهات العرض وأكواد النظام الأصلية:
        </p>

        <pre>
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
        </pre>

        <div class="card-box">
            <b>1. طبقة النطاق (Domain Layer - Pure Dart):</b><br>
            خالية 100% من استيراد Flutter أو Android UI. تضم الكيانات غير القابلة للتعديل:
            <ul>
                <li><code>NetworkMode</code>: يحمل معرّف النمط، اسمه الظاهر، كود الـ RIL الداخلي للمودم، وفئة الجيل الخلوي.</li>
                <li><code>NetworkInfo</code>: كائن يحمل تيليمتري الشبكة اللحظية (المشغل، نوع الاتصال، حالة الشريحة، وضع الطيران).</li>
                <li><code>NetworkRepository</code>: العقد المجرد الذي يحدد العمليات دون التدخل في كيفية استخراجها من أندرويد.</li>
                <li><code>Use Cases</code>: تضم حالات الاستخدام المنفصلة (GetSnapshot, SetMode, OpenRadio, ManagePreferred).</li>
            </ul>
        </div>

        <div class="card-box">
            <b>2. طبقة البيانات (Data Layer):</b><br>
            تضم فئة <code>RadioDeviceDataSourceImpl</code> المتصلة عبر القناة <code>com.netmode.app/radio</code>، والمستودع <code>NetworkRepositoryImpl</code> الذي يحول البيانات الخام (HashMaps) إلى كائنات الدومين النقية، ويحفظ التفضيلات محلياً.
        </div>

        <div class="card-box">
            <b>3. طبقة المنصة الأصلية (Kotlin Native):</b><br>
            تتولى التخاطب المباشر مع رقاقة المودم الراديوي ونظام التشغيل عبر <code>TelephonyManager</code> و <code>SubscriptionManager</code>.
        </div>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 7: محرك أندرويد وسامسونج ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب السابع: محرك النظام الأصلي في كوتلن</span>
        </div>

        <h1>7. محرك النظام الأصلي وحلول سامسونج ويمن موبايل (`MainActivity.kt`)</h1>

        <h2>7.1 حل مشكلة شرائح يمن موبايل (CDMA Quirk Fix):</h2>
        <p>
            تعتمد شركة يمن موبايل على بروتوكولات CDMA/EVDO التي لا تبث اسم المشغل النصي عبر الدالة التقليدية <code>tm.networkOperatorName</code>، مما كان يتسبب في ظهور اسم المشغل كـ "No Carrier".
        </p>
        <div class="card-box-accent">
            <b>الحل المبتكر في Kotlin:</b> تم تجاوز الدوال التقليدية والاستعلام المباشر من مدقق الاشتراكات الفعلي <code>SubscriptionManager.getActiveSubscriptionInfoList()</code> مع فحص كود الدولة والشبكة الوطني 421، مما ضمن إظهار <b>Yemen Mobile</b> بدقة استثنائية.
        </div>

        <h2>7.2 مصفوفة النيات التعاقبية لتجاوز حجب كود سامسونج (OEM Fallback Matrix):</h2>
        <p>
            تحظر واجهة سامسونج One UI وشاومي إدخال الرمز السري <code>*#*#4636#*#*</code> في لوحة الاتصال لمنع المستخدمين من تعديل المودم. قام التطبيق باستدعاء نافذة <code>RadioInfo</code> مباشرة عبر تسلسل ذكي من 4 نيات تعاقبية تضمن تشغيلها على أي جهاز:
        </p>

        <pre>
val targets = listOf(
    Intent().setComponent(ComponentName("com.android.phone", "com.android.phone.settings.RadioInfo")),
    Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.RadioInfo")),
    Intent().setComponent(ComponentName("com.android.settings", "com.android.settings.TestingSettings")),
    Intent(Settings.ACTION_DATA_ROAMING_SETTINGS)
)
for (intent in targets) {{
    try {{
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        context.startActivity(intent)
        return true
    }} catch (_: Exception) {{ continue }}
}}
        </pre>

        <h2>7.3 التحليل الأمني وصلاحية `MODIFY_PHONE_STATE` (Hybrid Execution):</h2>
        <ul>
            <li>تمنع أنظمة أندرويد وسامسونج Knox أي تطبيق عادي من تحويل التردد صمتاً في الخلفية بدون روت لأن صلاحية <code>MODIFY_PHONE_STATE</code> محجوزة لتطبيقات النظام داخل <code>/system/priv-app</code>.</li>
            <li><b>استراتيجية التطبيق المزدوجة:</b>
                <br>• <b>في الهواتف المروّتة (Root):</b> ينفذ التطبيق أمر الـ Shell الصامت فوراً: <code>su -c cmd phone set-preferred-network-type [CODE]</code>.
                <br>• <b>في الهواتف العادية:</b> يفتح التطبيق نافذة <code>Phone info</code> الأصلية بضغطة زر واحدة ويوجه المستخدم للاسم المطابق لاختياره.
            </li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 8: الهندسة الدفاعية ووضع الطيران ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الثامن: الهندسة الدفاعية للشبكة</span>
        </div>

        <h1>8. الهندسة الدفاعية: رصد وضع الطيران واكتشاف الشريحة</h1>

        <h2>8.1 حل ثغرة وضع الطيران (Airplane Mode Logic):</h2>
        <p>
            في التطبيقات العادية، عند تشغيل وضع الطيران تظل بطاقة الـ SIM داخل الدرج، فيقرأ الهاتف وجود الشريحة ويُظهر خطأً أن "الشبكة متصلة". تم معالجة هذه الثغرة من خلال بنية دفاعية ثلاثية:
        </p>

        <ol>
            <li><b>الفحص العتادي المباشر في Kotlin:</b>
                <pre>val isAirplaneMode = Settings.Global.getInt(context.contentResolver, Settings.Global.AIRPLANE_MODE_ON, 0) != 0</pre>
            </li>
            <li><b>التصدير الآمن للبيانات:</b> إرجاع <code>isAirplaneMode = true</code> مع تسمية المشغل بـ "وضع الطيران" ونوع الشبكة بـ "الراديو متوقف".</li>
            <li><b>الشرط الدفاعي الصارم في واجهة Flutter:</b>
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
            <b>السلوك المرئي الفوري في الواجهة عند تفعيل الطيران:</b>
            <ul>
                <li>تتحول حالة الشبكة العلوية إلى <b>"وضع الطيران (غير متصلة)"</b> باللون البرتقالي التحذيري.</li>
                <li>تنطفئ أعمدة الإشارة النيون الخمسة تماماً وتتحول إلى رمادي داكن مطفأ بدون أي توهج.</li>
                <li>تظهر كبسولة النمط بعبارة <b>"الراديو متوقف"</b>.</li>
            </ul>
        </div>

        <h2>8.2 المزامنة اللحظية الحية (Live Lifecycle Observer):</h2>
        <p>
            تم دمج فئة <code>WidgetsBindingObserver</code> مع الشاشة الرئيسية: بمجرد أن يعود المستخدم من شاشة المودم أو يسحب شريط الإشعارات لتفعيل الطيران (<code>AppLifecycleState.resumed</code>)، يستشعر التطبيق الحدث ويعيد قراءة حالة المودم وتحديث الواجهة فوراً دون الحاجة لإعادة تشغيل التطبيق، مع مؤقت دوري كل 3 ثوانٍ لمراقبة الإشارة باستمرار.
        </p>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 9: واجهة المستخدم وأوضاع اليمن ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب التاسع: أنماط الشبكة وشاشات التطبيق</span>
        </div>

        <h1>9. واجهة المستخدم والأوضاع الخمسة لشركات الاتصالات باليمن</h1>

        <div class="images-grid-three">
            <div class="screen-container">
                <img class="screen-img" src="data:image/png;base64,{app_screen_b64}" alt="واجهة التطبيق الرئيسية">
                <div class="screen-caption">1. واجهة تطبيق NET Mode</div>
            </div>
            <div class="screen-container">
                <img class="screen-img" src="data:image/png;base64,{device_screen_b64}" alt="شاشة Phone info">
                <div class="screen-caption">2. شاشة المودم Phone Info</div>
            </div>
            <div class="screen-container">
                <img class="screen-img" src="data:image/png;base64,{airplane_screen_b64}" alt="وضع الطيران">
                <div class="screen-caption">3. رصد وضع الطيران بدقة</div>
            </div>
        </div>

        <h2>جدول الأنماط الخمسة المخصصة لليمن:</h2>
        <table>
            <thead>
                <tr>
                    <th style="width: 5%;">#</th>
                    <th style="width: 25%;">اسم النمط بالتطبيق</th>
                    <th style="width: 35%;">الخيار المقابل في المودم (RadioInfo)</th>
                    <th style="width: 35%;">الفائدة التشغيلية وبيئة الاستخدام باليمن</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>1</b></td>
                    <td><span class="badge-chip">Yemen Mobile+4G</span></td>
                    <td><code>CDMA+LTE/EVDO (PRL)</code></td>
                    <td>تثبيت ودمج الفورجي مع الثري جي ليمن موبايل لبقاء الإنترنت والمكالمات معاً.</td>
                </tr>
                <tr>
                    <td><b>2</b></td>
                    <td><span class="badge-green">Yemen Mobile 3G Only</span></td>
                    <td><code>CDMA/EVDO auto (PRL)</code></td>
                    <td>قفل الهاتف على شبكة 3G فقط؛ لتوفير البطارية وفي المناطق الجبلية والريفية.</td>
                </tr>
                <tr>
                    <td><b>3</b></td>
                    <td><span class="badge-chip">sabafon + you</span></td>
                    <td><code>GSM/WCDMA/LTE (PRL)</code></td>
                    <td>مخصص لشرائح سبأفون ويو العاملة بنظام GSM للتنقل السلس بين 4G و 3G دون انقطاع.</td>
                </tr>
                <tr>
                    <td><b>4</b></td>
                    <td><span class="badge-chip">VoLTE</span></td>
                    <td><code>LTE only</code></td>
                    <td>قفل الهاتف الصارم على 4G فقط؛ لمنع التقطيع نهائياً أثناء ألعاب الأونلاين والتحميل.</td>
                </tr>
                <tr>
                    <td><b>5</b></td>
                    <td><span class="badge-purple">(Auto)</span></td>
                    <td><code>NR/LTE/CDMA/EvDo/GSM/WCDMA</code></td>
                    <td>الوضع التلقائي الشامل لجميع الشبكات والترددات (5G/4G/3G/2G) دون أي تقييد.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 10: إدارة التكوين وحماية GitHub ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب العاشر: إدارة التكوين وحماية فروع GitHub</span>
        </div>

        <h1>10. إدارة التكوين، حماية فروع GitHub وسير العمل (Git Workflow)</h1>

        <h2>10.1 فروع العمل الرسمية للفريق على GitHub:</h2>
        <p>تم رفع وتخصيص الفروع التالية على المستودع الرسمي لضمان استقلالية كل مهندس:</p>
        <ul>
            <li>فرع أحمد العماري: <code>feature/issue-1-native-platform-and-intents</code></li>
            <li>فرع محمد الدعيس: <code>feature/issue-2-domain-contracts-and-usecases</code></li>
            <li>فرع يوسف خيري: <code>feature/issue-3-data-repository-and-method-channel</code></li>
            <li>فرع مؤيد الصوفي: <code>feature/issue-4-presentation-ui-and-visualizer</code></li>
            <li>فرع الاختبارات وضمان الجودة: <code>feature/issue-5-permissions-and-edge-cases</code></li>
        </ul>

        <h2>10.2 حماية الفرع الرئيسي (Branch Protection Rule on `main`):</h2>
        <div class="alert-box">
            تم تفعيل قاعدة الحماية <b>Require a pull request before merging</b> على فرع <code>main</code>؛ بحيث يُمنع أي عضو في الفريق من عمل <code>git push origin main</code> مباشرة، ويُشترط فتح Pull Request وخضوعه للمراجعة والاختبار قبل الدمج من قِبل رئيس الفريق أحمد العماري.
        </div>

        <h2>10.3 نتائج ضمان الجودة والاختبارات الآلية (Testing Suite):</h2>
        <div class="card-box-accent">
            <ul>
                <li><b>اختبارات الوحدات (Unit Tests):</b> تغطية شاملة لكيانات <code>NetworkMode</code> ومستودع البيانات وحالات الاستخدام في <code>test/</code>.</li>
                <li><b>اختبارات الواجهات (Widget Tests):</b> محاكاة الشاشة الرئيسية واختبار محاكاة وضع الطيران عبر فئة وهمية <code>FakeAirplaneRepository</code>.</li>
                <li><b>نتيجة تشغيل الاختبارات الآلية:</b> اجتياز 11 اختباراً بنجاح تام: <code>flutter test</code> ➔ <b>(11/11 All tests passed!)</b>.</li>
                <li><b>نتيجة التحليل الساكن:</b> فحص الكود بالكامل عبر <code>flutter analyze</code> ➔ <b>(No issues found!)</b>.</li>
            </ul>
        </div>
    </div>

    <div class="page-break"></div>

    <!-- ══════════ الباب 11: سيناريو المناقشة الشفهية ══════════ -->
    <div>
        <div class="header-bar">
            <span>تقرير مشروع NET Mode — هندسة النظم الخلوية</span>
            <span>الباب الحادي عشر: سيناريو ودليل المناقشة الشفهية</span>
        </div>

        <h1>11. سيناريو ودليل المناقشة الشفهية أمام الدكتور ساهر الهمداني</h1>

        <p>عند بدء المناقشة، يتحدث أعضاء الفريق بالتسلسل الهندسي التالي لإبراز قوة وتكامل العمل الجماعي:</p>

        <div class="engineer-card">
            <b>1. المهندس أحمد ياسين العماري (Project Lead & Native Platform Engineer):</b>
            <p style="margin-top: 4px;">
                "بسم الله الرحمن الرحيم. أهلاً بك يا دكتور ساهر. فكرة مشروعنا NET Mode انطلقت لحل مشاكل تذبذب شبكات 4G و 3G باليمن، واختلاف تقنيات CDMA ليمن موبايل عن GSM لسبأفون ويو، وحظر سامسونج لكود الراديو <code>*#*#4636#*#*</code>. دوري كـ Project Lead شمل إدارة سريان العمل الهندسي (Pipeline) وإدارة وحماية فروع المستودع على GitHub. وبرمجياً، توليت المسار الأول (Epic 1) بالمهام من Issue #1 إلى #6 في <code>MainActivity.kt</code> بلغة Kotlin؛ حيث تجاوزت حظر كود سامسونج بسلسلة نيات تعاقبية، وحللت مشكلة عدم بث الاسم لشرائح CDMA عبر <code>SubscriptionManager</code> والكود 421، وبرمجت كشف وضع الطيران لمنع القراءات الكاذبة."
            </p>
        </div>

        <div class="engineer-card">
            <b>2. المهندس محمد علي / محمد الدعيس (Core Domain & Software Architect):</b>
            <p style="margin-top: 4px;">
                "دكتورنا الفاضل، طبقت معمارية Clean Architecture ومبادئ SOLID ودستور <code>GEMINI.md</code>. توليت المسار الثاني (Epic 2) بالمهام من Issue #7 إلى #12؛ حيث قمت بعزل طبقة النطاق <code>lib/domain/</code> ككود Dart نقي خالي 100% من أي استيراد لـ Flutter أو أندرويد لضمان استقلالية منطق الأعمال. وصممت الكيانات غير القابلة للتعديل <code>NetworkMode</code> و <code>NetworkInfo</code> وحالات الاستخدام المنفصلة (Use Cases). وأدرت التخطيط في Trello بربط كل بطاقة بمتطلبات وثيقة الـ SRS، وطبقت معايير إنجاز صارمة (Definition of Done) تضمن عدم دمج أي مهمة إلا بعد استيفاء اختباراتها."
            </p>
        </div>

        <div class="engineer-card">
            <b>3. المهندس يوسف خيري (Data Layer & Telephony Storage Engineer):</b>
            <p style="margin-top: 4px;">
                "أهلاً دكتور. توليت المسار الثالث (Epic 3) بالمهام من Issue #13 إلى #18؛ حيث بنيت مستودع <code>NetworkRepositoryImpl</code> وطبقت نمط التجريد لعزل قنوات الاتصال بالمنصة. أنشأت مصدر البيانات <code>RadioDeviceDataSourceImpl</code> وربطته بـ <code>MethodChannel</code> باسم <code>com.netmode.app/radio</code> لنقل بيانات المودم بين دارت وكوتلن بدون تجميد للواجهة وبشكل غير متزامن، مع إدارة وحفظ النمط المفضل للمستخدم محلياً وإدارة الصلاحيات في AndroidManifest."
            </p>
        </div>

        <div class="engineer-card">
            <b>4. المهندس مؤيد الصوفي (UI/UX & Presentation State Engineer):</b>
            <p style="margin-top: 4px;">
                "دكتورنا الكريم، توليت المسار الرابع (Epic 4) بالمهام من Issue #19 إلى #24؛ حيث بنيت واجهة تفاعلية متطورة (Cyberpunk Dark Navy Theme) وفق معايير UI/UX Pro Max. صممت بطاقة المراقبة الحية التي تحتوي على 5 أعمدة نيون مضيئة تتفاعل مع الإشارة وتنطفئ تماماً في وضع الطيران، وشارة ذكية لبطاقة SIM، والأنماط الخمسة لليمن. كما دمجت فئة <code>WidgetsBindingObserver</code> مع دورة حياة التطبيق، مما جعل الواجهة تُحدث نفسها تلقائياً فور عودة المستخدم من إعدادات المودم أو فور تفعيل وضع الطيران دون الحاجة للمس الشاشة."
            </p>
        </div>

        <div style="margin-top: 30px; text-align: center; border-top: 1px solid #e2e8f0; padding-top: 15px;">
            <p style="font-size: 11pt; font-weight: 800; color: #0369a1;">تم بحمد الله وتوفيقه</p>
            <p style="font-size: 9.5pt; color: #64748b;">إعداد الفريق الهندسي لمشروع NET Mode — إشراف الأستاذ الدكتور: د.م. ساهر الهمداني (2026 م)</p>
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
    # تحديث النسخة النهائية أيضاً
    import shutil
    shutil.copyfile(pdf_path, final_pdf_path)
    print("Copied to final PDF path successfully.")
else:
    print("PDF generation failed:", res.stderr)
