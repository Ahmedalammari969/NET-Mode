import 'package:flutter/material.dart';
import '../../domain/entities/network_info.dart';

/// بطاقة حالة الشبكة الحالية مع أعمدة إشارة نيونية مضيئة.
///
/// تعرض حالة الاتصال (متصلة / غير متصلة / وضع طيران)
/// واسم المشغل ونوع الشبكة الحالي وحالة شريحة SIM.
class NetworkStatusCard extends StatelessWidget {
  final NetworkInfo? networkInfo;

  const NetworkStatusCard({super.key, required this.networkInfo});

  /// يبني عمود إشارة واحد بارتفاع محدد ولون يعتمد على حالة الاتصال.
  static Widget _buildBar(double height, {required bool isConnected}) {
    return Container(
      width: 6,
      height: height,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(2.5),
        gradient: isConnected
            ? const LinearGradient(
                begin: Alignment.bottomCenter,
                end: Alignment.topCenter,
                colors: [Color(0xFF0284C7), Color(0xFF38BDF8)],
              )
            : const LinearGradient(
                begin: Alignment.bottomCenter,
                end: Alignment.topCenter,
                colors: [Color(0xFF334155), Color(0xFF64748B)],
              ),
        boxShadow: isConnected
            ? [
                BoxShadow(
                  color: const Color(0xFF38BDF8).withValues(alpha: 0.6),
                  blurRadius: 6,
                  spreadRadius: 1,
                ),
              ]
            : null,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final info = networkInfo;
    final isAirplane = info?.isAirplaneMode == true;
    final isConnected = info != null &&
        info.hasSimCard &&
        !isAirplane &&
        info.carrier != 'No Carrier' &&
        info.carrier != 'وضع الطيران';

    final String statusText;
    final Color statusColor;
    if (isAirplane) {
      statusText = 'وضع الطيران (غير متصلة)';
      statusColor = const Color(0xFFFB923C);
    } else if (isConnected) {
      statusText = 'الشبكة متصلة';
      statusColor = const Color(0xFF38BDF8);
    } else {
      statusText = 'الشبكة غير متصلة';
      statusColor = Colors.redAccent;
    }

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 20),
      decoration: BoxDecoration(
        color: const Color(0xFF162032).withValues(alpha: 0.75),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(
          color: const Color(0xFF38BDF8).withValues(alpha: 0.3),
          width: 1.5,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.35),
            blurRadius: 18,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        children: [
          // ── السطر العلوي: أعمدة الإشارة + حالة الاتصال (مرن لتجنب overflow) ──
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // أعمدة الإشارة النيونية
              Row(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  _buildBar(14, isConnected: isConnected),
                  const SizedBox(width: 5),
                  _buildBar(22, isConnected: isConnected),
                  const SizedBox(width: 5),
                  _buildBar(30, isConnected: isConnected),
                  const SizedBox(width: 5),
                  _buildBar(38, isConnected: isConnected),
                  const SizedBox(width: 5),
                  _buildBar(46, isConnected: isConnected),
                ],
              ),
              const SizedBox(width: 12),
              // نص حالة الاتصال — Flexible لمنع overflow على الشاشات الصغيرة
              Flexible(
                child: Text(
                  statusText,
                  overflow: TextOverflow.ellipsis,
                  textAlign: TextAlign.end,
                  style: TextStyle(
                    fontSize: 13,
                    fontWeight: FontWeight.w600,
                    color: statusColor,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          if (info == null)
            const CircularProgressIndicator()
          else ...[
            // ── اسم/رمز المشغل في المنتصف ──
            Text(
              info.carrier,
              style: const TextStyle(
                fontSize: 26,
                fontWeight: FontWeight.bold,
                color: Colors.white,
                letterSpacing: 1,
              ),
            ),
            const SizedBox(height: 10),
            // ── النمط الحالي ──
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 6),
              decoration: BoxDecoration(
                color: const Color(0xFF0F2B48).withValues(alpha: 0.6),
                borderRadius: BorderRadius.circular(20),
                border: Border.all(
                  color: const Color(0xFF0284C7).withValues(alpha: 0.35),
                  width: 1,
                ),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Text(
                    'النمط الحالي: ',
                    textDirection: TextDirection.rtl,
                    style: TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.w500,
                      color: Color(0xFF7DD3FC),
                    ),
                  ),
                  Flexible(
                    child: Text(
                      info.networkType,
                      textDirection: TextDirection.ltr,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 10),
            // ── شارة الشريحة متصلة مع أيقونة الرقاقة الذهبية ──
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
              decoration: BoxDecoration(
                color: (info.hasSimCard ? const Color(0xFF14532D) : const Color(0xFF7F1D1D)).withValues(alpha: 0.35),
                borderRadius: BorderRadius.circular(20),
                border: Border.all(
                  color: (info.hasSimCard ? const Color(0xFF22C55E) : const Color(0xFFEF4444)).withValues(alpha: 0.35),
                  width: 1,
                ),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(
                    info.hasSimCard ? Icons.sim_card : Icons.sim_card_alert,
                    size: 16,
                    color: info.hasSimCard ? const Color(0xFFEAB308) : Colors.redAccent,
                  ),
                  const SizedBox(width: 8),
                  Text(
                    info.hasSimCard ? 'الشريحة متصلة' : 'الشريحة غير متصلة',
                    style: TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.w700,
                      color: info.hasSimCard ? const Color(0xFF4ADE80) : Colors.redAccent,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ],
      ),
    );
  }
}
