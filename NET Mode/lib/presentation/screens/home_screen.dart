import 'dart:async';
import 'package:flutter/material.dart';
import '../../data/datasources/radio_device_datasource.dart';
import '../../data/repositories/network_repository_impl.dart';
import '../../domain/entities/network_info.dart';
import '../../domain/entities/network_mode.dart';
import '../../domain/usecases/network_usecases.dart';
import '../widgets/network_status_card.dart';
import '../widgets/mode_card.dart';
import '../widgets/radio_action_button.dart';

/// الشاشة الرئيسية للتطبيق — تعرض حالة الشبكة وأنماط الاتصال اليمنية.
///
/// تُدمج فيها:
/// - [FR-21] زر الإجراء التفاعلي البارز (RadioActionButton).
/// - [FR-22] زر التحديث الفوري الدائري أسفل الشاشة (FloatingActionButton).
/// - [FR-23] نظام التنبيهات المنبثقة التوجيهية (SnackBars).
/// - [US-24] التجاوب الكامل مع الشاشات (SingleChildScrollView + EdgeInsets).
class HomeScreen extends StatefulWidget {
  final GetInstantNetworkSnapshotUseCase? getSnapshotUseCase;
  final OpenRadioSettingsUseCase? openRadioSettingsUseCase;
  final ManagePreferredModeUseCase? managePreferredModeUseCase;
  final SetNetworkModeUseCase? setNetworkModeUseCase;

  const HomeScreen({
    super.key,
    this.getSnapshotUseCase,
    this.openRadioSettingsUseCase,
    this.managePreferredModeUseCase,
    this.setNetworkModeUseCase,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> with WidgetsBindingObserver {
  late final GetInstantNetworkSnapshotUseCase _getSnapshotUseCase;
  late final OpenRadioSettingsUseCase _openRadioSettingsUseCase;
  late final ManagePreferredModeUseCase _managePreferredModeUseCase;
  late final SetNetworkModeUseCase _setNetworkModeUseCase;

  NetworkInfo? _networkInfo;
  NetworkMode? _preferredMode;
  bool _isLoading = true;
  bool _isApplying = false;
  Timer? _refreshTimer;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    final repo = NetworkRepositoryImpl(radioDataSource: RadioDeviceDataSourceImpl());
    _getSnapshotUseCase = widget.getSnapshotUseCase ?? GetInstantNetworkSnapshotUseCase(repo);
    _openRadioSettingsUseCase = widget.openRadioSettingsUseCase ?? OpenRadioSettingsUseCase(repo);
    _managePreferredModeUseCase = widget.managePreferredModeUseCase ?? ManagePreferredModeUseCase(repo);
    _setNetworkModeUseCase = widget.setNetworkModeUseCase ?? SetNetworkModeUseCase(repo);
    _loadData();

    // تحديث دوري كل 3 ثوانٍ لالتقاط أي تغيير فوري في الشبكة أو وضع الطيران
    _refreshTimer = Timer.periodic(const Duration(seconds: 3), (_) {
      if (mounted) _loadData(showIndicator: false);
    });
  }

  @override
  void dispose() {
    _refreshTimer?.cancel();
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.resumed) {
      _loadData(showIndicator: false);
    }
  }

  /// [FR-22] يجلب بيانات الشبكة اللحظية ويُعيد بناء الواجهة عبر setState.
  Future<void> _loadData({bool showIndicator = true}) async {
    if (showIndicator && _networkInfo == null) {
      setState(() => _isLoading = true);
    }
    final snapshot = await _getSnapshotUseCase();
    final preferred = await _managePreferredModeUseCase.get();
    if (mounted) {
      setState(() {
        _networkInfo = snapshot;
        _preferredMode = preferred;
        _isLoading = false;
      });
    }
  }

  /// [FR-23] يفتح إعدادات الراديو مع إظهار SnackBar توجيهي عربي عند التعذر.
  Future<void> _openSettings() async {
    final success = await _openRadioSettingsUseCase();
    if (!success && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('تعذر فتح قائمة الراديو — جرب مشغّل آخر أو افتح الإعدادات يدوياً'),
          backgroundColor: Color(0xFF7C3AED),
        ),
      );
    }
  }

  /// [FR-23] يُطبِّق النمط المختار على المودم ويعرض SnackBar تأكيدي أو إرشادي.
  Future<void> _applyMode(NetworkMode mode) async {
    if (_isApplying) return; // منع الضغط المتكرر (Debounce)
    setState(() => _isApplying = true);

    final applied = await _setNetworkModeUseCase(mode);
    await _managePreferredModeUseCase.save(mode);

    if (mounted) {
      setState(() {
        _preferredMode = mode;
        _isApplying = false;
      });
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            applied
                ? '✅ تم تطبيق نمط "${mode.name}" بنجاح'
                : '📲 افتحت صفحة الإعدادات — اختر من القائمة: ${mode.description}',
          ),
          backgroundColor: applied ? const Color(0xFF0369A1) : const Color(0xFF1D4ED8),
          duration: const Duration(seconds: 4),
          behavior: SnackBarBehavior.floating,
        ),
      );// تحديث قراءة الشبكة في الإطار التالي بعد التغيير
      WidgetsBinding.instance.addPostFrameCallback((_) {
        if (mounted) _loadData();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('NET Mode - التحكم بالشبكة'),
        centerTitle: true,
        backgroundColor: Colors.transparent,
        elevation: 0,
        actions: [
          IconButton(
            onPressed: _loadData,
            icon: const Icon(Icons.refresh),
            tooltip: 'تحديث فوري',
          ),
        ],
      ),

      // ── [FR-22 / US-22] زر التحديث الفوري الدائري أسفل الشاشة ──
      // DoD:
      //   ✅ وضع زر تحديث دائري أسفل الشاشة مع أيقونة Icons.refresh.
      //   ✅ إضافة تلميح توصيفي للمستخدم (Tooltip): 'تحديث فوري'.
      //   ✅ ربط الزر بدالة _loadData() وإعادة بناء الواجهة عبر setState.
      //   ✅ إظهار مؤشر التحميل المؤقت أثناء عملية التحديث اللحظي.
      floatingActionButton: FloatingActionButton(
        onPressed: _isLoading ? null : _loadData,
        tooltip: 'تحديث فوري',
        backgroundColor: const Color(0xFF0284C7),
        child: _isLoading
            ? const SizedBox(
                width: 24,
                height: 24,
                child: CircularProgressIndicator(
                  strokeWidth: 2.5,
                  color: Colors.white,
                ),
              )
            : const Icon(Icons.refresh, color: Colors.white),
      ),

      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : SingleChildScrollView(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // ── بطاقة حالة الشبكة الحالية ──
                  NetworkStatusCard(networkInfo: _networkInfo),
                  const SizedBox(height: 16),

                  // ── [FR-21] زر تغيير نمط شبكة الهاتف ──
                  RadioActionButton(onPressed: _openSettings),
                  const SizedBox(height: 24),

                  // ── عنوان قسم الأنماط اليمنية ──
                  const Align(
                    alignment: Alignment.centerRight,
                    child: Text(
                      'اختر نمط الشبكة:',
                      textDirection: TextDirection.rtl,
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                        color: Color(0xFF7DD3FC),
                      ),
                    ),
                  ),
                  const SizedBox(height: 14),

                  // ── قائمة الأنماط اليمنية الخمسة ──
                  ...NetworkMode.yemenPresets.map((mode) {
                    return ModeCard(
                      mode: mode,
                      isSelected: _preferredMode?.id == mode.id,
                      isApplying: _isApplying,
                      onTap: () => _applyMode(mode),
                    );
                  }),
                ],
              ),
            ),
    );
  }
}
