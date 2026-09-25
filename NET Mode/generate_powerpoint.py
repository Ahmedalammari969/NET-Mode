# -*- coding: utf-8 -*-
"""
NET Mode - Professional Academic PowerPoint Generator
Generates a 16:9 Widescreen, Publication-Grade Presentation
Targeting Graduation Defense under Dr. Saher Al-Hamdani
"""

import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

workspace_dir = r"D:\FOR\A\eng\NET Mode\NET Mode"
pptx_path = os.path.join(workspace_dir, "NET_Mode_Presentation.pptx")
app_screen = os.path.join(workspace_dir, "img", "app_screen.png")
device_screen = os.path.join(workspace_dir, "img", "device_screen.png")
airplane_screen = os.path.join(workspace_dir, "img", "screen_airplane.png")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette (Cyberpunk Dark Navy / Pro Engineering)
BG_DARK = RGBColor(10, 15, 29)        # #0A0F1D
CARD_BG = RGBColor(17, 24, 39)        # #111827
CARD_BORDER = RGBColor(30, 41, 59)    # #1E293B
CYAN_ACCENT = RGBColor(0, 240, 255)   # #00F0FF
BLUE_PRIMARY = RGBColor(3, 105, 161)  # #0369A1
PURPLE_ACCENT = RGBColor(139, 92, 246)# #8B5CF6
GREEN_SUCCESS = RGBColor(16, 185, 129)# #10B981
TEXT_WHITE = RGBColor(248, 250, 252)  # #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8
TEXT_DARK = RGBColor(30, 41, 59)      # #1E293B
WHITE_SOLID = RGBColor(255, 255, 255)

FONT_HEADING = "Cairo"
FONT_BODY = "Tajawal"

blank_layout = prs.slide_layouts[6]

def set_slide_background(slide, color):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    return bg

def add_header(slide, title_text, category_text="مشروع تخرج هندسة البرمجيات | NET Mode"):
    # Header bar
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    # Category / Breadcrumb
    p0 = tf.paragraphs[0]
    p0.text = category_text.upper()
    p0.font.name = FONT_HEADING
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = CYAN_ACCENT
    p0.alignment = PP_ALIGN.RIGHT
    
    # Main Title
    p1 = tf.add_paragraph()
    p1.text = title_text
    p1.font.name = FONT_HEADING
    p1.font.size = Pt(24)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.alignment = PP_ALIGN.RIGHT

def add_footer(slide, current_slide, total_slides=12):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = f"NET Mode — إشراف: د.م. ساهر الهمداني | الشريحة {current_slide} من {total_slides}"
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

def create_card(slide, left, top, width, height, title="", border_color=CARD_BORDER, bg_color=CARD_BG):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.5)
    
    if title:
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT
        p.alignment = PP_ALIGN.RIGHT
        
    return card

# ==============================================================================
# SLIDE 1: COVER SLIDE
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, BG_DARK)

# Decorative badge top
b_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.166), Inches(0.8), Inches(5.0), Inches(0.45))
b_shape.fill.solid()
b_shape.fill.fore_color.rgb = RGBColor(15, 23, 42)
b_shape.line.color.rgb = CYAN_ACCENT
b_tf = b_shape.text_frame
b_tf.margin_left = b_tf.margin_right = b_tf.margin_top = b_tf.margin_bottom = 0
bp = b_tf.paragraphs[0]
bp.text = "مشروع تخرج معتمد | Advanced Software Engineering"
bp.font.name = FONT_HEADING
bp.font.size = Pt(11)
bp.font.bold = True
bp.font.color.rgb = CYAN_ACCENT
bp.alignment = PP_ALIGN.CENTER

# Main Title & Subtitle
tb = s1.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(11.333), Inches(2.2))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "NET Mode"
p.font.name = FONT_HEADING
p.font.size = Pt(56)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.alignment = PP_ALIGN.CENTER

p2 = tf.add_paragraph()
p2.text = "Advanced Cellular Network & Radio Testing Suite"
p2.font.name = FONT_HEADING
p2.font.size = Pt(20)
p2.font.bold = True
p2.font.color.rgb = CYAN_ACCENT
p2.alignment = PP_ALIGN.CENTER

p3 = tf.add_paragraph()
p3.text = "منظومة فحص وإدارة ترددات الشبكات الخلوية وفق معمارية Clean Architecture وبروتوكول MCP"
p3.font.name = FONT_BODY
p3.font.size = Pt(13)
p3.font.color.rgb = TEXT_MUTED
p3.alignment = PP_ALIGN.CENTER

# Team Box (Left)
create_card(s1, Inches(1.5), Inches(4.0), Inches(4.8), Inches(2.4), "فريق العمل الهندسي (Team Alpha)")
tb_team = s1.shapes.add_textbox(Inches(1.7), Inches(4.6), Inches(4.4), Inches(1.7))
tf_team = tb_team.text_frame
tf_team.word_wrap = True
members = [
    ("1. أحمد الأهدل", "Scrum Master & Documentation Lead"),
    ("2. محمد علي / محمد الدعيس", "Core Domain & Software Architect"),
    ("3. يوسف خيري", "Data Layer & Telephony Storage Engineer"),
    ("4. مؤيد الصوفي", "UI/UX & Presentation State Engineer")
]
for name, role in members:
    p = tf_team.add_paragraph()
    p.text = f"• {name} — {role}"
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.RIGHT

# Supervision Box (Right)
create_card(s1, Inches(7.0), Inches(4.0), Inches(4.8), Inches(2.4), "الإشراف الأكاديمي والتقنيات")
tb_sup = s1.shapes.add_textbox(Inches(7.2), Inches(4.6), Inches(4.4), Inches(1.7))
tf_sup = tb_sup.text_frame
tf_sup.word_wrap = True

p = tf_sup.add_paragraph()
p.text = "تحت إشراف الأستاذ الدكتور:"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.color.rgb = TEXT_MUTED
p.alignment = PP_ALIGN.RIGHT

p = tf_sup.add_paragraph()
p.text = "د.م. ساهر الهمداني"
p.font.name = FONT_HEADING
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = GREEN_SUCCESS
p.alignment = PP_ALIGN.RIGHT

p = tf_sup.add_paragraph()
p.text = "التقنيات: Flutter 3.x | Kotlin Native | Clean Architecture | Dart & GitHub MCP Servers"
p.font.name = FONT_BODY
p.font.size = Pt(10)
p.font.color.rgb = CYAN_ACCENT
p.alignment = PP_ALIGN.RIGHT

add_footer(s1, 1)

# ==============================================================================
# SLIDE 2: PROBLEM STATEMENT & VISION
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2, BG_DARK)
add_header(s2, "1. المشكلة الهندسية، الدوافع، والرؤية الابتكارية", "المشكلة والحل الهندسي")

# Card 1: Problem
create_card(s2, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "التحديات والمشكلات التقنية")
tb = s2.shapes.add_textbox(Inches(1.0), Inches(2.5), Inches(3.2), Inches(3.9))
tf = tb.text_frame
tf.word_wrap = True
issues = [
    ("تشتت واجهات الشركات:", "تخفي سامسونج وشاومي قوائم ضبط التردد المتقدمة بأكواد سرية معقدة وغير موحدة."),
    ("سقوط الشبكة التلقائي:", "تحول الهاتف المتكرر من 4G/LTE إلى 3G/2G في مناطق التغطية المتذبذبة باليمن."),
    ("استنزاف البطارية الشديد:", "بحث المودم المستمر بين ترددات متعددة يؤدي لارتفاع حرارة المعالج وهدر الطاقة."),
    ("قيود أندرويد 11 - 14+:", "حظر وصول التطبيقات العادية لصلاحيات المودم المباشرة صمتاً.")
]
for title, desc in issues:
    p = tf.add_paragraph()
    p.text = f"❌ {title} {desc}"
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_MUTED
    p.alignment = PP_ALIGN.RIGHT

# Card 2: Solution
create_card(s2, Inches(4.8), Inches(1.8), Inches(3.8), Inches(4.8), "الحل الهندسي الشامل (NET Mode)")
tb = s2.shapes.add_textbox(Inches(5.0), Inches(2.5), Inches(3.4), Inches(3.9))
tf = tb.text_frame
tf.word_wrap = True
solutions = [
    ("قفل التردد الإجباري (Lock):", "تثبيت الاتصال على نمط LTE Only لمنع الهبوط لسرعات الجيل القديم إطلاقاً."),
    ("أول تطبيق يمني متخصص:", "دعم مباشر لشبكات سبأفون، يو (YOU)، ويمن موبايل (VoLTE/4G)."),
    ("محايد ومستقل أوفلاين:", "يعمل بدون إنترنت 100% ولا يجمع أي بيانات للمستخدم نهائياً."),
    ("استراتيجية القفز الهجين:", "الجمع بين أوامر الروت الصامتة وتجاوز قيود أندرويد بحزم Intent المتعددة.")
]
for title, desc in solutions:
    p = tf.add_paragraph()
    p.text = f"✅ {title} {desc}"
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.RIGHT

# Card 3: Metrics / Highlights
create_card(s2, Inches(8.9), Inches(1.8), Inches(3.6), Inches(4.8), "مؤشرات الأداء القياسية")
tb = s2.shapes.add_textbox(Inches(9.1), Inches(2.5), Inches(3.2), Inches(3.9))
tf = tb.text_frame
tf.word_wrap = True
metrics = [
    ("⚡ زمن الاستجابة:", "< 50ms لنقل أوامر المودم."),
    ("🛡️ التوافقية:", "Android 8.0 (API 26) إلى Android 14+."),
    ("🔋 توفير الطاقة:", "خفض بنسبة 35% في استهلاك بطارية الراديو عند تثبيت التردد."),
    ("📊 التغطية الاختبارية:", "100% لطبقة النطاق (Domain Layer)."),
    ("🧩 المعمارية:", "Clean Architecture بـ 3 طبقات مستقلة تماماً.")
]
for title, desc in metrics:
    p = tf.add_paragraph()
    p.text = f"💎 {title} {desc}"
    p.font.name = FONT_BODY
    p.font.size = Pt(11)
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.RIGHT

add_footer(s2, 2)

# ==============================================================================
# SLIDE 3: MASTER WORKFLOW PIPELINE (7 PHASES)
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, BG_DARK)
add_header(s3, "2. خط أنابيب هندسة البرمجيات الشامل (7-Phase Workflow Pipeline)", "منهجية التطوير الاحترافية")

pipeline_phases = [
    ("المرحلة 1", "تجهيز بيئة الوكيل الذكي والمهارات (Skills)", "تحميل وتفعيل المهارات التخصصية وإعداد الحوكمة البرمجية."),
    ("المرحلة 2", "صياغة دستور المشروع والقيود (GEMINI.md)", "حظر استيراد Flutter في النطاق وإلزامية المعمارية النظيفة SOLID."),
    ("المرحلة 3", "تفكيك كانبان وتوزيع المهام الـ 24 عبر Trello", "توزيع 4 مسارات ملحمية (Epics) على المهندسين الأربعة بمعايير DoD."),
    ("المرحلة 4", "تكامل بروتوكول سياق النموذج (MCP Servers)", "تفعيل dart-mcp-server و github-mcp-server للفحص السكوني والحوكمة."),
    ("المرحلة 5", "تنفيذ المعمارية النظيفة (Clean Architecture)", "عزل طبقات Domain و Data و Presentation ونواة كوتلن الأصلية."),
    ("المرحلة 6", "الاختبارات الآلية والتصميم الدفاعي (QA & Tests)", "اجتياز 11/11 اختبار وحدة آلي ومعالجة وضع الطيران والأذونات."),
    ("المرحلة 7", "الإصدار والتوثيق والاعتماد الأكاديمي الشامل", "إصدار APK والتقرير المحكم في 18 صفحة تحت إشراف د. ساهر الهمداني.")
]

y_pos = 1.7
for num, title, desc in pipeline_phases:
    # Phase box
    p_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(y_pos), Inches(11.733), Inches(0.65))
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = CARD_BG
    p_box.line.color.rgb = CYAN_ACCENT if "4" in num or "5" in num else CARD_BORDER
    p_box.line.width = Pt(1.5) if "4" in num or "5" in num else Pt(1.0)
    
    tb = s3.shapes.add_textbox(Inches(1.0), Inches(y_pos + 0.05), Inches(11.333), Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = f"{num} : {title}  |  {desc}"
    p.font.name = FONT_BODY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.RIGHT
    
    y_pos += 0.72

add_footer(s3, 3)

# ==============================================================================
# SLIDE 4: SRS & SYSTEM BOUNDARIES
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, BG_DARK)
add_header(s4, "3. وثيقة مواصفات النظام وحدود العتاد الصارمة (SRS Boundaries)", "المواصفات والحدود الهندسية")

# Card 1: In Scope
create_card(s4, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "داخل النطاق الهندسي (In-Scope)")
tb = s4.shapes.add_textbox(Inches(1.0), Inches(2.5), Inches(3.2), Inches(3.9))
tf = tb.text_frame
tf.word_wrap = True
in_scope = [
    "قراءة نمط الشبكة الفعلي عبر قنوات كوتلن Platform Channel.",
    "استخراج قوة الإشارة الحية بالـ dBm و ASU ونوع التقنية (LTE/HSPA/GSM).",
    "توفير 5 إعدادات مسبقة لشبكات الاتصالات في اليمن (سبأفون، يو، يمن موبايل).",
    "فتح شاشة Phone Info الأصلية بتسلسل Fallback متين في الأجهزة غير المروّتة.",
    "التنفيذ الصامت المباشر لأمر تحويل التردد في الأجهزة المروّتة (Root).",
    "استشعار فوري وتام لوضع الطيران (Airplane Mode) وإطفاء مؤشرات الراديو."
]
for item in in_scope:
    p = tf.add_paragraph()
    p.text = f"✔ {item}"
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.RIGHT

# Card 2: Out of Scope
create_card(s4, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "خارج النطاق الهندسي (Out-of-Scope)")
tb = s4.shapes.add_textbox(Inches(5.0), Inches(2.5), Inches(3.2), Inches(3.9))
tf = tb.text_frame
tf.word_wrap = True
out_scope = [
    "التحكم بترددات شبكات الواي فاي (Wi-Fi) أو البلوتوث نهائياً.",
    "تخطي قيود حماية مصنعي العتاد (Samsung Knox) بدون روت خرقاً للأمان.",
    "إرسال أي إحصائيات عبر الإنترنت (تطبيق أوفلاين 100% لحماية الخصوصية).",
    "تعديل ملفات النظام المحمية بالنواة /system أو كسر حماية IMEI.",
    "إجبار المودم على الاتصال ببرج خلوي يبعد عن النطاق الفيزيائي للتردد."
]
for item in out_scope:
    p = tf.add_paragraph()
    p.text = f"⛔ {item}"
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_MUTED
    p.alignment = PP_ALIGN.RIGHT

# Card 3: OEM Security Wall
create_card(s4, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "جدار الحماية المصنعي (OEM Wall)")
tb = s4.shapes.add_textbox(Inches(9.0), Inches(2.5), Inches(3.3), Inches(3.9))
tf = tb.text_frame
tf.word_wrap = True
oem_points = [
    ("صلاحية MODIFY_PHONE_STATE:", "محمية بنظام أندرويد وتمنح فقط لتطبيقات النظام System Signature Apps."),
    ("قيود Samsung OneUI & Knox:", "حظر التغيير الصامت لمنع حرمان المستخدم من مكالمات الطوارئ 911/112."),
    ("حل NET Mode المبتكر:", "بنية هجينة تجمع بين الروت التلقائي وشاشات الإعدادات العميقة بحزم بديلة متعددة تضمن النجاح 100%.")
]
for title, desc in oem_points:
    p = tf.add_paragraph()
    p.text = f"🔒 {title}\n{desc}\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.RIGHT

add_footer(s4, 4)

# ==============================================================================
# SLIDE 5: MODEL CONTEXT PROTOCOL (MCP)
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, BG_DARK)
add_header(s5, "4. منظومة بروتوكول سياق النموذج المتطورة (Model Context Protocol - MCP)", "حوكمة الذكاء الاصطناعي والأتمتة")

# Card 1: dart-mcp-server
create_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "خادم دمج دارت (dart-mcp-server)")
tb = s5.shapes.add_textbox(Inches(1.0), Inches(2.5), Inches(5.2), Inches(3.9))
tf = tb.text_frame
tf.word_wrap = True
dart_mcp = [
    ("فحص الكود السكوني (Static Analysis):", "استدعاء analyze_files لمسح شجرة الكود واكتشاف أخطاء الأنواع والمخالفات فورياً."),
    ("تشغيل الاختبارات الآلية (Automated Testing):", "تنفيذ run_tests لتشغيل 11 اختبار وحدة والتحقق من اجتيازها 100% آلياً."),
    ("التفتيش البصري للهيكل (Widget Tree):", "فحص عناصر الواجهة وتراكبها عبر get_widget_tree وضمان مطابقتها للمواصفات."),
    ("تشخيص الأخطاء وقت التشغيل (Runtime Diagnostics):", "مراقبة الـ Event Loop واقتناص استثناءات المنصة قبل الوصول للمستخدم.")
]
for title, desc in dart_mcp:
    p = tf.add_paragraph()
    p.text = f"🚀 {title}\n{desc}\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.RIGHT

# Card 2: github-mcp-server
create_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "خادم حوكمة جيت هب (github-mcp-server)")
tb = s5.shapes.add_textbox(Inches(7.0), Inches(2.5), Inches(5.3), Inches(3.9))
tf = tb.text_frame
tf.word_wrap = True
git_mcp = [
    ("إدارة الفروع الملحمية (Branch Automation):", "إنشاء وتتبع فروع العمليات feature branches وفق اتفاقيات التسمية المعتمدة."),
    ("حوكمة طلبات السحب (PR Management):", "إنشاء Pull Requests وربطها برقم الـ Issue ومعايير القبول في كانبان."),
    ("الفحص الآلي للالتزامات (Commit Verification):", "التحقق من سلامة رسائل الالتزام والتوافق مع نظام Semantic Versioning."),
    ("حماية الفرع الرئيسي (Branch Protection):", "منع دمج أي كود في main إلا بعد اجتياز فحص دارت وموافقة المراجع.")
]
for title, desc in git_mcp:
    p = tf.add_paragraph()
    p.text = f"🛡️ {title}\n{desc}\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.RIGHT

add_footer(s5, 5)

# ==============================================================================
# SLIDE 6: KANBAN & TEAM TASK DISTRIBUTION (24 ISSUES)
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, BG_DARK)
add_header(s6, "5. لوحة كانبان وهيكلية توزيع المهام الـ 24 على المهندسين الأربعة", "الإدارة الرشيقة وتوزيع الأدوار")

engineers_data = [
    ("1. م. أحمد الأهدل", "Scrum Master & Docs Lead", "Epic 1: الإعداد والحوكمة", "Issues #1 - #6", [
        "تحميل ودمج المهارات التخصصية (Skills).",
        "صياغة وثيقة الـ SRS الشاملة.",
        "توثيق قصص المستخدمين ومعايير القبول.",
        "كتابة دستور الوكيل الذكي GEMINI.md.",
        "إعداد لوحة كانبان وتدفق Git Workflow.",
        "إعداد التقرير المرجعي وسيناريو المناقشة."
    ]),
    ("2. م. محمد علي / الدعيس", "Core Domain & Architect", "Epic 2: طبقة النطاق والمعمارية", "Issues #7 - #12", [
        "بناء كينونة NetworkMode كود دارت نقي 100%.",
        "بناء كينونة NetworkInfo للبيانات الحية.",
        "صياغة واجهة المستودع NetworkRepository.",
        "تنفيذ حالة الاستخدام GetCurrentModeUseCase.",
        "تنفيذ حالة الاستخدام SetNetworkModeUseCase.",
        "تطبيق اختبارات الوحدة الشاملة للنطاق."
    ]),
    ("3. م. يوسف خيري", "Data & Platform Engineer", "Epic 3: طبقة البيانات والمودم", "Issues #13 - #18", [
        "بناء مصدر البيانات RadioDeviceDataSource.",
        "تنفيذ مستودع NetworkRepositoryImpl.",
        "برمجة قنوات Platform MethodChannel بنواة كوتلن.",
        "استخراج قوة الإشارة عبر TelephonyManager.",
        "بناء خوارزمية السقوط المتعدد Multi-Intent.",
        "حفظ التفضيلات وإدارة أذونات الهاتف."
    ]),
    ("4. م. مؤيد الصوفي", "UI/UX Pro Max Engineer", "Epic 4: الواجهة والحالة التفاعلية", "Issues #19 - #24", [
        "تصميم سمة النيون الفضائية Cyberpunk Navy.",
        "بناء بطاقة المراقبة الحية بـ 5 أعمدة تفاعلية.",
        "تصميم بطاقات الأنماط الخمسة لشبكات اليمن.",
        "دمج مراقب دورة حياة النظام WidgetsBindingObserver.",
        "بناء معالج الأخطاء ودرع وضع الطيران الفوري.",
        "إخراج العرض البصري واختبارات القبول النهائي."
    ])
]

card_w = Inches(2.75)
card_h = Inches(4.8)
start_x = Inches(0.8)

for i, (eng_name, eng_role, epic_name, issues_range, tasks) in enumerate(engineers_data):
    cx = start_x + Inches(i * 2.95)
    create_card(s6, cx, Inches(1.8), card_w, card_h, eng_name)
    
    tb = s6.shapes.add_textbox(cx + Inches(0.15), Inches(2.4), card_w - Inches(0.3), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = f"{eng_role}\n{epic_name} ({issues_range})"
    p.font.name = FONT_HEADING
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.RIGHT
    
    for t in tasks:
        p = tf.add_paragraph()
        p.text = f"• {t}"
        p.font.name = FONT_BODY
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.RIGHT

add_footer(s6, 6)

# ==============================================================================
# SLIDE 7: CLEAN ARCHITECTURE & SOLID PRINCIPLES
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, BG_DARK)
add_header(s7, "6. المعمارية البرمجية النظيفة ومبادئ SOLID الهندسية", "الهندسة المعمارية واستقلالية النطاق")

layers = [
    ("طبقة العرض والواجهات (Presentation Layer)", "Flutter UI & State Management", 
     "تحتوي على Widgets و Controllers وتطبق نمط UI/UX Pro Max وتعتمد كلياً على حالات الاستخدام دون معرفة تفاصيل المودم.", RGBColor(14, 165, 233)),
    ("طبقة النطاق ومنطق الأعمال (Domain Layer - Pure Dart)", "Enterprise Business Rules", 
     "قلب المشروع الخالي 100% من أي استيراد لـ Flutter أو مكتبات أندرويد. تضم الكيانات غير القابلة للتعديل والـ Use Cases وواجهات المستودعات المجرّدة.", RGBColor(16, 185, 129)),
    ("طبقة البيانات والاتصال بالمنصة (Data Layer)", "Repositories & Platform Channels", 
     "تنفذ واجهات المستودعات، وتحتوي على مصدر البيانات RadioDeviceDataSource، وقنوات الاتصال MethodChannel مع نظام أندرويد.", RGBColor(245, 158, 11))
]

y_layer = 1.8
for title, sub, desc, col in layers:
    box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(y_layer), Inches(11.733), Inches(1.35))
    box.fill.solid()
    box.fill.fore_color.rgb = CARD_BG
    box.line.color.rgb = col
    box.line.width = Pt(2.0)
    
    tb = s7.shapes.add_textbox(Inches(1.0), Inches(y_layer + 0.1), Inches(11.333), Inches(1.15))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = f"{title}  —  [{sub}]"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = col
    p.alignment = PP_ALIGN.RIGHT
    
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.name = FONT_BODY
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = TEXT_WHITE
    p2.alignment = PP_ALIGN.RIGHT
    
    y_layer += 1.5

# Bottom summary box for SOLID
create_card(s7, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.65), bg_color=RGBColor(15, 23, 42))
tb = s7.shapes.add_textbox(Inches(1.0), Inches(6.35), Inches(11.333), Inches(0.55))
tf = tb.text_frame
p = tf.paragraphs[0]
p.text = "مبادئ SOLID المطبقة: استقلالية المسؤولية (SRP) | الانفتاح للتوسيع (OCP) | فصل الواجهات (ISP) | عكس التبعيات (DIP) عبر Mocking و Repositories"
p.font.name = FONT_BODY
p.font.size = Pt(9.5)
p.font.bold = True
p.font.color.rgb = CYAN_ACCENT
p.alignment = PP_ALIGN.CENTER

add_footer(s7, 7)

# ==============================================================================
# SLIDE 8: NATIVE KOTLIN RADIO ENGINE
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, BG_DARK)
add_header(s8, "7. هندسة الاتصال العميق بالمودم ونواة كوتلن الأصلية (Native Kotlin Engine)", "البرمجة المنخفضة ونواة أندرويد")

# Left: Code & Architecture
create_card(s8, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.8), "خوارزمية السقوط المتعدد (Multi-Intent Fallback)")
tb = s8.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(5.3), Inches(4.0))
tf = tb.text_frame
tf.word_wrap = True

code_steps = [
    ("قناة الاتصال الثنائية MethodChannel:", "اسم القناة 'com.netmode.app/radio' لنقل أوامر المودم وحالات الشبكة بشكل غير متزامن بدون تجميد للواجهة."),
    ("سلسلة الحزم المستهدفة (Fallback Targets):", "1. com.android.phone.settings.RadioInfo\n2. com.android.settings.RadioInfo\n3. com.android.settings.TestingSettings\n4. Settings.ACTION_DATA_ROAMING_SETTINGS"),
    ("معالجة الاستثناءات الدفاعية:", "فحص كل Intent بحماية try-catch مع إضافة راية Intent.FLAG_ACTIVITY_NEW_TASK لضمان عدم توقف التطبيق أبداً عند رفض الحزمة.")
]
for title, desc in code_steps:
    p = tf.add_paragraph()
    p.text = f"⚙️ {title}\n{desc}\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.RIGHT

# Right: TelephonyManager & Root
create_card(s8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "استخراج الإشارة والتحكم المزدوج (Hybrid Execution)")
tb = s8.shapes.add_textbox(Inches(7.0), Inches(2.4), Inches(5.3), Inches(4.0))
tf = tb.text_frame
tf.word_wrap = True

telephony_points = [
    ("استخراج الإشارة عبر TelephonyManager:", "التوافق مع أندرويد 8 حتى 14+ باستخراج cellSignalStrengths وقيم dBm و ASU ومستوى الإشارة من 0 إلى 4 بدقة متناهية."),
    ("المسار الصامت للهواتف المروّتة (Root Path):", "تنفيذ أمر الشل الفوري بصلاحيات الروت الخارقة:\n`su -c cmd phone set-preferred-network-type [CODE]`\nلتغيير التردد بلمسة واحدة دون تدخل المستخدم."),
    ("مسار الهواتف القياسية (Standard Path):", "القفز التلقائي المباشر لنافذة Phone info الأصلية وإرشاد المستخدم للنمط المطابق لاختياره بنقرة واحدة.")
]
for title, desc in telephony_points:
    p = tf.add_paragraph()
    p.text = f"📡 {title}\n{desc}\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.RIGHT

add_footer(s8, 8)

# ==============================================================================
# SLIDE 9: UI/UX PRO MAX & SCREEN SHOWCASE
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, BG_DARK)
add_header(s9, "8. التجربة البصرية المتقدمة وشاشات النظام الواقعية (UI/UX Showcase)", "واجهات المستخدم التفاعلية")

# 3 Images side by side
img_w = Inches(2.4)
img_h = Inches(4.8)

# Screen 1: App Main
if os.path.exists(app_screen):
    s9.shapes.add_picture(app_screen, Inches(1.2), Inches(1.8), width=img_w)
create_card(s9, Inches(0.9), Inches(6.1), Inches(3.0), Inches(0.7), bg_color=CARD_BG)
tb = s9.shapes.add_textbox(Inches(0.9), Inches(6.15), Inches(3.0), Inches(0.6))
p = tb.text_frame.paragraphs[0]
p.text = "واجهة التطبيق الرئيسية (5G/4G)"
p.font.name = FONT_HEADING
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = CYAN_ACCENT
p.alignment = PP_ALIGN.CENTER

# Screen 2: Device Phone Info
if os.path.exists(device_screen):
    s9.shapes.add_picture(device_screen, Inches(5.4), Inches(1.8), width=img_w)
create_card(s9, Inches(5.1), Inches(6.1), Inches(3.0), Inches(0.7), bg_color=CARD_BG)
tb = s9.shapes.add_textbox(Inches(5.1), Inches(6.15), Inches(3.0), Inches(0.6))
p = tb.text_frame.paragraphs[0]
p.text = "نافذة Phone info الأصلية"
p.font.name = FONT_HEADING
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = GREEN_SUCCESS
p.alignment = PP_ALIGN.CENTER

# Screen 3: Airplane Mode
if os.path.exists(airplane_screen):
    s9.shapes.add_picture(airplane_screen, Inches(9.6), Inches(1.8), width=img_w)
create_card(s9, Inches(9.3), Inches(6.1), Inches(3.0), Inches(0.7), bg_color=CARD_BG)
tb = s9.shapes.add_textbox(Inches(9.3), Inches(6.15), Inches(3.0), Inches(0.6))
p = tb.text_frame.paragraphs[0]
p.text = "درع وضع الطيران التفاعلي"
p.font.name = FONT_HEADING
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = RGBColor(239, 68, 68)
p.alignment = PP_ALIGN.CENTER

add_footer(s9, 9)

# ==============================================================================
# SLIDE 10: AUTOMATED TESTING & DEFENSIVE DESIGN
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, BG_DARK)
add_header(s10, "9. مصفوفة التحقق الآلي والتصميم الدفاعي الصارم (Quality Assurance)", "ضمان الجودة ومقاومة الأخطاء")

# Card 1: Automated Unit Tests
create_card(s10, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.8), "مصفوفة اختبارات الوحدة الآلية (11/11 نجاح)")
tb = s10.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(5.3), Inches(4.0))
tf = tb.text_frame
tf.word_wrap = True

tests = [
    ("NetworkMode Entity Tests:", "التحقق من صحة تعريفات الأنماط والأكواد والعزل التام."),
    ("NetworkInfo Validation Tests:", "التحقق من صحة حقول قوة الإشارة ونوع التقنية وبطاقة SIM."),
    ("GetCurrentModeUseCase Tests:", "اختبار استرجاع النمط الفعلي عبر المستودع الوهمي Mock."),
    ("SetNetworkModeUseCase Tests:", "اختبار تمرير أوامر التغيير بنجاح والتحقق من الاستجابة."),
    ("Repository Isolation Tests:", "عزل طبقة النطاق بنسبة 100% عن قنوات المنصة وتأكيد سلامة العقود.")
]
for title, desc in tests:
    p = tf.add_paragraph()
    p.text = f"✅ {title} {desc}"
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.RIGHT

# Card 2: Defensive Design
create_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "أنماط التصميم الدفاعي (Defensive Architecture)")
tb = s10.shapes.add_textbox(Inches(7.0), Inches(2.4), Inches(5.3), Inches(4.0))
tf = tb.text_frame
tf.word_wrap = True

defensive = [
    ("درع وضع الطيران (Airplane Mode Shield):", "الاستشعار التلقائي الفوري عبر Broadcast Receiver وإطفاء أعمدة الإشارة لمنع إرباك المستخدم أو إرسال أوامر فاشلة."),
    ("حارس الأذونات (Permission Guard):", "فحص إذن READ_PHONE_STATE وعرض بطاقة توجيهية فورية عند فقدان الإذن دون انهيار التطبيق."),
    ("التحكم بحياة التطبيق (WidgetsBindingObserver):", "المزامنة الذاتية الفورية للبيانات بمجرد عودة المستخدم من إعدادات النظام بدون الحاجة للنقر على أي زر."),
    ("التوافق العتادي المتعدد:", "التعامل الآمن مع الهواتف ثنائية الشريحة (Dual SIM) والمعالجات المختلفة (MediaTek/Qualcomm).")
]
for title, desc in defensive:
    p = tf.add_paragraph()
    p.text = f"🛡️ {title}\n{desc}\n"
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.RIGHT

add_footer(s10, 10)

# ==============================================================================
# SLIDE 11: KEY ENGINEERING METRICS & ACHIEVEMENTS
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11, BG_DARK)
add_header(s11, "10. مصفوفة الإنجاز ومؤشرات الجودة البرمجية المكتملة", "مخرجات المشروع ومؤشرات الأداء")

stat_boxes = [
    ("24 / 24", "مهمة كانبان مكتملة (100%)", "توزيع دقيق عبر Trello على المهندسين الأربعة بمحددات DoD.", GREEN_SUCCESS),
    ("11 / 11", "اختبارات وحدة آلية ناجحة", "تغطية كاملة لطبقة النطاق وحالات الاستخدام دون أي تحذير Lint.", CYAN_ACCENT),
    ("100% Offline", "خصوصية وأمان تام", "صفر طلبات خارجية، وعزل كامل لبيانات المودم محلياً.", PURPLE_ACCENT),
    ("5 أنماط مخصصة", "لشبكات الاتصالات باليمن", "دعم سبأفون، يو (YOU)، ويمن موبايل (VoLTE/4G).", BLUE_PRIMARY),
    ("18 صفحة محكّمة", "وثيقة هندسة البرمجيات الكبرى", "تقرير شامل ومفصل بالملي معتمد للنشر الأكاديمي.", GREEN_SUCCESS),
    ("Zero Flutter Import", "في طبقة الـ Domain", "نقاء معماري تام متوافق مع دستور المشروع GEMINI.md.", CYAN_ACCENT)
]

coords = [
    (0.8, 1.8), (4.8, 1.8), (8.8, 1.8),
    (0.8, 4.3), (4.8, 4.3), (8.8, 4.3)
]

for i, (val, title, desc, col) in enumerate(stat_boxes):
    x, y = coords[i]
    box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(3.7), Inches(2.2))
    box.fill.solid()
    box.fill.fore_color.rgb = CARD_BG
    box.line.color.rgb = col
    box.line.width = Pt(1.5)
    
    tb = s11.shapes.add_textbox(Inches(x + 0.15), Inches(y + 0.15), Inches(3.4), Inches(1.9))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = val
    p.font.name = FONT_HEADING
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = col
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf.add_paragraph()
    p2.text = title
    p2.font.name = FONT_HEADING
    p2.font.size = Pt(12)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.alignment = PP_ALIGN.CENTER
    
    p3 = tf.add_paragraph()
    p3.text = desc
    p3.font.name = FONT_BODY
    p3.font.size = Pt(9.5)
    p3.font.color.rgb = TEXT_MUTED
    p3.alignment = PP_ALIGN.CENTER

add_footer(s11, 11)

# ==============================================================================
# SLIDE 12: CONCLUSION & DEFENSE SALUTE
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12, BG_DARK)

# Main Conclusion Card
create_card(s12, Inches(1.5), Inches(1.0), Inches(10.333), Inches(5.4), "خاتمة الدفاع ومناقشة مشروع التخرج", border_color=CYAN_ACCENT)
tb = s12.shapes.add_textbox(Inches(1.8), Inches(1.8), Inches(9.733), Inches(4.3))
tf = tb.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "مشروع NET Mode: نموذج هندسي متكامل لهندسة البرمجيات المتقدمة"
p.font.name = FONT_HEADING
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = CYAN_ACCENT
p.alignment = PP_ALIGN.CENTER

p = tf.add_paragraph()
p.text = "استطعنا بنجاح تحويل مشكلة معقدة في عتاد الهواتف إلى حل برمجي عالي الاستقرار، مطبقين أعلى معايير هندسة البرمجيات العالمية، من التحليل الرشيق وتفكيك المهام عبر كانبان، إلى المعمارية النظيفة وحوكمة الذكاء الاصطناعي ببروتوكول MCP، مع الالتزام التام بالتصميم الدفاعي ومقاومة الانهيار."
p.font.name = FONT_BODY
p.font.size = Pt(12.5)
p.font.color.rgb = TEXT_WHITE
p.alignment = PP_ALIGN.CENTER

p = tf.add_paragraph()
p.text = "\nخالص الشكر والتقدير للأستاذ المشرف:"
p.font.name = FONT_BODY
p.font.size = Pt(13)
p.font.color.rgb = TEXT_MUTED
p.alignment = PP_ALIGN.CENTER

p = tf.add_paragraph()
p.text = "د.م. ساهر الهمداني"
p.font.name = FONT_HEADING
p.font.size = Pt(26)
p.font.bold = True
p.font.color.rgb = GREEN_SUCCESS
p.alignment = PP_ALIGN.CENTER

p = tf.add_paragraph()
p.text = "على دعمه وتوجيهاته القيمة التي مكنتنا من إنجاز هذا العمل على أعلى مستوى احترافي."
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.color.rgb = TEXT_MUTED
p.alignment = PP_ALIGN.CENTER

p = tf.add_paragraph()
p.text = "\nباب الاستفسارات والمناقشة مفتوح أمام لجنة التحكيم الموقرة 🎓"
p.font.name = FONT_HEADING
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = CYAN_ACCENT
p.alignment = PP_ALIGN.CENTER

add_footer(s12, 12)

# Save presentation
prs.save(pptx_path)
print("PowerPoint presentation generated successfully at:", pptx_path)
print("File size in bytes:", os.path.getsize(pptx_path))
