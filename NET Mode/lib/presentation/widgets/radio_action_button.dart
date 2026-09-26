import 'package:flutter/material.dart';

/// [FR-21 / US-21] زر الإجراء التفاعلي البارز لفتح إعدادات شبكة LTE Only.
///
/// ودجت مخصصة قابلة لإعادة الاستخدام تمثل زر الإجراء الرئيسي
/// لفتح صفحة إعدادات الراديو أو تغيير نمط الشبكة.
/// يتميز بتصميم بارز مع حدود نيون وتأثيرات ضغط تفاعلية (InkWell).
///
/// معايير القبول (DoD):
/// - [x] زر بتصميم مميز بأيقونة مناسبة.
/// - [x] استجابة نقر غير متزامنة دون تعليق الواجهة.
class RadioActionButton extends StatelessWidget {
  /// الدالة التي تُنفَّذ عند الضغط على الزر (غير متزامنة دون تعليق الواجهة).
  final VoidCallback onPressed;

  /// النص التوضيحي المعروض على الزر.
  final String label;

  /// الأيقونة المعروضة بجانب النص.
  final IconData icon;

  const RadioActionButton({
    super.key,
    required this.onPressed,
    this.label = 'تغيير نمط شبكة الهاتف',
    this.icon = Icons.settings,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: const Color(0xFF0F172A).withValues(alpha: 0.5),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: const Color(0xFF38BDF8),
          width: 1.5,
        ),
      ),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          borderRadius: BorderRadius.circular(16),
          onTap: onPressed,
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 14),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(icon, color: const Color(0xFF38BDF8), size: 20),
                const SizedBox(width: 8),
                Flexible(
                  child: Text(
                    label,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF38BDF8),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
