import 'dart:async';
import 'package:flutter/material.dart';
import 'data/datasources/radio_device_datasource.dart';
import 'data/repositories/network_repository_impl.dart';
import 'domain/entities/network_info.dart';
import 'domain/entities/network_mode.dart';
import 'domain/usecases/network_usecases.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const NetModeApp());
}

class NetModeApp extends StatelessWidget {
  const NetModeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'NET Mode',
      theme: ThemeData(
        brightness: Brightness.dark,
        scaffoldBackgroundColor: const Color(0xFF0F172A),
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFF38BDF8),
          secondary: Color(0xFF818CF8),
        ),
      ),
      home: const HomeScreen(),
    );
  }
}

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

  /// يُطبِّق النمط المختار على المودم عبر الـ MethodChannel ثم يحفظه.
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
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : SingleChildScrollView(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // ── بطاقة حالة الشبكة الحالية ──
                  _NetworkStatusCard(networkInfo: _networkInfo),
                  const SizedBox(height: 16),

                  // ── زر تغيير نمط شبكة الهاتف (مطابق للصورة) ──
                  Container(
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
                        onTap: _openSettings,
                        child: const Padding(
                          padding: EdgeInsets.symmetric(vertical: 14),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Icon(Icons.settings, color: Color(0xFF38BDF8), size: 20),
                              SizedBox(width: 8),
                              Text(
                                'تغيير نمط شبكة الهاتف',
                                style: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.bold,
                                  color: Color(0xFF38BDF8),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 24),

                  // ── عنوان قسم الأنماط اليمنية (مطابق للصورة) ──
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
                    return _ModeCard(
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

// ─── بطاقة حالة الشبكة الحالية (مطابقة للصورة بدقة) ─────────────────────────
class _NetworkStatusCard extends StatelessWidget {
  final NetworkInfo? networkInfo;

  const _NetworkStatusCard({required this.networkInfo});

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
          // ── السطر العلوي: أعمدة الإشارة في المنتصف و "الشبكة متصلة" على اليمين ──
          SizedBox(
            height: 50,
            child: Stack(
              children: [
                Align(
                  alignment: Alignment.center,
                  child: Row(
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
                ),
                Positioned(
                  right: 4,
                  top: 12,
                  child: Text(
                    statusText,
                    style: TextStyle(
                      fontSize: 14,
                      fontWeight: FontWeight.w600,
                      color: statusColor,
                    ),
                  ),
                ),
              ],
            ),
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
                  Text(
                    info.networkType,
                    textDirection: TextDirection.ltr,
                    style: const TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
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

// ─── بطاقة نمط شبكة واحد (مطابقة للصورة بدقة) ──────────────────────────────
class _ModeCard extends StatelessWidget {
  final NetworkMode mode;
  final bool isSelected;
  final bool isApplying;
  final VoidCallback onTap;

  const _ModeCard({
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
            // ── دائرة الجيل بالحدود الملونة (مطابقة للصورة) ──
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
