import 'package:flutter/material.dart';
import '../../domain/entities/network_mode.dart';

/// بطاقة نمط شبكة واحد (مطابقة للتصميم بدقة).
///
/// تعرض اسم النمط ووصفه ودائرة الجيل الملونة مع تأثيرات
/// التحديد المتحركة (AnimatedContainer) ومؤشر التطبيق.
class ModeCard extends StatelessWidget {
  final NetworkMode mode;
  final bool isSelected;
  final bool isApplying;
  final VoidCallback onTap;

  const ModeCard({
    super.key,
    required this.mode,
    required this.isSelected,
    required this.isApplying,
    required this.onTap,
  });

  Color get _generationColor {
    return switch (mode.generation) {
      NetworkGeneration.fiveG => const Color(0xFF818CF8),
      NetworkGeneration.fourG => const Color(0xFF38BDF8),
      NetworkGeneration.threeG => const Color(0xFF34D399),
      NetworkGeneration.twoG => const Color(0xFFFBBF24),
      NetworkGeneration.autoMultiMode => const Color(0xFF94A3B8),
    };
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: isApplying ? null : onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        decoration: BoxDecoration(
          color: isSelected
              ? const Color(0xFF0C2442).withValues(alpha: 0.75)
              : const Color(0xFF162032).withValues(alpha: 0.75),
          borderRadius: BorderRadius.circular(18),
          border: Border.all(
            color: isSelected ? const Color(0xFF38BDF8) : const Color(0xFF334155).withValues(alpha: 0.45),
            width: 1.5,
          ),
          boxShadow: isSelected
              ? [
                  BoxShadow(
                    color: const Color(0xFF38BDF8).withValues(alpha: 0.15),
                    blurRadius: 10,
                    spreadRadius: 1,
                  ),
                ]
              : null,
        ),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // ── دائرة الجيل بالحدود الملونة ──
            Container(
              width: 48,
              height: 48,
              decoration: BoxDecoration(
                color: const Color(0xFF0B132B).withValues(alpha: 0.8),
                shape: BoxShape.circle,
                border: Border.all(
                  color: _generationColor,
                  width: 1.5,
                ),
              ),
              child: Center(
                child: Text(
                  mode.generation.label.split(' ')[0], // "4G", "3G", etc.
                  style: TextStyle(
                    color: _generationColor,
                    fontWeight: FontWeight.bold,
                    fontSize: 14,
                  ),
                ),
              ),
            ),
            const SizedBox(width: 14),

            // ── الاسم والنمط المستهدف مع سهم المثلث ──
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    mode.name,
                    textDirection: TextDirection.ltr,
                    style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w700,
                      color: Colors.white,
                    ),
                  ),
                  if (mode.description.isNotEmpty) ...[
                    const SizedBox(height: 5),
                    Row(
                      children: [
                        const Icon(
                          Icons.arrow_right,
                          size: 16,
                          color: Color(0xFF38BDF8),
                        ),
                        Flexible(
                          child: Text(
                            mode.description,
                            textDirection: TextDirection.ltr,
                            style: const TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                              color: Color(0xFF7DD3FC),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ],
                ],
              ),
            ),

            const SizedBox(width: 8),
            // ── أيقونة التحديد عند الاختيار ──
            if (isSelected && isApplying)
              const SizedBox(
                width: 22,
                height: 22,
                child: CircularProgressIndicator(strokeWidth: 2, color: Color(0xFF38BDF8)),
              )
            else if (isSelected)
              const Icon(Icons.check_circle, color: Color(0xFF38BDF8), size: 24),
          ],
        ),
      ),
    );
  }
}
