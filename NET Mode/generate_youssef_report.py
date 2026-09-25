import os
import subprocess

workspace_dir = r"c:\Users\ComputerWorld\OneDrive\Desktop\the colage\my project\python\engring progriming\real_project\NET Mode"
html_path = os.path.join(workspace_dir, "youssef_khairy_report.html")
pdf_path = os.path.join(workspace_dir, "Youssef_Khairy_Engineering_Report.pdf")

html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>التقرير الهندسي المفصل: دور المهندس يوسف خيري في مشروع NET Mode</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap');

        @page {
            size: A4;
            margin: 14mm 12mm 14mm 12mm;
            @bottom-left {
                content: "NET Mode • تقرير طبقة البيانات والتخزين (Data Layer)";
                font-family: 'Tajawal', sans-serif;
                font-size: 8.5pt;
                color: #94a3b8;
            }
            @bottom-right {
                content: "صفحة " counter(page);
                font-family: 'Tajawal', sans-serif;
                font-size: 9pt;
                font-weight: 700;
                color: #0284c7;
            }
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Tajawal', 'Segoe UI', Tahoma, sans-serif;
            background-color: #ffffff;
            color: #0f172a;
            line-height: 1.65;
            font-size: 10pt;
        }

        .page-break {
            page-break-after: always;
            break-after: page;
        }

        /* ── Cover Page ── */
        .cover-page {
            min-height: 260mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            text-align: center;
            padding: 30px 20px;
            background: linear-gradient(145deg, #0b1329 0%, #0f172a 40%, #034674 100%);
            color: #ffffff;
            border-radius: 14px;
        }

        .cover-header {
            margin-top: 15px;
        }

        .badge-tag {
            display: inline-block;
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1.5px solid #38bdf8;
            padding: 5px 18px;
            border-radius: 20px;
            font-size: 11pt;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 16px;
        }

        .cover-title {
            font-size: 30pt;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }

        .cover-subtitle {
            font-size: 16pt;
            font-weight: 700;
            color: #38bdf8;
            margin-bottom: 12px;
        }

        .cover-desc {
            font-size: 11.5pt;
            color: #cbd5e1;
            max-width: 620px;
            line-height: 1.7;
            margin: 0 auto;
        }

        .member-focus-card {
            background: rgba(255, 255, 255, 0.06);
            border: 1.5px solid rgba(56, 189, 248, 0.3);
            border-radius: 14px;
            padding: 18px 30px;
            margin-top: 20px;
            max-width: 580px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        }

        .member-role {
            font-size: 13pt;
            font-weight: 800;
            color: #38bdf8;
            margin-bottom: 4px;
        }

        .member-name {
            font-size: 20pt;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 6px;
        }

        .member-specialty {
            font-size: 10.5pt;
            color: #94a3b8;
        }

        .cover-stats {
            display: flex;
            gap: 14px;
            justify-content: center;
            margin-top: 20px;
            width: 100%;
        }

        .stat-box {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(56, 189, 248, 0.25);
            padding: 10px 18px;
            border-radius: 10px;
            flex: 1;
            max-width: 150px;
        }

        .stat-number {
            font-size: 18pt;
            font-weight: 900;
            color: #38bdf8;
        }

        .stat-text {
            font-size: 8.5pt;
            color: #cbd5e1;
            font-weight: 600;
        }

        .cover-footer {
            width: 100%;
            display: flex;
            justify-content: space-around;
            background: rgba(0, 0, 0, 0.4);
            padding: 16px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            margin-top: 20px;
        }

        .meta-card {
            text-align: center;
        }

        .meta-label {
            font-size: 9pt;
            color: #94a3b8;
            margin-bottom: 3px;
        }

        .meta-val {
            font-size: 11.5pt;
            font-weight: 700;
            color: #ffffff;
        }

        /* ── Content Pages ── */
        .content-container {
            padding: 8px 4px;
        }

        .header-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 6px;
            margin-bottom: 16px;
        }

        .header-title {
            font-size: 14pt;
            font-weight: 800;
            color: #0369a1;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .header-tag {
            font-size: 8.5pt;
            background: #e0f2fe;
            color: #0369a1;
            padding: 3px 10px;
            border-radius: 12px;
            font-weight: 700;
        }

        h2 {
            font-size: 13pt;
            font-weight: 800;
            color: #0f172a;
            margin: 14px 0 8px 0;
            border-right: 4px solid #0284c7;
            padding-right: 8px;
        }

        h3 {
            font-size: 11pt;
            font-weight: 700;
            color: #0369a1;
            margin: 10px 0 6px 0;
        }

        p {
            margin-bottom: 8px;
            text-align: justify;
            color: #334155;
            font-size: 9.5pt;
        }

        /* ── Cards & Boxes ── */
        .card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 12px 14px;
            margin-bottom: 12px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        }

        .card-highlight {
            background: #f0f9ff;
            border: 1.5px solid #bae6fd;
            border-radius: 10px;
            padding: 12px 14px;
            margin-bottom: 12px;
        }

        .card-warning {
            background: #fffbeb;
            border: 1.5px solid #fde68a;
            border-radius: 10px;
            padding: 12px 14px;
            margin-bottom: 12px;
        }

        .card-success {
            background: #f0fdf4;
            border: 1.5px solid #bbf7d0;
            border-radius: 10px;
            padding: 12px 14px;
            margin-bottom: 12px;
        }

        /* ── Tables ── */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0 14px 0;
            font-size: 8.8pt;
        }

        th, td {
            border: 1px solid #cbd5e1;
            padding: 7px 10px;
            text-align: right;
        }

        th {
            background: #0f172a;
            color: #ffffff;
            font-weight: 700;
        }

        tr:nth-child(even) {
            background-color: #f8fafc;
        }

        /* ── Code Blocks ── */
        pre {
            background: #0f172a;
            color: #f8fafc;
            padding: 10px 12px;
            border-radius: 8px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 8.2pt;
            direction: ltr;
            text-align: left;
            overflow-x: auto;
            margin: 8px 0 10px 0;
            border: 1px solid #334155;
            line-height: 1.45;
        }

        code {
            font-family: 'Consolas', 'Courier New', monospace;
            background: #e2e8f0;
            color: #0f172a;
            padding: 1px 4px;
            border-radius: 4px;
            font-size: 8.5pt;
            direction: ltr;
            display: inline-block;
        }

        /* ── Lists ── */
        ul, ol {
            margin: 6px 18px 10px 0;
            color: #334155;
            font-size: 9.3pt;
        }

        li {
            margin-bottom: 5px;
        }

        .badge {
            display: inline-block;
            padding: 2px 7px;
            border-radius: 6px;
            font-size: 7.5pt;
            font-weight: 700;
        }

        .badge-blue { background: #e0f2fe; color: #0284c7; }
        .badge-green { background: #dcfce7; color: #15803d; }
        .badge-purple { background: #f3e8ff; color: #7e22ce; }
        .badge-amber { background: #fef3c7; color: #b45309; }

        .diagram-box {
            background: #0b1329;
            color: #38bdf8;
            padding: 12px;
            border-radius: 10px;
            text-align: center;
            font-family: 'Consolas', monospace;
            font-size: 8.2pt;
            direction: ltr;
            margin: 10px 0;
            border: 1px solid #0284c7;
            white-space: pre;
            line-height: 1.35;
        }
    </style>
</head>
<body>

    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- الصفحة 1: الغلاف الفاخر (Cover Page)                                -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="cover-page">
        <div class="cover-header">
            <div class="badge-tag">📡 وثيقة هندسية تخصصية • تقرير عضو الفريق</div>
            <h1 class="cover-title">مشروع NET Mode</h1>
            <div class="cover-subtitle">دراسة تحليلية شاملة لدور مهندس طبقة البيانات والتخزين</div>
            <p class="cover-desc">
                توثيق هندسي دقيق لجميع المراحل البرمجية، الملفات المنفذة، بنية نقل البيانات عبر قنوات المنصة، ومصفوفة التغلب على العوائق الفنية وفق معمارية Clean Architecture ومبادئ SOLID.
            </p>
        </div>

        <div class="member-focus-card">
            <div class="member-role">⚡ العضو الثالث في الفريق الهندسي</div>
            <div class="member-name">المهندس / يوسف خيري</div>
            <div class="member-specialty">Data Layer & Telephony Storage Engineer</div>
            <div style="margin-top: 10px; font-size: 9.5pt; color: #7dd3fc; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 8px;">
                مسؤولية ربط منصة أندرويد بالمعمارية النظيفة • إدارة استدعاءات MethodChannel • التخزين المحلي الآمن للأجهزة
            </div>
        </div>

        <div class="cover-stats">
            <div class="stat-box">
                <div class="stat-number">6</div>
                <div class="stat-text">قصص مستخدم (US-13 إلى US-18)</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">100%</div>
                <div class="stat-text">نسبة نجاح الاختبارات الآلية</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">0%</div>
                <div class="stat-text">تسريب بيانات (معالجة محلية)</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">Zero</div>
                <div class="stat-text">انهيار للتطبيق (Crash-Free)</div>
            </div>
        </div>

        <div class="cover-footer">
            <div class="meta-card">
                <div class="meta-label">المشروع الهندسي</div>
                <div class="meta-val">NET Mode Cellular Suite</div>
            </div>
            <div class="meta-card">
                <div class="meta-label">المهندس المعني</div>
                <div class="meta-val">يوسف خيري</div>
            </div>
            <div class="meta-card">
                <div class="meta-label">الإشراف الأكاديمي</div>
                <div class="meta-val">د.م. ساهر الهمداني</div>
            </div>
            <div class="meta-card">
                <div class="meta-label">تاريخ التحكيم</div>
                <div class="meta-val">سبتمبر 2026</div>
            </div>
        </div>
    </div>

    <div class="page-break"></div>

    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- الصفحة 2: موقع يوسف خيري في المعمارية ومسؤولياته الأساسية           -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="content-container">
        <div class="header-bar">
            <div class="header-title">1. موقع يوسف خيري في معمارية Clean Architecture ومسؤولياته</div>
            <div class="header-tag">المعمارية الهندسية</div>
        </div>

        <h2>1.1 أين يكمن دور المهندس يوسف خيري في النظام؟</h2>
        <p>
            تعتبر <b>طبقة البيانات (Data Layer)</b> التي طورها المهندس <b>يوسف خيري</b> هي "حلقة الوصل والعمود الفقري" في التطبيق؛ فهي تفصل بين منطق الأعمال المجرد النقي (Domain Layer) وبين العالم الخارجي والعتاد الفعلي لنظام أندرويد (Platform Layer & Storage).
        </p>

        <div class="diagram-box">
┌────────────────────────────────────────────────────────────────────────┐
│                      Presentation Layer (UI)                           │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (Calls UseCases)
┌───────────────────────────────────▼────────────────────────────────────┐
│                      Domain Layer (Pure Dart)                          │
│   NetworkRepository (Abstract Contract) ◄─── (Entities & UseCases)     │
└───────────────────────────────────▲────────────────────────────────────┘
                                    │ (Implements Interface)
┌───────────────────────────────────┴────────────────────────────────────┐
│      ★ نطاق عمل يوسف خيري: Data Layer (طبقة البيانات والتخزين) ★         │
│   ┌────────────────────────────────┐  ┌────────────────────────────┐   │
│   │     NetworkRepositoryImpl      │  │ RadioDeviceDataSourceImpl  │   │
│   │ (DTO to Entity Mapping & Cache)│  │ (MethodChannel & Fallbacks)│   │
│   └────────────────────────────────┘  └────────────────────────────┘   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (Invokes MethodChannel: 'com.netmode.app/radio')
┌───────────────────────────────────▼────────────────────────────────────┐
│                 Native Platform Layer (Kotlin / Android)               │
└────────────────────────────────────────────────────────────────────────┘
        </div>

        <h2>1.2 المهام الموكلة للمهندس يوسف خيري (User Stories US-13 إلى US-18)</h2>
        <p>وفقاً لوثائق متطلبات البرمجيات (SRS) وقصص المستخدمين، تولى يوسف خيري تنفيذ 6 قصص مستخدم محورية:</p>

        <table>
            <thead>
                <tr>
                    <th style="width: 10%;">الرمز</th>
                    <th style="width: 25%;">عنوان المهمة</th>
                    <th style="width: 35%;">الملفات المسؤولة</th>
                    <th style="width: 30%;">الأثر البرمجي والهندسي</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>US-13</b></td>
                    <td>كلاس مصدر بيانات القناة الأصلية</td>
                    <td><code>lib/data/datasources/radio_device_datasource.dart</code></td>
                    <td>إنشاء استدعاءات MethodChannel الآمنة والتقاط استثناءات PlatformException.</td>
                </tr>
                <tr>
                    <td><b>US-14</b></td>
                    <td>تنفيذ كلاس المستودع الفعلي</td>
                    <td><code>lib/data/repositories/network_repository_impl.dart</code></td>
                    <td>تطبيق عقد NetworkRepository وتحويل الـ Raw Maps إلى كائنات نطاقية.</td>
                </tr>
                <tr>
                    <td><b>US-15</b></td>
                    <td>محرك التخزين المحلي للتفضيلات</td>
                    <td><code>lib/data/repositories/network_repository_impl.dart</code></td>
                    <td>تخزين واسترجاع النمط المفضل للمستخدم في الذاكرة دون الحاجة لخوادم خارجية.</td>
                </tr>
                <tr>
                    <td><b>US-16</b></td>
                    <td>إدارة الصلاحيات الحساسة</td>
                    <td><code>android/app/src/main/AndroidManifest.xml</code></td>
                    <td>إعلان أذونات READ_PHONE_STATE وحماية التطبيق عند رفض المستخدم للصلاحية.</td>
                </tr>
                <tr>
                    <td><b>US-17</b></td>
                    <td>هندسة التحصين واعتراض الأخطاء</td>
                    <td>منظومة الـ Defensive Fallback في DataSource</td>
                    <td>منع الـ Crashes وتمرير قيم افتراضية آمنة في حال فشل المودم أو وضع الطيران.</td>
                </tr>
                <tr>
                    <td><b>US-18</b></td>
                    <td>توثيق أمان البيانات للمتجر</td>
                    <td>إقرارات Google Play Data Safety</td>
                    <td>إثبات أن التطبيق Offline-First ولا يشارك بيانات الاتصال مع أي طرف خارجي.</td>
                </tr>
            </tbody>
        </table>

        <h2>1.3 الالتزام الصارم بمبادئ SOLID</h2>
        <div class="card-highlight">
            <ul style="margin: 0; padding-right: 15px;">
                <li><b>Single Responsibility Principle (SRP):</b> فصل مهام التخاطب مع القناة في <code>RadioDeviceDataSource</code> عن مهام التحويل والتخزين في <code>NetworkRepositoryImpl</code>.</li>
                <li><b>Dependency Inversion Principle (DIP):</b> لا تعتمد طبقة النطاق على يوسف، بل يوسف هو من يعتمد على تجريدات النطاق وينفذ واجهة <code>NetworkRepository</code>.</li>
                <li><b>Liskov Substitution Principle (LSP):</b> تصميم المستودع بحيث يمكن استبداله بـ <code>MockNetworkRepository</code> في الاختبارات دون أي تغيير في السلوك.</li>
            </ul>
        </div>
    </div>

    <div class="page-break"></div>

    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- الصفحة 3: دراسة الملفات البرمجية خطوة بخطوة                       -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="content-container">
        <div class="header-bar">
            <div class="header-title">2. التحليل التفصيلي للملفات البرمجية التي أنجزها يوسف خيري</div>
            <div class="header-tag">الكود البرمجي خطوة بخطوة</div>
        </div>

        <h2>2.1 الملف الأول: مصدر بيانات الراديو (radio_device_datasource.dart)</h2>
        <p>
            قام يوسف خيري ببناء واجهة تجريدية <code>RadioDeviceDataSource</code> تليها فئة التنفيذ <code>RadioDeviceDataSourceImpl</code>، لتكون البوابة الحصرية الوحيدة في التطبيق التي تتحدث مع <code>MethodChannel</code>:
        </p>

        <pre><code>// lib/data/datasources/radio_device_datasource.dart
abstract class RadioDeviceDataSource {
  Future&lt;Map&lt;String, dynamic&gt;&gt; getInstantNetworkSnapshot();
  Future&lt;bool&gt; openRadioMenu();
  Future&lt;bool&gt; setNetworkMode(int networkTypeCode);
}

class RadioDeviceDataSourceImpl implements RadioDeviceDataSource {
  static const _channel = MethodChannel('com.netmode.app/radio');

  @override
  Future&lt;Map&lt;String, dynamic&gt;&gt; getInstantNetworkSnapshot() async {
    try {
      final result = await _channel.invokeMapMethod&lt;String, dynamic&gt;('getInstantNetworkSnapshot');
      return result ?? {'networkType': 'Unknown', 'carrier': 'No Carrier', 'simState': false};
    } on PlatformException catch (_) {
      // اعتراض استثناءات النظام وإرجاع بيانات آمنة لمنع الانهيار
      return {'networkType': 'Unknown', 'carrier': 'No Carrier', 'simState': false};
    }
  }

  @override
  Future&lt;bool&gt; openRadioMenu() async {
    try {
      final bool? success = await _channel.invokeMethod&lt;bool&gt;('openRadioSettings');
      return success ?? false;
    } on PlatformException catch (_) {
      return false;
    }
  }

  @override
  Future&lt;bool&gt; setNetworkMode(int networkTypeCode) async {
    try {
      final bool? applied = await _channel.invokeMethod&lt;bool&gt;(
        'setNetworkMode',
        {'networkTypeCode': networkTypeCode},
      );
      return applied ?? false;
    } on PlatformException catch (_) {
      return false;
    }
  }
}</code></pre>

        <div class="card">
            <b>تحليل القرارات الهندسية ليوسف في هذا الملف:</b>
            <ol style="margin-right: 15px; margin-top: 5px;">
                <li><b>اسم القناة الموحد:</b> تم تثبيت القناة <code>com.netmode.app/radio</code> بالتنسيق مع مهندس المنصة (أحمد العماري).</li>
                <li><b>البرمجة الدفاعية (Defensive Fallback):</b> استخدام <code>invokeMapMethod</code> المحمي بـ <code>try/catch</code> مع إرجاع قاموس افتراضي ذكي يمنع الـ Null Pointer.</li>
                <li><b>الاستدعاءات غير المتزامنة:</b> جميع الدوال تعيد <code>Future</code> لتجنب تجميد خيط الواجهة الرئيسي (UI Thread).</li>
            </ol>
        </div>

        <h2>2.2 الملف الثاني: مستودع الشبكات الفعلي (network_repository_impl.dart)</h2>
        <p>
            هنا تكمن عبقرية تحويل البيانات من كائنات خام (Raw Maps) إلى كيانات نطاقية معتمدة (Domain Entities):
        </p>

        <pre><code>// lib/data/repositories/network_repository_impl.dart
class NetworkRepositoryImpl implements NetworkRepository {
  final RadioDeviceDataSource _radioDataSource;
  NetworkMode? _cachedPreferredMode; // التخزين المحلي السريع لتفضيل النمط

  NetworkRepositoryImpl({required RadioDeviceDataSource radioDataSource})
      : _radioDataSource = radioDataSource;

  @override
  Future&lt;NetworkInfo&gt; getInstantNetworkSnapshot() async {
    final rawSnapshot = await _radioDataSource.getInstantNetworkSnapshot();

    // هندسة التحويل الآمن (Safe Data Mapping)
    return NetworkInfo(
      carrier: rawSnapshot['carrier']?.toString() ?? 'No Carrier',
      networkType: rawSnapshot['networkType']?.toString() ?? 'Unknown',
      hasSimCard: rawSnapshot['simState'] == true,
      isAirplaneMode: rawSnapshot['isAirplaneMode'] == true,
    );
  }

  @override
  Future&lt;bool&gt; openRadioTestingSettings() =&gt; _radioDataSource.openRadioMenu();

  @override
  Future&lt;void&gt; savePreferredMode(NetworkMode mode) async {
    _cachedPreferredMode = mode;
  }

  @override
  Future&lt;NetworkMode?&gt; getPreferredMode() async =&gt; _cachedPreferredMode;

  @override
  Future&lt;bool&gt; setNetworkMode(NetworkMode mode) =&gt; 
      _radioDataSource.setNetworkMode(mode.networkTypeCode);
}</code></pre>
    </div>

    <div class="page-break"></div>

    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- الصفحة 4: المراحل التنفيذية واختبارات الوحدة                         -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="content-container">
        <div class="header-bar">
            <div class="header-title">3. المراحل التنفيذية واختبارات الوحدة الآلية لطبقة البيانات</div>
            <div class="header-tag">المراحل والاختبارات</div>
        </div>

        <h2>3.1 المراحل الزمنية التي اتبعها يوسف خيري في بناء طبقة البيانات</h2>
        <p>قام يوسف خيري بتنفيذ مهامه عبر 5 مراحل هندسية متسلسلة:</p>

        <div class="card">
            <b>المرحلة 1: تحليل وتوصيف عقد التبادل (Protocol Specification)</b><br />
            تحديد بنية قاموس البيانات المشترك مع مهندس المنصة بلغة Kotlin: مفاتيح <code>carrier</code>, <code>networkType</code>, <code>simState</code>, و <code>isAirplaneMode</code> لتجنب أي تعارض في أسماء الحقول.
        </div>

        <div class="card">
            <b>المرحلة 2: بناء مصدر البيانات الأصيل وتطويق الاستثناءات (Data Source Layer)</b><br />
            كتابة كلاس <code>RadioDeviceDataSourceImpl</code> وتطبيق آليات التقاط <code>PlatformException</code> لمنع توقف التطبيق في حال تعطل خدمة TelephonyManager.
        </div>

        <div class="card">
            <b>المرحلة 3: بناء محول البيانات والمستودع (Mapping & Repository Implementation)</b><br />
            تنفيذ عقد <code>NetworkRepository</code> وتحويل الخرائط إلى كائنات <code>NetworkInfo</code> النطاقية، وحفظ النمط المفضل في ذاكرة التشغيل.
        </div>

        <div class="card">
            <b>المرحلة 4: هندسة الأذونات وسياسة أمان البيانات (Permissions & Store Compliance)</b><br />
            التأكد من سلامة التعامل مع إذن <code>READ_PHONE_STATE</code> وتقديم إقرار أن التطبيق يعمل Offline-First دون أي إرسال للبيانات عبر الإنترنت.
        </div>

        <div class="card">
            <b>المرحلة 5: صياغة اختبارات الوحدة بالـ Mock (Automated Testing)</b><br />
            كتابة اختبارات الوحدة والتأكد من نجاحها الكامل دون الحاجة لتوصيل هاتف حقيقي عبر Mock Data Source.
        </div>

        <h2>3.2 ملف اختبارات طبقة البيانات (network_repository_impl_test.dart)</h2>
        <p>لضمان استقرار المستودع بنسبة 100%، كتب يوسف هذا الاختبار الآلي الذي يجري تشغيله بنجاح:</p>

        <pre><code>// test/data/repositories/network_repository_impl_test.dart
class MockRadioDataSource implements RadioDeviceDataSource {
  @override
  Future&lt;Map&lt;String, dynamic&gt;&gt; getInstantNetworkSnapshot() async =&gt; {
    'carrier': 'Test Carrier',
    'networkType': '4G LTE',
    'simState': true,
  };
  @override
  Future&lt;bool&gt; openRadioMenu() async =&gt; true;
  @override
  Future&lt;bool&gt; setNetworkMode(int networkTypeCode) async =&gt; true;
}

void main() {
  test('maps raw data source map to Domain NetworkInfo entity', () async {
    final repository = NetworkRepositoryImpl(radioDataSource: MockRadioDataSource());
    final info = await repository.getInstantNetworkSnapshot();

    expect(info.carrier, 'Test Carrier');
    expect(info.networkType, '4G LTE');
    expect(info.hasSimCard, true);
  });

  test('saves and retrieves preferred mode in memory', () async {
    final repository = NetworkRepositoryImpl(radioDataSource: MockRadioDataSource());
    await repository.savePreferredMode(NetworkMode.lteOnly);
    final saved = await repository.getPreferredMode();
    expect(saved, equals(NetworkMode.lteOnly));
  });
}</code></pre>
    </div>

    <div class="page-break"></div>

    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- الصفحة 5: العوائق والتحديات الهندسية وكيفية التغلب عليها            -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="content-container">
        <div class="header-bar">
            <div class="header-title">4. العوائق والتحديات التي واجهت يوسف خيري والحلول المبتكرة</div>
            <div class="header-tag">العوائق والحلول الهندسية</div>
        </div>

        <h2>4.1 جدول العوائق الهندسية وكيفية التغلب عليها</h2>

        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">العائق / التحدي الهندسي</th>
                    <th style="width: 35%;">طبيعة المشكلة والمخاطر</th>
                    <th style="width: 40%;">الحل الهندسي المبتكر المطبق</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>1. استثناءات المنصة المفاجئة<br>(PlatformExceptions)</b></td>
                    <td>عند تشغيل التطبيق على أجهزة قديمة أو واجهات معدلة تمنع استدعاءات الراديو، قد تقذف القناة استثناء يسبب انهياراً فورياً (Crash).</td>
                    <td><b>الحل:</b> قام يوسف بتطويق استدعاءات <code>_channel.invokeMethod</code> بكتل <code>try/catch</code> صارمة وإرجاع قيم افتراضية آمنة (Defensive Fallback).</td>
                </tr>
                <tr>
                    <td><b>2. عدم تجانس أنواع البيانات والـ Null Safety</b></td>
                    <td>منصة أندرويد قد ترجع قيماً فارغة (Null) لاسم المشغل في شبكات CDMA مثل يمن موبايل، أو قيماً غير نصية.</td>
                    <td><b>الحل:</b> تطبيق مبدأ التحويل الدفاعي الصارم:<br><code>rawSnapshot['carrier']?.toString() ?? 'No Carrier'</code> مما منع حدوث أي NullPointerException.</td>
                </tr>
                <tr>
                    <td><b>3. رفض المستخدم لصلاحية قراءة الهاتف (READ_PHONE_STATE)</b></td>
                    <td>إذا رفض المستخدم الصلاحية الحساسة، ستفشل قراءة اسم المشغل والشبكة.</td>
                    <td><b>الحل:</b> برمجة طبقة البيانات بحيث تتعايش مع غياب الصلاحية وتستعرض حالة <code>Cellular / Unknown</code> مع إبقاء زر التحويل يعمل دون توقف.</td>
                </tr>
                <tr>
                    <td><b>4. فحص واختبار الكود بدون هاتف متصل</b></td>
                    <td>في بيئة الاختبارات الآلية (CI/CD)، لا يتوفر هاتف حقيقي لتنفيذ استدعاءات الـ MethodChannel مما يمنع فحص الكود.</td>
                    <td><b>الحل:</b> صياغة واجهة تجريدية <code>RadioDeviceDataSource</code>، مما مكنه من كتابة <code>MockRadioDataSource</code> وفحص المستودع بنسبة نجاح 100%.</td>
                </tr>
                <tr>
                    <td><b>5. اشتراطات متجر Google Play لسياسة أمان البيانات</b></td>
                    <td>تفرض Google متطلبات مشددة عند استخدام أذونات الهاتف؛ خوفاً من تجسس التطبيقات وسرقة بيانات الشريحة.</td>
                    <td><b>الحل:</b> إثبات أن طبقة البيانات لا تستخدم أي مكتبات إنترنت (Zero Network Calls)، وأن المعالجة والتخزين تتم محلياً 100% داخل ذاكرة الهاتف (Offline-First).</td>
                </tr>
            </tbody>
        </table>

        <h2>4.2 الخلاصة والتقييم النهائي لأداء المهندس يوسف خيري</h2>
        <div class="card-success">
            <p style="margin: 0; font-weight: 600; color: #166534;">
                أظهر المهندس <b>يوسف خيري</b> احترافية هندسية عالية في بناء طبقة بيانات مرنة ومتماسكة؛ حيث نجح في عزل تفاصيل نظام أندرويد عن بقية أجزاء التطبيق، وطبق مبادئ البرمجة الدفاعية (Defensive Programming) بامتياز، مما جعل تطبيق <b>NET Mode</b> مستقراً تماماً وخالياً من أي أخطاء انهيار أو تسريب للبيانات.
            </p>
        </div>

        <div style="margin-top: 30px; text-align: center; border-top: 1px solid #e2e8f0; padding-top: 15px;">
            <p style="font-size: 10pt; font-weight: 700; color: #0369a1;">تم إعداد التقرير بنجاح وتوثيق كافة المراحل والملفات والعوائق</p>
            <p style="font-size: 9pt; color: #64748b;">مشروع NET Mode • إشراف الدكتور: د.م. ساهر الهمداني</p>
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
