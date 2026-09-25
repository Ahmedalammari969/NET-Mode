# -*- coding: utf-8 -*-
"""
NET Mode - Interactive Ultra-Modern HTML5 Presentation Deck
Includes:
- Dynamic Canvas Particle / Constellation Network Background
- Custom Theme and Ambient Lighting per Slide Topic
- Animated SVG Interactive Architecture & Pipeline Diagrams
- High-Resolution Base64 Embedded Real App Screenshots
- Keyboard Controls (Arrows, Space, F for Fullscreen, O for Overview, N for Notes)
- Speaker Notes for All 4 Engineers
- Supervised by: Dr. Saher Al-Hamdani
"""

import os
import base64

workspace_dir = r"D:\FOR\A\eng\NET Mode\NET Mode"
html_deck_path = os.path.join(workspace_dir, "NET_Mode_Interactive_Presentation.html")

app_screen_path = os.path.join(workspace_dir, "img", "app_screen.png")
device_screen_path = os.path.join(workspace_dir, "img", "device_screen.png")
airplane_screen_path = os.path.join(workspace_dir, "img", "screen_airplane.png")

with open(app_screen_path, "rb") as f:
    app_screen_b64 = base64.b64encode(f.read()).decode("utf-8")

with open(device_screen_path, "rb") as f:
    device_screen_b64 = base64.b64encode(f.read()).decode("utf-8")

with open(airplane_screen_path, "rb") as f:
    airplane_screen_b64 = base64.b64encode(f.read()).decode("utf-8")

html_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NET Mode - العرض التقديمي الهندسي لمشروع التخرج</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@300;400;500;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-deep: #070B14;
            --bg-card: rgba(15, 23, 42, 0.75);
            --border-glow: rgba(0, 240, 255, 0.3);
            --cyan: #00F0FF;
            --cyan-glow: rgba(0, 240, 255, 0.4);
            --blue: #0284C7;
            --purple: #8B5CF6;
            --green: #10B981;
            --amber: #F59E0B;
            --red: #EF4444;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
        }

        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: 'Tajawal', sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Dynamic Canvas Background */
        #networkCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            pointer-events: none;
        }

        /* Presentation Container (16:9 Aspect Ratio) */
        .presentation-deck {
            position: relative;
            z-index: 2;
            width: 96vw;
            height: 54vw; /* 16:9 */
            max-height: 94vh;
            max-width: 167vh; /* 16:9 */
            background: radial-gradient(circle at 50% 20%, rgba(14, 165, 233, 0.08) 0%, rgba(7, 11, 20, 0.85) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 0 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 240, 255, 0.15);
            border-radius: 20px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            backdrop-filter: blur(20px);
        }

        /* Top Progress Bar */
        .progress-bar-container {
            width: 100%;
            height: 5px;
            background: rgba(255, 255, 255, 0.05);
            position: relative;
        }
        .progress-bar-fill {
            height: 100%;
            width: 8.33%;
            background: linear-gradient(90deg, var(--cyan), var(--purple));
            box-shadow: 0 0 12px var(--cyan);
            transition: width 0.4s ease;
        }

        /* Top Navigation & Status Bar */
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 24px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.07);
            font-size: 13px;
        }
        .top-brand {
            display: flex;
            align-items: center;
            gap: 10px;
            font-family: 'Cairo', sans-serif;
            font-weight: 800;
            color: var(--cyan);
            letter-spacing: 0.5px;
        }
        .badge-pulse {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--green);
            box-shadow: 0 0 10px var(--green);
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(0.9); opacity: 0.7; }
            50% { transform: scale(1.3); opacity: 1; box-shadow: 0 0 15px var(--green); }
            100% { transform: scale(0.9); opacity: 0.7; }
        }

        .top-meta {
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .top-controls {
            display: flex;
            gap: 8px;
        }
        .ctrl-btn {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 5px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-family: 'Tajawal', sans-serif;
            font-size: 12px;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .ctrl-btn:hover {
            background: rgba(0, 240, 255, 0.2);
            border-color: var(--cyan);
            color: #fff;
            box-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
        }

        /* Slide Viewport */
        .slides-viewport {
            flex: 1;
            position: relative;
            overflow: hidden;
        }

        .slide-item {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            padding: 24px 36px;
            opacity: 0;
            visibility: hidden;
            transform: translateX(40px) scale(0.98);
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }

        .slide-item.active {
            opacity: 1;
            visibility: visible;
            transform: translateX(0) scale(1);
        }

        /* Slide Header */
        .slide-header {
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 12px;
        }
        .slide-category {
            font-size: 13px;
            color: var(--cyan);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .slide-title {
            font-family: 'Cairo', sans-serif;
            font-size: 26px;
            font-weight: 800;
            color: #fff;
            margin-top: 4px;
        }
        .slide-number-badge {
            font-family: 'JetBrains Mono', monospace;
            font-size: 14px;
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid var(--border-glow);
            color: var(--cyan);
            padding: 4px 10px;
            border-radius: 6px;
        }

        /* Slide Grid Layouts */
        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            flex: 1;
        }
        .grid-3 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 18px;
            flex: 1;
        }
        .grid-4 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr;
            gap: 15px;
            flex: 1;
        }

        /* Glassmorphic Cards */
        .glass-card {
            background: var(--bg-card);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
            transition: all 0.3s ease;
        }
        .glass-card:hover {
            border-color: var(--cyan);
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(0, 240, 255, 0.15);
        }
        .glass-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--cyan), transparent);
            opacity: 0.5;
        }

        .card-title {
            font-family: 'Cairo', sans-serif;
            font-size: 16px;
            font-weight: 700;
            color: var(--cyan);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Pipeline Steps */
        .pipeline-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
            flex: 1;
        }
        .pipeline-step {
            display: flex;
            align-items: center;
            gap: 14px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 10px 16px;
            transition: all 0.25s ease;
        }
        .pipeline-step:hover {
            border-color: var(--cyan);
            background: rgba(0, 240, 255, 0.05);
            transform: translateX(-5px);
        }
        .step-num {
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            font-weight: 700;
            background: var(--blue);
            color: #fff;
            padding: 4px 10px;
            border-radius: 6px;
            box-shadow: 0 0 10px rgba(2, 132, 199, 0.5);
        }
        .step-info {
            flex: 1;
        }
        .step-info h4 {
            font-size: 14px;
            color: #fff;
            margin-bottom: 2px;
        }
        .step-info p {
            font-size: 12px;
            color: var(--text-muted);
        }

        /* Clean Architecture Layers */
        .arch-layer {
            border-radius: 12px;
            padding: 14px 18px;
            margin-bottom: 12px;
            border: 1px solid;
            background: rgba(15, 23, 42, 0.7);
            position: relative;
            transition: all 0.3s;
        }
        .arch-layer:hover {
            transform: scale(1.01);
        }
        .arch-layer.presentation {
            border-color: #38BDF8;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.15);
        }
        .arch-layer.domain {
            border-color: #34D399;
            box-shadow: 0 0 15px rgba(52, 211, 153, 0.15);
        }
        .arch-layer.data {
            border-color: #FBBF24;
            box-shadow: 0 0 15px rgba(251, 191, 36, 0.15);
        }

        /* Screen Mockups */
        .screens-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 25px;
            flex: 1;
            padding-bottom: 10px;
        }
        .mockup-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }
        .mockup-frame {
            height: 380px;
            border-radius: 18px;
            border: 2px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7), 0 0 20px rgba(0, 240, 255, 0.2);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .mockup-frame:hover {
            transform: scale(1.05);
            border-color: var(--cyan);
            box-shadow: 0 15px 40px rgba(0, 240, 255, 0.4);
        }
        .mockup-caption {
            font-size: 13px;
            font-weight: 700;
            color: var(--cyan);
        }

        /* Key Metrics Grid */
        .metric-card {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 18px;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            transition: all 0.3s ease;
        }
        .metric-card:hover {
            border-color: var(--cyan);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.25);
            transform: translateY(-4px);
        }
        .metric-val {
            font-family: 'JetBrains Mono', monospace;
            font-size: 38px;
            font-weight: 800;
            color: var(--cyan);
            text-shadow: 0 0 15px rgba(0, 240, 255, 0.5);
            margin-bottom: 6px;
        }
        .metric-label {
            font-family: 'Cairo', sans-serif;
            font-size: 15px;
            font-weight: 700;
            color: #fff;
            margin-bottom: 4px;
        }
        .metric-desc {
            font-size: 12px;
            color: var(--text-muted);
        }

        /* Bottom Status & Key Hints */
        .bottom-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 24px;
            border-top: 1px solid rgba(255, 255, 255, 0.07);
            font-size: 12px;
            color: var(--text-muted);
        }
        .keyboard-hints {
            display: flex;
            gap: 12px;
        }
        .key-tag {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 2px 7px;
            border-radius: 5px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: #fff;
        }

        /* Speaker Notes Modal */
        #notesModal {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 420px;
            background: rgba(10, 15, 29, 0.95);
            border: 1px solid var(--cyan);
            border-radius: 12px;
            padding: 16px;
            z-index: 100;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8), 0 0 20px rgba(0, 240, 255, 0.3);
            display: none;
            backdrop-filter: blur(15px);
        }
        #notesModal.visible { display: block; }
        .notes-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 6px;
            font-family: 'Cairo', sans-serif;
            font-size: 14px;
            font-weight: 700;
            color: var(--cyan);
        }

        /* Overview Grid Overlay */
        #overviewGrid {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(7, 11, 20, 0.96);
            z-index: 200;
            display: none;
            padding: 40px;
            overflow-y: auto;
            backdrop-filter: blur(25px);
        }
        #overviewGrid.visible { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
        .overview-thumb {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 10px;
            padding: 14px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .overview-thumb:hover {
            border-color: var(--cyan);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.3);
            transform: scale(1.02);
        }
        .overview-thumb.current {
            border-color: var(--green);
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
        }

        /* Cover Specific */
        .cover-box {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%;
            text-align: center;
        }
        .cover-badge {
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid var(--cyan);
            color: var(--cyan);
            padding: 6px 18px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 15px;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.2);
        }
        .cover-title {
            font-family: 'Cairo', sans-serif;
            font-size: 58px;
            font-weight: 900;
            background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 60%, #0284C7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 1px;
            margin-bottom: 6px;
        }
        .cover-sub {
            font-family: 'Cairo', sans-serif;
            font-size: 22px;
            font-weight: 700;
            color: var(--cyan);
            margin-bottom: 10px;
        }
        .cover-desc {
            font-size: 15px;
            color: var(--text-muted);
            max-width: 750px;
            line-height: 1.6;
            margin-bottom: 25px;
        }
        .cover-cards-row {
            display: flex;
            gap: 20px;
            width: 100%;
            max-width: 900px;
        }

        /* Pulse and Animations */
        @keyframes floatSlow {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-6px); }
            100% { transform: translateY(0px); }
        }
        .float-elem { animation: floatSlow 4s ease-in-out infinite; }
    </style>
</head>
<body>

    <!-- Particle Background -->
    <canvas id="networkCanvas"></canvas>

    <!-- Main Presentation 16:9 Deck -->
    <div class="presentation-deck">
        <!-- Progress Bar -->
        <div class="progress-bar-container">
            <div class="progress-bar-fill" id="progressBar"></div>
        </div>

        <!-- Top Bar -->
        <div class="top-bar">
            <div class="top-brand">
                <span class="badge-pulse"></span>
                <span>NET Mode — Suite v2.0</span>
            </div>
            <div class="top-meta">
                <span>إشراف الأستاذ المشرف: <b>د.م. ساهر الهمداني</b></span>
                <span>|</span>
                <span id="slideIndicator">الشريحة 1 من 12</span>
            </div>
            <div class="top-controls">
                <button class="ctrl-btn" onclick="toggleOverview()" title="عرض كل الشرائح (O)">📋 الفهرس</button>
                <button class="ctrl-btn" onclick="toggleNotes()" title="ملاحظات المتحدث (N)">🎙️ المتحدث</button>
                <button class="ctrl-btn" onclick="toggleFullscreen()" title="ملء الشاشة (F)">⛶ تكبير</button>
            </div>
        </div>

        <!-- Viewport -->
        <div class="slides-viewport">

            <!-- SLIDE 1: COVER -->
            <div class="slide-item active" data-slide="1" data-notes="أهلاً بكم دكاترتنا الأفاضل. اليوم نقدم لكم مشروع تخرجنا NET Mode، وهو حل برمجي هندسي لمعضلة تشتت واجهات المودم في أندرويد وتثبيت ترددات 4G/LTE، طبقنا فيه أعلى معايير هندسة البرمجيات وأتمتة الذكاء الاصطناعي بروتوكول MCP والمعمارية النظيفة تحت إشراف الدكتور ساهر الهمداني.">
                <div class="cover-box">
                    <div class="cover-badge float-elem">مشروع تخرج محكّم | Advanced Software Engineering 2026</div>
                    <div class="cover-title">NET Mode</div>
                    <div class="cover-sub">Advanced Cellular Network & Radio Testing Suite</div>
                    <div class="cover-desc">
                        منظومة فحص وإدارة ترددات الشبكات الخلوية للأجهزة الذكية وفق معمارية Clean Architecture، ودستور الحوكمة الصارم، وتكامل بروتوكول سياق النموذج (MCP).
                    </div>
                    <div class="cover-cards-row">
                        <div class="glass-card" style="flex: 1; text-align: right;">
                            <div class="card-title">👥 فريق العمل الهندسي (Team Alpha)</div>
                            <p style="font-size: 13px; line-height: 1.8;">
                                <b>1. أحمد الأهدل</b> — Scrum Master & Docs Lead<br>
                                <b>2. محمد علي / الدعيس</b> — Core Domain & Architect<br>
                                <b>3. يوسف خيري</b> — Data Layer & Platform Engineer<br>
                                <b>4. مؤيد الصوفي</b> — UI/UX & Presentation State
                            </p>
                        </div>
                        <div class="glass-card" style="flex: 1; text-align: right; border-color: rgba(16, 185, 129, 0.4);">
                            <div class="card-title" style="color: var(--green);">🎓 الإشراف الأكاديمي والتقنيات</div>
                            <p style="font-size: 14px; margin-bottom: 8px;">
                                إشراف الأستاذ المشرف:<br>
                                <b style="font-size: 18px; color: var(--green);">د.م. ساهر الهمداني</b>
                            </p>
                            <p style="font-size: 12px; color: var(--cyan);">
                                Flutter 3.x • Kotlin Native • Clean Architecture • Dart & GitHub MCP Servers
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SLIDE 2: PROBLEM STATEMENT -->
            <div class="slide-item" data-slide="2" data-notes="المشكلة التي حركتنا هي أن شركات مثل سامسونج وشاومي تخفي خيارات قفل التردد بأكواد سرية مثل نجمة مربع نجمة مربع 4636 مربع نجمة مربع نجمة التي حظرتها أندرويد 11 فما فوق. التطبيق يقدم حلاً يمنياً متخصصاً يقفل التردد ويوفر 35% من استهلاك البطارية.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">📍 المشكلة والدوافع الهندسية</div>
                        <div class="slide-title">التحديات الواقعية، الدوافع، والرؤية الابتكارية للمشروع</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 02</div>
                </div>
                <div class="grid-3">
                    <div class="glass-card" style="border-top: 3px solid var(--red);">
                        <div class="card-title" style="color: var(--red);">❌ المعضلة التقنية والتشتت</div>
                        <ul style="font-size: 13px; line-height: 1.9; color: var(--text-muted); list-style: none;">
                            <li>• <b>حظر الأكواد السرية:</b> إغلاق منافذ <code>*#*#4636#*#*</code> في أندرويد الحديث.</li>
                            <li>• <b>سقوط الشبكة التلقائي:</b> الانحدار من 4G إلى 3G/2G في مناطق التغطية الضعيفة باليمن.</li>
                            <li>• <b>تشتت الشركات:</b> اختلاف جذري بين سامسونج وشاومي وميدياتك وكوالكوم.</li>
                            <li>• <b>استنزاف البطارية:</b> البحث العشوائي المتواصل للمودم يرفع حرارة الهاتف.</li>
                        </ul>
                    </div>
                    <div class="glass-card" style="border-top: 3px solid var(--cyan);">
                        <div class="card-title">💡 الحل الهندسي (NET Mode)</div>
                        <ul style="font-size: 13px; line-height: 1.9; color: #fff; list-style: none;">
                            <li>• <b>تثبيت التردد الإجباري (Lock):</b> حظر السقوط لشبكات الجيل القديم إطلاقاً.</li>
                            <li>• <b>تخصيص كامل لليمن:</b> أوضاع محددة لـ (سبأفون، يو، يمن موبايل VoLTE).</li>
                            <li>• <b>أوفلاين 100%:</b> حماية خصوصية المستخدم بدون أي اتصال خارجي.</li>
                            <li>• <b>استراتيجية القفز الهجين:</b> التوافق التام مع الأجهزة المروّتة وغير المروّتة.</li>
                        </ul>
                    </div>
                    <div class="glass-card" style="border-top: 3px solid var(--green);">
                        <div class="card-title" style="color: var(--green);">💎 المعايير القياسية المستهدفة</div>
                        <ul style="font-size: 13px; line-height: 1.9; color: var(--cyan); list-style: none;">
                            <li>• <b>سرعة الاستجابة:</b> أقل من 50ms لنقل الأوامر عبر المنصة.</li>
                            <li>• <b>توفير الطاقة:</b> خفض حتى 35% في هدر طاقة بطاقة الراديو.</li>
                            <li>• <b>تغطية الاختبارات:</b> 100% اختبارات مؤتمتة لمنطق الأعمال.</li>
                            <li>• <b>صفر تحذيرات Lint:</b> كود نقي خاضع لمعايير التحليل الصارم.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- SLIDE 3: MASTER WORKFLOW PIPELINE -->
            <div class="slide-item" data-slide="3" data-notes="هنا يظهر التزامنا بأعلى معايير هندسة البرمجيات عبر خط الأنابيب المكون من 7 مراحل متتالية: بدأنا بالمهارات ودستور المشروع، ثم تفكيك كانبان لـ 24 مهمة، وتكامل خوادم MCP، ثم تنفيذ المعمارية النظيفة والاختبارات حتى الإصدار النهائي.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">🔄 دورة حياة التطوير</div>
                        <div class="slide-title">خط أنابيب هندسة البرمجيات الشامل (7-Phase Master Workflow Pipeline)</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 03</div>
                </div>
                <div class="pipeline-list">
                    <div class="pipeline-step">
                        <span class="step-num">PHASE 1</span>
                        <div class="step-info">
                            <h4>تجهيز بيئة الوكيل الذكي والمهارات (Skills Setup)</h4>
                            <p>تحميل وتفعيل المهارات التخصصية (ui-ux-pro-max, dart-add-unit-test, flutter-apply-architecture) وحوكمة الذكاء الاصطناعي.</p>
                        </div>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-num">PHASE 2</span>
                        <div class="step-info">
                            <h4>صياغة دستور المشروع والقيود المعمارية (GEMINI.md)</h4>
                            <p>إقرار مبادئ Clean Architecture و SOLID وعزل طبقة النطاق تماماً ومنع أي استيراد لـ Flutter أو أندرويد داخلها.</p>
                        </div>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-num">PHASE 3</span>
                        <div class="step-info">
                            <h4>تفكيك كانبان وتوزيع المهام الـ 24 عبر Trello</h4>
                            <p>تقسيم المشروع إلى 4 مسارات ملحمية (Epics) وتوزيعها على المهندسين الأربعة بمحددات إنجاز صارمة (DoD).</p>
                        </div>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-num" style="background: var(--purple);">PHASE 4</span>
                        <div class="step-info">
                            <h4>تكامل بروتوكول سياق النموذج (MCP Servers Integration)</h4>
                            <p>ربط الوكيل البرمجي بخادمي dart-mcp-server و github-mcp-server للفحص السكوني وإدارة الفروع وحوكمة الجودة.</p>
                        </div>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-num" style="background: var(--green);">PHASE 5</span>
                        <div class="step-info">
                            <h4>تنفيذ المعمارية النظيفة وقنوات المنصة (Clean Architecture & Native)</h4>
                            <p>بناء طبقات Domain و Data و Presentation وبرمجة نواة كوتلن الأصلية MethodChannel للتواصل المباشر مع المودم.</p>
                        </div>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-num">PHASE 6</span>
                        <div class="step-info">
                            <h4>الاختبارات الآلية والتصميم الدفاعي (Automated Testing & Defensive Design)</h4>
                            <p>تنفيذ 11 اختبار وحدة آلي بنجاح 100%، وحصانة التطبيق ضد فقدان الأذونات ووضع الطيران.</p>
                        </div>
                    </div>
                    <div class="pipeline-step">
                        <span class="step-num" style="background: var(--cyan); color: #000;">PHASE 7</span>
                        <div class="step-info">
                            <h4>الإصدار والتوثيق والاعتماد الأكاديمي الشامل (Release & Master Docs)</h4>
                            <p>توليد تقرير هندسة البرمجيات المحكّم في 18 صفحة، والملف العرضي المتقدم تحت إشراف د. ساهر الهمداني.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SLIDE 4: SRS BOUNDARIES -->
            <div class="slide-item" data-slide="4" data-notes="في وثيقة الـ SRS ركزنا بدقة على الحدود الهندسية: ما يدخل في النطاق وما يخرج منه. كما وضحنا جدار الحماية المصنعي في سامسونج ونظام أندرويد الذي يحظر صلاحية MODIFY_PHONE_STATE على التطبيقات العادية لحماية مكالمات الطوارئ، وكيف واجهنا ذلك باستراتيجية مزدوجة.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">📋 المواصفات والحدود</div>
                        <div class="slide-title">وثيقة متطلبات النظام والحدود العتادية الصارمة (SRS Boundaries)</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 04</div>
                </div>
                <div class="grid-3">
                    <div class="glass-card" style="border-top: 3px solid var(--green);">
                        <div class="card-title" style="color: var(--green);">✔ داخل النطاق (In-Scope)</div>
                        <ul style="font-size: 13px; line-height: 1.8; color: #fff; list-style: none;">
                            <li>• قراءة نمط الشبكة الفعلي عبر قنوات كوتلن.</li>
                            <li>• استخراج قوة الإشارة الحية بالـ dBm و ASU ونوع التقنية.</li>
                            <li>• 5 إعدادات مسبقة متوافقة مع شبكات الاتصال باليمن.</li>
                            <li>• خوارزمية Fallback متعددة لحزم شاشات الاختبار.</li>
                            <li>• أوامر الروت الصامتة للأجهزة المعدلة المروّتة.</li>
                            <li>• رصد وضع الطيران الفوري وإطفاء مؤشرات الراديو.</li>
                        </ul>
                    </div>
                    <div class="glass-card" style="border-top: 3px solid var(--red);">
                        <div class="card-title" style="color: var(--red);">⛔ خارج النطاق (Out-of-Scope)</div>
                        <ul style="font-size: 13px; line-height: 1.8; color: var(--text-muted); list-style: none;">
                            <li>• التحكم بشبكات الواي فاي أو البلوتوث نهائياً.</li>
                            <li>• كسر حماية Samsung Knox بالقوة دون روت.</li>
                            <li>• نقل أي بيانات عبر الإنترنت (تطبيق أوفلاين 100%).</li>
                            <li>• تعديل ملفات النظام بالنواة <code>/system</code> أو كسر IMEI.</li>
                            <li>• إجبار المودم على الاتصال ببرج خارج التغطية الفيزيائية.</li>
                        </ul>
                    </div>
                    <div class="glass-card" style="border-top: 3px solid var(--amber);">
                        <div class="card-title" style="color: var(--amber);">🔒 جدار حماية العتاد (OEM Wall)</div>
                        <p style="font-size: 12.5px; line-height: 1.7; color: var(--text-muted);">
                            تمنع أندرويد التطبيقات العادية من تنفيذ صلاحية <code>MODIFY_PHONE_STATE</code> لحماية أرقام الطوارئ (911/112).
                        </p>
                        <div style="background: rgba(0,0,0,0.4); border-radius: 8px; padding: 10px; margin-top: 10px; border-right: 3px solid var(--cyan);">
                            <b style="color: var(--cyan); font-size: 12px;">استراتيجية NET Mode المبتكرة:</b>
                            <p style="font-size: 11.5px; color: #fff; margin-top: 4px;">
                                • في الهواتف المروّتة: تنفيذ صامت فوري بـ Shell.<br>
                                • في الهواتف العادية: القفز المباشر لنافذة Phone info الأصلية بدون تعقيد.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SLIDE 5: MCP INTEGRATION -->
            <div class="slide-item" data-slide="5" data-notes="بروتوكول MCP هو حلقة الوصل الحديثة بين وكيل الذكاء الاصطناعي وبيئة التطوير الفعلية. دمجنا خادم dart-mcp-server للفحص السكوني وتتبع شجرة الـ Widgets وتشغيل الاختبارات آلياً، وخادم github-mcp-server لحوكمة الفروع وطلبات السحب وحماية الـ Main.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">🤖 الذكاء الاصطناعي والأتمتة</div>
                        <div class="slide-title">منظومة بروتوكول سياق النموذج (Model Context Protocol - MCP)</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 05</div>
                </div>
                <div class="grid-2">
                    <div class="glass-card" style="border-top: 3px solid var(--blue);">
                        <div class="card-title" style="color: var(--cyan);">
                            <span>🎯 خادم دارت (dart-mcp-server)</span>
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 5px;">
                            <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border-right: 3px solid var(--cyan);">
                                <b style="color: #fff; font-size: 13px;">1. الفحص السكوني الآلي (Static Code Analysis):</b>
                                <p style="font-size: 12px; color: var(--text-muted);">فحص شجرة الكود واكتشاف انتهاكات القواعد والأنواع عبر أداة <code>analyze_files</code>.</p>
                            </div>
                            <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border-right: 3px solid var(--green);">
                                <b style="color: #fff; font-size: 13px;">2. تشغيل الاختبارات الآلية (Test Suite Runner):</b>
                                <p style="font-size: 12px; color: var(--text-muted);">تنفيذ <code>run_tests</code> للتحقق من اجتياز اختبارات الوحدة الـ 11 آلياً بنسبة 100%.</p>
                            </div>
                            <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border-right: 3px solid var(--purple);">
                                <b style="color: #fff; font-size: 13px;">3. تفتيش شجرة العناصر (Widget Tree Inspection):</b>
                                <p style="font-size: 12px; color: var(--text-muted);">فحص تراكب الواجهات عبر <code>get_widget_tree</code> وضمان استقرار أبعاد الشاشة.</p>
                            </div>
                        </div>
                    </div>

                    <div class="glass-card" style="border-top: 3px solid var(--purple);">
                        <div class="card-title" style="color: var(--purple);">
                            <span>🛡️ خادم جيت هب (github-mcp-server)</span>
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 5px;">
                            <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border-right: 3px solid var(--purple);">
                                <b style="color: #fff; font-size: 13px;">1. إدارة وأتمتة الفروع (Branch Automation):</b>
                                <p style="font-size: 12px; color: var(--text-muted);">إنشاء فروع الميزات لكل مهمة في كانبان وتتبعها آلياً عبر أدوات الفروع.</p>
                            </div>
                            <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border-right: 3px solid var(--cyan);">
                                <b style="color: #fff; font-size: 13px;">2. حوكمة طلبات الدمج (Pull Request Governance):</b>
                                <p style="font-size: 12px; color: var(--text-muted);">فتح ومراجعة وتدقيق الـ PRs وربطها برقم الـ Issue ومعايير القبول.</p>
                            </div>
                            <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border-right: 3px solid var(--green);">
                                <b style="color: #fff; font-size: 13px;">3. حماية الفرع الرئيسي (Branch Protection):</b>
                                <p style="font-size: 12px; color: var(--text-muted);">حظر الدمج المباشر في <code>main</code> إلا بعد موافقة المراجع واجتياز الفحص السكوني.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SLIDE 6: KANBAN & TEAM (24 ISSUES) -->
            <div class="slide-item" data-slide="6" data-notes="هنا يظهر التوزيع الهندسي الرشيق عبر لوحة كانبان وتريلو: قسمنا الـ 24 مهمة إلى 4 مسارات ملحمية، كل مهندس من الفريق تولى 6 مهام متكاملة بملفات محددة واسم فرع ومعيار إنجاز DoD صارم يمنع الدمج قبل استيفاء الاختبارات.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">📊 إدارة المشاريع الرشيقة</div>
                        <div class="slide-title">لوحة كانبان وهيكلية توزيع المهام الـ 24 على المهندسين الأربعة</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 06</div>
                </div>
                <div class="grid-4">
                    <!-- Eng 1 -->
                    <div class="glass-card" style="border-top: 3px solid var(--cyan);">
                        <div class="card-title" style="font-size: 14px;">1. م. أحمد الأهدل</div>
                        <div style="font-size: 11px; color: var(--cyan); margin-bottom: 8px;">Scrum Master & Docs (Issues #1-#6)</div>
                        <ul style="font-size: 11px; line-height: 1.6; color: var(--text-muted); list-style: none;">
                            <li>• دمج المهارات التخصصية.</li>
                            <li>• صياغة وثيقة الـ SRS الشاملة.</li>
                            <li>• توثيق قصص المستخدمين ومعاييرها.</li>
                            <li>• إعداد دستور المشروع GEMINI.md.</li>
                            <li>• إدارة كانبان وتدفق Git Workflow.</li>
                            <li>• إعداد التقرير المرجعي والمناقشة.</li>
                        </ul>
                    </div>
                    <!-- Eng 2 -->
                    <div class="glass-card" style="border-top: 3px solid var(--green);">
                        <div class="card-title" style="font-size: 14px;">2. م. محمد علي / الدعيس</div>
                        <div style="font-size: 11px; color: var(--green); margin-bottom: 8px;">Core Domain & Architect (#7-#12)</div>
                        <ul style="font-size: 11px; line-height: 1.6; color: var(--text-muted); list-style: none;">
                            <li>• كينونة NetworkMode (دارت نقي).</li>
                            <li>• كينونة NetworkInfo للبيانات الحية.</li>
                            <li>• تجريد واجهة المستودع NetworkRepo.</li>
                            <li>• تنفيذ GetCurrentModeUseCase.</li>
                            <li>• تنفيذ SetNetworkModeUseCase.</li>
                            <li>• تطبيق اختبارات الوحدة للنطاق.</li>
                        </ul>
                    </div>
                    <!-- Eng 3 -->
                    <div class="glass-card" style="border-top: 3px solid var(--amber);">
                        <div class="card-title" style="font-size: 14px;">3. م. يوسف خيري</div>
                        <div style="font-size: 11px; color: var(--amber); margin-bottom: 8px;">Data & Platform (#13-#18)</div>
                        <ul style="font-size: 11px; line-height: 1.6; color: var(--text-muted); list-style: none;">
                            <li>• بناء RadioDeviceDataSource.</li>
                            <li>• تنفيذ مستودع NetworkRepoImpl.</li>
                            <li>• برمجة قنوات Platform بنواة كوتلن.</li>
                            <li>• استخراج الإشارة عبر TelephonyManager.</li>
                            <li>• خوارزمية السقوط المتعدد Multi-Intent.</li>
                            <li>• إدارة الأذونات وحفظ التفضيلات.</li>
                        </ul>
                    </div>
                    <!-- Eng 4 -->
                    <div class="glass-card" style="border-top: 3px solid var(--purple);">
                        <div class="card-title" style="font-size: 14px;">4. م. مؤيد الصوفي</div>
                        <div style="font-size: 11px; color: var(--purple); margin-bottom: 8px;">UI/UX & State (#19-#24)</div>
                        <ul style="font-size: 11px; line-height: 1.6; color: var(--text-muted); list-style: none;">
                            <li>• تصميم سمة النيون Cyberpunk Navy.</li>
                            <li>• بطاقة المراقبة الحية بـ 5 أعمدة.</li>
                            <li>• بطاقات الأنماط الخمسة لليمن.</li>
                            <li>• مراقب دورة الحياة WidgetsBinding.</li>
                            <li>• معالجة وضع الطيران والأخطاء.</li>
                            <li>• الإخراج البصري واختبارات القبول.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- SLIDE 7: CLEAN ARCHITECTURE -->
            <div class="slide-item" data-slide="7" data-notes="التزمنا بالمعمارية النظيفة Clean Architecture وقاعدة الاعتمادية. طبقة النطاق نقية 100% بدون أي كود فلاتر أو أندرويد لضمان استقلالية منطق الأعمال، وتتصل بطبقة البيانات عبر Interfaces وعكس التبعيات DIP وفق مبادئ SOLID.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">🏛️ المعمارية البرمجية</div>
                        <div class="slide-title">المعمارية النظيفة (Clean Architecture) ومبادئ SOLID الخمسة</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 07</div>
                </div>
                <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-around;">
                    <!-- Presentation Layer -->
                    <div class="arch-layer presentation">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <b style="color: #38BDF8; font-size: 15px;">1. طبقة العرض والواجهات (Presentation Layer)</b>
                            <span style="font-size: 12px; color: var(--text-muted);">Widgets, Controllers, UI/UX Pro Max Theme</span>
                        </div>
                        <p style="font-size: 12px; color: var(--text-muted);">
                            تستقبل مدخلات المستخدم وتعرض الحالة التفاعلية وتعتمد حصراً على حالات الاستخدام (Use Cases) دون أي معرفة بتفاصيل المودم أو كوتلن.
                        </p>
                    </div>

                    <!-- Domain Layer -->
                    <div class="arch-layer domain">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <b style="color: #34D399; font-size: 15px;">2. طبقة النطاق ومنطق الأعمال (Domain Layer - Pure Dart)</b>
                            <span style="font-size: 12px; background: rgba(16, 185, 129, 0.2); color: var(--green); padding: 2px 8px; border-radius: 4px;">Zero Flutter / Zero Android</span>
                        </div>
                        <p style="font-size: 12px; color: #fff;">
                            القلب المستقل للمشروع. يضم الكيانات غير القابلة للتعديل (NetworkMode, NetworkInfo)، وحالات الاستخدام، وواجهات المستودعات المجرّدة.
                        </p>
                    </div>

                    <!-- Data Layer -->
                    <div class="arch-layer data">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <b style="color: #FBBF24; font-size: 15px;">3. طبقة البيانات والاتصال بالمنصة (Data Layer)</b>
                            <span style="font-size: 12px; color: var(--text-muted);">Repositories, MethodChannel, SharedPreferences</span>
                        </div>
                        <p style="font-size: 12px; color: var(--text-muted);">
                            تنفذ واجهات المستودع وتتصل بنواة كوتلن عبر قنوات المنصة وتخزن تفضيلات المستخدم محلياً مع معالجة الاستثناءات الدفاعية.
                        </p>
                    </div>

                    <!-- SOLID Footer -->
                    <div style="background: rgba(0,0,0,0.4); border-radius: 8px; padding: 10px 16px; border: 1px dashed rgba(0, 240, 255, 0.4); text-align: center;">
                        <span style="color: var(--cyan); font-weight: 700; font-size: 12.5px;">مبادئ SOLID المطبقة:</span>
                        <span style="font-size: 12px; color: #fff; margin-right: 10px;">
                            مسؤولية أحادية (SRP) • انفتاح للتوسيع وإغلاق للتعديل (OCP) • استبدال لسكوف (LSP) • فصل الواجهات (ISP) • عكس الاعتمادية (DIP)
                        </span>
                    </div>
                </div>
            </div>

            <!-- SLIDE 8: NATIVE KOTLIN ENGINE -->
            <div class="slide-item" data-slide="8" data-notes="هنا يكمن العمق الهندسي لنواة كوتلن الأصلية. صممنا خوارزمية السقوط المتعدد Multi-Intent التي تضمن فتح إعدادات المودم حتى لو حظرت الشركة واجهة معينة، واستخرجنا قوة الإشارة من TelephonyManager بدقة الـ dBm مع التوافق التام مع أندرويد 8 إلى 14+.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">⚙️ النواة والبرمجة المنخفضة</div>
                        <div class="slide-title">هندسة الاتصال العميق بالمودم ونواة كوتلن (Native Kotlin Engine)</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 08</div>
                </div>
                <div class="grid-2">
                    <div class="glass-card">
                        <div class="card-title">🔄 خوارزمية السقوط المتعدد (Multi-Intent Fallback)</div>
                        <p style="font-size: 12.5px; color: var(--text-muted); margin-bottom: 10px;">
                            نظراً لاختلاف واجهات الشركات، يمر التطبيق بسلسلة حزم متتالية تضمن النجاح 100%:
                        </p>
                        <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 8px; font-family: 'JetBrains Mono', monospace; font-size: 11.5px; color: var(--cyan); line-height: 1.8;">
                            1. com.android.phone...RadioInfo<br>
                            2. com.android.settings...RadioInfo<br>
                            3. com.android.settings...TestingSettings<br>
                            4. Settings.ACTION_DATA_ROAMING_SETTINGS
                        </div>
                        <p style="font-size: 11.5px; color: var(--green); margin-top: 10px;">
                            ✔ كل نداء محمي بـ try-catch مع إضافة <code>FLAG_ACTIVITY_NEW_TASK</code> لمنع أي كراش.
                        </p>
                    </div>

                    <div class="glass-card">
                        <div class="card-title">📡 استخراج الإشارة ومسار الروت المزدوج</div>
                        <div style="display: flex; flex-direction: column; gap: 10px;">
                            <div style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px;">
                                <b style="color: #fff; font-size: 12.5px;">• استخراج الإشارة عبر TelephonyManager:</b>
                                <p style="font-size: 11.5px; color: var(--text-muted); margin-top: 3px;">
                                    استخراج قيم dBm و ASU ومستوى الإشارة من 0 إلى 4 مع التوافق التام من Android 8 إلى Android 14+.
                                </p>
                            </div>
                            <div style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px; border-right: 3px solid var(--purple);">
                                <b style="color: var(--purple); font-size: 12.5px;">• المسار الصامت للأجهزة المروّتة (Root Path):</b>
                                <p style="font-size: 11.5px; color: #fff; margin-top: 3px;">
                                    تنفيذ أمر الشل الفوري <code>su -c cmd phone set-preferred-network-type [CODE]</code> لتغيير التردد بلمسة واحدة.
                                </p>
                            </div>
                            <div style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px; border-right: 3px solid var(--cyan);">
                                <b style="color: var(--cyan); font-size: 12.5px;">• مسار الأجهزة القياسية (Standard Path):</b>
                                <p style="font-size: 11.5px; color: #fff; margin-top: 3px;">
                                    القفز لنافذة Phone info الأصلية بضغطة زر واحدة وإرشاد المستخدم للنمط المطلوب فوراً.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SLIDE 9: UI/UX & SCREEN SHOWCASE -->
            <div class="slide-item" data-slide="9" data-notes="هنا واجهات التطبيق الحقيقية: واجهة Cyberpunk Dark Navy مع 5 أعمدة إشارة نيون تتفاعل حياً مع الإشارة، شاشة Phone info الأصلية التي يفتحها التطبيق، ودرع وضع الطيران التفاعلي الذي يطفئ المودم فوراً، مع التحديث الذاتي التلقائي عبر مراقب دورة حياة النظام.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">📱 التجربة الرقمية</div>
                        <div class="slide-title">معرض الواجهات الواقعية وتجربة المستخدم (UI/UX Pro Max Showcase)</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 09</div>
                </div>
                <div class="screens-wrapper">
                    <div class="mockup-item">
                        <img class="mockup-frame" src="data:image/png;base64,__APP_SCREEN_B64__" alt="واجهة التطبيق الرئيسية">
                        <span class="mockup-caption">1. شاشة المراقبة وأعمدة النيون الحية</span>
                    </div>
                    <div class="mockup-item">
                        <img class="mockup-frame" src="data:image/png;base64,__DEVICE_SCREEN_B64__" alt="شاشة Phone info">
                        <span class="mockup-caption" style="color: var(--green);">2. نافذة Phone info الأصلية للمودم</span>
                    </div>
                    <div class="mockup-item">
                        <img class="mockup-frame" src="data:image/png;base64,__AIRPLANE_SCREEN_B64__" alt="وضع الطيران">
                        <span class="mockup-caption" style="color: var(--red);">3. درع وضع الطيران التفاعلي الفوري</span>
                    </div>
                </div>
            </div>

            <!-- SLIDE 10: QUALITY ASSURANCE & DEFENSIVE -->
            <div class="slide-item" data-slide="10" data-notes="الجودة والتصميم الدفاعي ركيزة أساسية: أنجزنا 11 اختبار وحدة آلي بنجاح 100% لتغطية كيانات النمط والإشارة وحالات الاستخدام، وطبقنا حماية ضد وضع الطيران وفقدان الأذونات والتكيف التلقائي مع عودة المستخدم للشاشة.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">🛡️ ضمان الجودة</div>
                        <div class="slide-title">مصفوفة التحقق الآلي والتصميم الدفاعي الصارم (Quality Assurance)</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 10</div>
                </div>
                <div class="grid-2">
                    <div class="glass-card" style="border-top: 3px solid var(--green);">
                        <div class="card-title" style="color: var(--green);">✔ اختبارات الوحدة المؤتمتة (11/11 نجاح تام)</div>
                        <ul style="font-size: 12.5px; line-height: 1.9; color: #fff; list-style: none;">
                            <li>• <b>NetworkMode Entity Tests:</b> التحقق من صحة تعريفات الأنماط والأكواد.</li>
                            <li>• <b>NetworkInfo Validation:</b> التحقق من سلامة قراءة dBm والتقنية وحالة SIM.</li>
                            <li>• <b>GetCurrentModeUseCase:</b> اختبار استرجاع النمط الفعلي عبر Mock Repository.</li>
                            <li>• <b>SetNetworkModeUseCase:</b> اختبار تمرير الأوامر وضمان الاستجابة.</li>
                            <li>• <b>Repository Isolation:</b> عزل طبقة النطاق 100% عن استثناءات المنصة.</li>
                        </ul>
                    </div>

                    <div class="glass-card" style="border-top: 3px solid var(--cyan);">
                        <div class="card-title">🛡️ أنماط التصميم الدفاعي (Defensive Resilience)</div>
                        <ul style="font-size: 12.5px; line-height: 1.9; color: var(--text-muted); list-style: none;">
                            <li>• <b>درع وضع الطيران:</b> استشعار فوري وإطفاء مؤشرات الراديو فوراً.</li>
                            <li>• <b>حارس الأذونات:</b> فحص <code>READ_PHONE_STATE</code> وعرض بطاقة إرشادية دون كراش.</li>
                            <li>• <b>مراقب دورة الحياة:</b> <code>WidgetsBindingObserver</code> يحدث البيانات تلقائياً بمجرد عودة المستخدم من الإعدادات.</li>
                            <li>• <b>التوافق العتادي:</b> تعامل آمن مع الشرائح المزدوجة (Dual SIM) ومعالجات ميدياتك وكوالكوم.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- SLIDE 11: KEY METRICS -->
            <div class="slide-item" data-slide="11" data-notes="هذه المؤشرات الرقمية تلخص الجهد الهندسي الجبار: 24 مهمة مكتملة بنسبة 100%، 11 اختبار آلي ناجح، صفر اعتمادات خارجية للإنترنت لضمان الأمان، 5 أوضاع مخصصة لليمن، وتوثيق أكاديمي شامل في 18 صفحة.">
                <div class="slide-header">
                    <div>
                        <div class="slide-category">📈 مؤشرات النجاح</div>
                        <div class="slide-title">مصفوفة الإنجاز ومؤشرات الجودة الهندسية المكتملة</div>
                    </div>
                    <div class="slide-number-badge">SLIDE 11</div>
                </div>
                <div class="grid-3" style="grid-template-rows: 1fr 1fr;">
                    <div class="metric-card">
                        <div class="metric-val">24 / 24</div>
                        <div class="metric-label">مهمة كانبان مكتملة</div>
                        <div class="metric-desc">توزيع دقيق عبر Trello على المهندسين الأربعة بمحددات DoD.</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-val" style="color: var(--green);">11 / 11</div>
                        <div class="metric-label">اختبارات وحدة آلية ناجحة</div>
                        <div class="metric-desc">تغطية شاملة لطبقة النطاق بدون أي تحذير Lint.</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-val" style="color: var(--purple);">100%</div>
                        <div class="metric-label">أوفلاين وأمان تام</div>
                        <div class="metric-desc">صفر اتصالات خارجية، وحماية تامة لخصوصية المستخدم.</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-val" style="color: var(--amber);">5 أنماط</div>
                        <div class="metric-label">مخصصة لشبكات اليمن</div>
                        <div class="metric-desc">دعم سبأفون، يو، ويمن موبايل (VoLTE/4G).</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-val" style="color: var(--cyan);">18 صفحة</div>
                        <div class="metric-label">توثيق أكاديمي محكّم</div>
                        <div class="metric-desc">تقرير هندسة البرمجيات الكبرى المعتمد للمناقشة.</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-val" style="color: #38BDF8;">0 Imports</div>
                        <div class="metric-label">نقاء طبقة النطاق</div>
                        <div class="metric-desc">استقلالية كاملة متوافقة مع معايير Clean Architecture.</div>
                    </div>
                </div>
            </div>

            <!-- SLIDE 12: CONCLUSION & DEFENSE -->
            <div class="slide-item" data-slide="12" data-notes="ختاماً، نتوجه بأسمى آيات الشكر والامتنان لأستاذنا المشرف الدكتور ساهر الهمداني على دعمه وتوجيهه المستمر. ويسعدنا ويشرفنا الآن فتح باب النقاش والاستفسارات أمام لجنتكم الموقرة.">
                <div class="cover-box">
                    <div class="cover-badge" style="border-color: var(--green); color: var(--green);">خاتمة الدفاع ومناقشة مشروع التخرج</div>
                    <div class="cover-title" style="font-size: 42px;">خلاصة الإنجاز الهندسي</div>
                    <div class="cover-desc" style="max-width: 800px; font-size: 15px; margin-bottom: 20px;">
                        مشروع <b>NET Mode</b> يمثل دليلاً تطبيقياً حياً على أن هندسة البرمجيات الرشيقة، عندما تقترن بالمعمارية النظيفة، وحوكمة الذكاء الاصطناعي عبر بروتوكول MCP، والتصميم الدفاعي، قادرة على حل أصعب المشكلات العتادية على الهواتف الذكية بكفاءة وأمان تام.
                    </div>

                    <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid var(--green); border-radius: 14px; padding: 20px 30px; margin-bottom: 25px; box-shadow: 0 0 30px rgba(16, 185, 129, 0.2);">
                        <p style="font-size: 14px; color: var(--text-muted); margin-bottom: 5px;">خالص الشكر والتقدير للأستاذ المشرف:</p>
                        <h2 style="font-family: 'Cairo', sans-serif; font-size: 28px; color: var(--green); font-weight: 800;">
                            د.م. ساهر الهمداني
                        </h2>
                        <p style="font-size: 13px; color: var(--cyan); margin-top: 6px;">
                            على دعمه وتوجيهاته العلمية القيمة التي مكنتنا من إنجاز هذا العمل بأعلى المقاييس العالمية.
                        </p>
                    </div>

                    <div style="font-family: 'Cairo', sans-serif; font-size: 20px; font-weight: 800; color: var(--cyan); display: flex; align-items: center; gap: 10px;">
                        <span>🎓</span>
                        <span>باب الاستفسارات والمناقشة مفتوح أمام لجنة التحكيم الموقرة</span>
                        <span>🎓</span>
                    </div>
                </div>
            </div>

        </div>

        <!-- Bottom Bar -->
        <div class="bottom-bar">
            <div class="keyboard-hints">
                <span>التنقل: <span class="key-tag">←</span> <span class="key-tag">→</span> أو <span class="key-tag">مسافة</span></span>
                <span>ملء الشاشة: <span class="key-tag">F</span></span>
                <span>الفهرس: <span class="key-tag">O</span></span>
                <span>المتحدث: <span class="key-tag">N</span></span>
            </div>
            <div>
                <span>مشروع تخرج هندسة البرمجيات | NET Mode Suite © 2026</span>
            </div>
        </div>
    </div>

    <!-- Speaker Notes Modal -->
    <div id="notesModal">
        <div class="notes-header">
            <span>🎙️ ملاحظات المتحدث وسيناريو الإلقاء</span>
            <span style="cursor: pointer;" onclick="toggleNotes()">✕</span>
        </div>
        <p id="notesContent" style="font-size: 13px; line-height: 1.7; color: var(--text-main); max-height: 250px; overflow-y: auto;">
            ملاحظات الشريحة الحالية...
        </p>
    </div>

    <!-- Overview Grid -->
    <div id="overviewGrid"></div>

    <script>
        // Particle Background System
        const canvas = document.getElementById('networkCanvas');
        const ctx = canvas.getContext('2d');
        let width, height, particles;

        function initCanvas() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            particles = [];
            const count = Math.floor((width * height) / 18000);
            for (let i = 0; i < count; i++) {
                particles.push({
                    x: Math.random() * width,
                    y: Math.random() * height,
                    vx: (Math.random() - 0.5) * 0.6,
                    vy: (Math.random() - 0.5) * 0.6,
                    radius: Math.random() * 2 + 1,
                    color: Math.random() > 0.4 ? '#00F0FF' : '#8B5CF6'
                });
            }
        }

        function drawParticles() {
            ctx.clearRect(0, 0, width, height);

            for (let i = 0; i < particles.length; i++) {
                const p = particles[i];
                p.x += p.vx;
                p.y += p.vy;

                if (p.x < 0 || p.x > width) p.vx *= -1;
                if (p.y < 0 || p.y > height) p.vy *= -1;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fillStyle = p.color;
                ctx.shadowBlur = 10;
                ctx.shadowColor = p.color;
                ctx.fill();

                for (let j = i + 1; j < particles.length; j++) {
                    const p2 = particles[j];
                    const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
                    if (dist < 120) {
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = `rgba(0, 240, 255, ${0.2 * (1 - dist / 120)})`;
                        ctx.lineWidth = 0.8;
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(drawParticles);
        }

        window.addEventListener('resize', initCanvas);
        initCanvas();
        drawParticles();

        // Slide Deck Navigation System
        const slides = document.querySelectorAll('.slide-item');
        const progressBar = document.getElementById('progressBar');
        const slideIndicator = document.getElementById('slideIndicator');
        const notesContent = document.getElementById('notesContent');
        const notesModal = document.getElementById('notesModal');
        const overviewGrid = document.getElementById('overviewGrid');
        let currentSlide = 0;
        const totalSlides = slides.length;

        function updateSlide() {
            slides.forEach((s, idx) => {
                s.classList.toggle('active', idx === currentSlide);
            });
            const progress = ((currentSlide + 1) / totalSlides) * 100;
            progressBar.style.width = progress + '%';
            slideIndicator.innerText = `الشريحة ${currentSlide + 1} من ${totalSlides}`;

            // Update speaker notes
            const activeNotes = slides[currentSlide].getAttribute('data-notes') || 'لا توجد ملاحظات إضافية لهذه الشريحة.';
            notesContent.innerHTML = activeNotes;
        }

        function nextSlide() {
            if (currentSlide < totalSlides - 1) {
                currentSlide++;
                updateSlide();
            }
        }

        function prevSlide() {
            if (currentSlide > 0) {
                currentSlide--;
                updateSlide();
            }
        }

        function goToSlide(index) {
            if (index >= 0 && index < totalSlides) {
                currentSlide = index;
                updateSlide();
                if (overviewGrid.classList.contains('visible')) {
                    toggleOverview();
                }
            }
        }

        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                }
            }
        }

        function toggleNotes() {
            notesModal.classList.toggle('visible');
        }

        function toggleOverview() {
            overviewGrid.classList.toggle('visible');
            if (overviewGrid.classList.contains('visible')) {
                overviewGrid.innerHTML = '';
                slides.forEach((s, i) => {
                    const title = s.querySelector('.slide-title')?.innerText || (i === 0 ? 'الغلاف الهندسي' : s.querySelector('.card-title')?.innerText || `شريحة ${i+1}`);
                    const thumb = document.createElement('div');
                    thumb.className = `overview-thumb ${i === currentSlide ? 'current' : ''}`;
                    thumb.innerHTML = `
                        <div style="display:flex; justify-content:space-between; font-size:11px; color:var(--cyan); font-family:'JetBrains Mono';">
                            <span>SLIDE ${i+1}</span>
                            <span>${i === currentSlide ? '● النشطة' : ''}</span>
                        </div>
                        <div style="font-size:13px; font-weight:700; color:#fff; font-family:'Cairo';">${title}</div>
                    `;
                    thumb.onclick = () => goToSlide(i);
                    overviewGrid.appendChild(thumb);
                });
            }
        }

        // Keyboard Controls
        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
                nextSlide();
            } else if (e.key === 'ArrowLeft' || e.key === 'PageUp' || e.key === 'Backspace') {
                prevSlide();
            } else if (e.key === 'f' || e.key === 'F') {
                toggleFullscreen();
            } else if (e.key === 'n' || e.key === 'N') {
                toggleNotes();
            } else if (e.key === 'o' || e.key === 'O' || e.key === 'Escape') {
                if (e.key === 'Escape' && overviewGrid.classList.contains('visible')) {
                    toggleOverview();
                } else if (e.key === 'o' || e.key === 'O') {
                    toggleOverview();
                }
            }
        });

        // Initialize state
        updateSlide();
    </script>
</body>
</html>
"""

# Replace base64 tokens
final_html = html_template.replace("__APP_SCREEN_B64__", app_screen_b64)
final_html = final_html.replace("__DEVICE_SCREEN_B64__", device_screen_b64)
final_html = final_html.replace("__AIRPLANE_SCREEN_B64__", airplane_screen_b64)

with open(html_deck_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Interactive Presentation Deck generated successfully at:", html_deck_path)
print("File size in bytes:", os.path.getsize(html_deck_path))
