import 'package:flutter/material.dart';

/// [FR-19 / US-19] السمة الداكنة المتقدمة (Dark Cyberpunk Theme).
///
/// تعريف نظام ألوان موحد مريح للعين يوفر طاقة شاشات AMOLED
/// ويضمن تناسق جميع العناصر البصرية في التطبيق.
///
/// DoD:
///   ✅ تعريف ثيم داكن رسمي موحد داخل ThemeData.dark().
///   ✅ ضبط الألوان الأساسية: الخلفية #0F172A والأزرق السماوي #38BDF8.
///   ✅ توحيد مظهر خطوط النصوص وعناوين الشاشة الرئيسية.
///   ✅ اختبار ظهور الألوان وتناسقها في بيئة التشغيل الفعلية.
class AppTheme {
  AppTheme._(); // منع الإنشاء — كلاس مساعد فقط

  // ─────────────────────────────────────────────────────────
  //  لوحة الألوان الأساسية (Color Palette)
  // ─────────────────────────────────────────────────────────

  /// لون الخلفية الرئيسي — أزرق غامق شبيه بسماء الليل
  static const Color background = Color(0xFF0F172A);

  /// اللون الأساسي — أزرق سماوي نيون
  static const Color primary = Color(0xFF38BDF8);

  /// اللون الثانوي — بنفسجي ناعم
  static const Color secondary = Color(0xFF818CF8);

  /// لون بطاقات الواجهة (Cards)
  static const Color cardColor = Color(0xFF1E293B);

  /// لون سطح العناصر الداخلية
  static const Color surface = Color(0xFF162032);

  /// لون النصوص الرئيسية
  static const Color textPrimary = Colors.white;

  /// لون النصوص الثانوية / التوضيحية
  static const Color textSecondary = Color(0xFF7DD3FC);

  /// لون النصوص الخافتة
  static const Color textMuted = Color(0xFF94A3B8);

  /// لون الحدود المضيئة
  static const Color borderGlow = Color(0xFF38BDF8);

  /// لون النجاح — أخضر زمردي
  static const Color success = Color(0xFF4ADE80);

  /// لون التحذير — برتقالي
  static const Color warning = Color(0xFFFB923C);

  /// لون الخطأ — أحمر ناعم
  static const Color error = Color(0xFFEF4444);

  /// درجة أزرق داكنة للتدرجات
  static const Color gradientDark = Color(0xFF0284C7);

  // ─────────────────────────────────────────────────────────
  //  الثيم الداكن الرسمي الموحد (Dark ThemeData)
  // ─────────────────────────────────────────────────────────

  /// الثيم الرسمي المستخدم في MaterialApp.
  ///
  /// يُعرَّف داخل `ThemeData.dark()` مع تخصيص كامل لنظام الألوان
  /// والخطوط والأشكال وأنماط العناصر التفاعلية.
  static ThemeData get darkTheme {
    return ThemeData(
      brightness: Brightness.dark,
      useMaterial3: true,

      // ── الألوان الأساسية ──
      scaffoldBackgroundColor: background,
      cardColor: cardColor,
      colorScheme: const ColorScheme.dark(
        primary: primary,
        secondary: secondary,
        surface: surface,
        error: error,
        onPrimary: Colors.white,
        onSecondary: Colors.white,
        onSurface: textPrimary,
        onError: Colors.white,
      ),

      // ── شريط التطبيق (AppBar) ──
      appBarTheme: const AppBarTheme(
        backgroundColor: Colors.transparent,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: TextStyle(
          fontSize: 18,
          fontWeight: FontWeight.w700,
          color: textPrimary,
          letterSpacing: 0.5,
        ),
        iconTheme: IconThemeData(color: primary),
      ),

      // ── أنماط النصوص (Typography) ──
      textTheme: const TextTheme(
        // عناوين كبيرة — اسم المشغل
        headlineLarge: TextStyle(
          fontSize: 26,
          fontWeight: FontWeight.bold,
          color: textPrimary,
          letterSpacing: 1,
        ),
        // عناوين متوسطة — عنوان الشاشة
        headlineMedium: TextStyle(
          fontSize: 20,
          fontWeight: FontWeight.w700,
          color: textPrimary,
        ),
        // عناوين صغيرة — أقسام الواجهة
        titleMedium: TextStyle(
          fontSize: 16,
          fontWeight: FontWeight.bold,
          color: textSecondary,
        ),
        // نص الأجسام — المحتوى العادي
        bodyLarge: TextStyle(
          fontSize: 16,
          fontWeight: FontWeight.w700,
          color: textPrimary,
        ),
        bodyMedium: TextStyle(
          fontSize: 14,
          fontWeight: FontWeight.w500,
          color: textPrimary,
        ),
        // نصوص ثانوية — التفاصيل والوصف
        bodySmall: TextStyle(
          fontSize: 12,
          fontWeight: FontWeight.w600,
          color: textSecondary,
        ),
        // نص الأزرار
        labelLarge: TextStyle(
          fontSize: 16,
          fontWeight: FontWeight.bold,
          color: primary,
        ),
      ),

      // ── الأزرار المرتفعة (ElevatedButton) ──
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: primary,
          foregroundColor: Colors.white,
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
          textStyle: const TextStyle(
            fontSize: 16,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),

      // ── الزر العائم (FAB) ──
      floatingActionButtonTheme: const FloatingActionButtonThemeData(
        backgroundColor: gradientDark,
        foregroundColor: Colors.white,
        elevation: 6,
      ),

      // ── SnackBar ──
      snackBarTheme: SnackBarThemeData(
        backgroundColor: cardColor,
        contentTextStyle: const TextStyle(
          fontSize: 14,
          fontWeight: FontWeight.w500,
          color: textPrimary,
        ),
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),

      // ── البطاقات (Cards) ──
      cardTheme: CardThemeData(
        color: cardColor,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(18),
          side: BorderSide(
            color: borderGlow.withValues(alpha: 0.3),
            width: 1.5,
          ),
        ),
      ),

      // ── مؤشر التحميل ──
      progressIndicatorTheme: const ProgressIndicatorThemeData(
        color: primary,
        circularTrackColor: surface,
      ),

      // ── حقول الإدخال ──
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: surface,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: BorderSide(color: borderGlow.withValues(alpha: 0.3)),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: primary, width: 1.5),
        ),
      ),

      // ── مؤشر التبديل / الخيارات ──
      switchTheme: SwitchThemeData(
        thumbColor: WidgetStateProperty.resolveWith((states) =>
            states.contains(WidgetState.selected) ? primary : textMuted),
        trackColor: WidgetStateProperty.resolveWith((states) =>
            states.contains(WidgetState.selected) ? primary.withValues(alpha: 0.3) : surface),
      ),
    );
  }
}
