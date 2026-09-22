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

class _HomeScreenState extends State<HomeScreen> {
  late final GetInstantNetworkSnapshotUseCase _getSnapshotUseCase;
  late final OpenRadioSettingsUseCase _openRadioSettingsUseCase;
  late final ManagePreferredModeUseCase _managePreferredModeUseCase;
  late final SetNetworkModeUseCase _setNetworkModeUseCase;

  NetworkInfo? _networkInfo;
  NetworkMode? _preferredMode;
  bool _isLoading = true;
  bool _isApplying = false;

  @override
  void initState() {
    super.initState();
    final repo = NetworkRepositoryImpl(radioDataSource: RadioDeviceDataSourceImpl());
    _getSnapshotUseCase = widget.getSnapshotUseCase ?? GetInstantNetworkSnapshotUseCase(repo);
    _openRadioSettingsUseCase = widget.openRadioSettingsUseCase ?? OpenRadioSettingsUseCase(repo);
    _managePreferredModeUseCase = widget.managePreferredModeUseCase ?? ManagePreferredModeUseCase(repo);
    _setNetworkModeUseCase = widget.setNetworkModeUseCase ?? SetNetworkModeUseCase(repo);
    _loadData();
  }

  Future<void> _loadData() async {
    setState(() => _isLoading = true);
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
                : '⚠️ فُتحت قائمة الراديو — اختر النمط يدوياً',
          ),
          backgroundColor: applied ? const Color(0xFF0369A1) : const Color(0xFF92400E),
          duration: const Duration(seconds: 3),
        ),
      );
      // تحديث قراءة الشبكة في الإطار التالي بعد التغيير
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

                  // ── زر فتح إعدادات الراديو المخفية ──
                  ElevatedButton.icon(
                    onPressed: _openSettings,
                    icon: const Icon(Icons.settings_suggest),
                    label: const Text('تغيير نمط شبكة الهاتف'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF38BDF8),
                      foregroundColor: const Color(0xFF0F172A),
                      padding: const EdgeInsets.symmetric(vertical: 16),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(14),
                      ),
                      textStyle: const TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  const SizedBox(height: 28),

                  // ── عنوان قسم الأنماط اليمنية ──
                  const Align(
                    alignment: Alignment.centerRight,
                    child: Text(
                      ':اختر نمط الشبكة',
                      style: TextStyle(
                        fontSize: 17,
                        fontWeight: FontWeight.bold,
                        color: Color(0xFF38BDF8),
                      ),
                    ),
                  ),
                  const SizedBox(height: 12),

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

// ─── بطاقة عرض حالة الشبكة الحالية ───────────────────────────────────────
class _NetworkStatusCard extends StatelessWidget {
  final NetworkInfo? networkInfo;
  const _NetworkStatusCard({required this.networkInfo});

  @override
  Widget build(BuildContext context) {
    final info = networkInfo;
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: const Color(0xFF1E293B),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFF38BDF8).withValues(alpha: 0.25)),
      ),
      child: Column(
        children: [
          const Icon(Icons.cell_tower, size: 56, color: Color(0xFF38BDF8)),
          const SizedBox(height: 12),
          if (info == null)
            const CircularProgressIndicator()
          else ...[
            Text(
              info.carrier,
              style: const TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
            const SizedBox(height: 6),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 5),
              decoration: BoxDecoration(
                color: const Color(0xFF0369A1).withValues(alpha: 0.4),
                borderRadius: BorderRadius.circular(20),
              ),
              child: Text(
                'النمط الفعلي: ${info.networkType}',
                style: const TextStyle(fontSize: 14, color: Color(0xFF7DD3FC)),
              ),
            ),
            const SizedBox(height: 8),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  info.hasSimCard ? Icons.sim_card : Icons.sim_card_alert,
                  size: 18,
                  color: info.hasSimCard ? Colors.greenAccent : Colors.redAccent,
                ),
                const SizedBox(width: 6),
                Text(
                  info.hasSimCard ? 'الشريحة جاهزة (SIM Ready)' : 'لا توجد شريحة',
                  style: TextStyle(
                    fontSize: 13,
                    color: info.hasSimCard ? Colors.greenAccent : Colors.redAccent,
                  ),
                ),
              ],
            ),
          ],
        ],
      ),
    );
  }
}

// ─── بطاقة نمط شبكة واحد ──────────────────────────────────────────────────
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

  IconData get _icon {
    if (!mode.isLockMode) return Icons.autorenew;
    return Icons.lock_outline;
  }

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
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        decoration: BoxDecoration(
          color: isSelected
              ? const Color(0xFF0284C7).withValues(alpha: 0.18)
              : const Color(0xFF1E293B),
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isSelected ? const Color(0xFF38BDF8) : Colors.transparent,
            width: 1.5,
          ),
        ),
        child: Row(
          children: [
            // أيقونة النمط
            Container(
              width: 44,
              height: 44,
              decoration: BoxDecoration(
                color: _generationColor.withValues(alpha: isSelected ? 0.25 : 0.12),
                shape: BoxShape.circle,
              ),
              child: Icon(_icon, color: _generationColor, size: 22),
            ),
            const SizedBox(width: 14),
            // اسم النمط والوصف
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    mode.name,
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w700,
                      color: isSelected ? const Color(0xFF38BDF8) : Colors.white,
                    ),
                  ),
                  const SizedBox(height: 3),
                  Text(
                    mode.description,
                    style: const TextStyle(fontSize: 12, color: Color(0xFF94A3B8)),
                  ),
                ],
              ),
            ),
            // مؤشر التحديد أو التحميل
            if (isSelected && isApplying)
              const SizedBox(
                width: 22,
                height: 22,
                child: CircularProgressIndicator(strokeWidth: 2),
              )
            else if (isSelected)
              const Icon(Icons.check_circle, color: Color(0xFF38BDF8), size: 24),
          ],
        ),
      ),
    );
  }
}
