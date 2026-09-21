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

  const HomeScreen({
    super.key,
    this.getSnapshotUseCase,
    this.openRadioSettingsUseCase,
    this.managePreferredModeUseCase,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late final GetInstantNetworkSnapshotUseCase _getSnapshotUseCase;
  late final OpenRadioSettingsUseCase _openRadioSettingsUseCase;
  late final ManagePreferredModeUseCase _managePreferredModeUseCase;

  NetworkInfo? _networkInfo;
  NetworkMode? _preferredMode;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    final repo = NetworkRepositoryImpl(radioDataSource: RadioDeviceDataSourceImpl());
    _getSnapshotUseCase = widget.getSnapshotUseCase ?? GetInstantNetworkSnapshotUseCase(repo);
    _openRadioSettingsUseCase = widget.openRadioSettingsUseCase ?? OpenRadioSettingsUseCase(repo);
    _managePreferredModeUseCase = widget.managePreferredModeUseCase ?? ManagePreferredModeUseCase(repo);
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
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(const SnackBar(content: Text('تعذر فتح القائمة مباشرة')));
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
      ),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: const Color(0xFF1E293B),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(
                    color: Colors.blueAccent.withValues(alpha: 0.3),
                  ),
                ),
                child: Column(
                  children: [
                    const Icon(
                      Icons.cell_tower,
                      size: 60,
                      color: Color(0xFF38BDF8),
                    ),
                    const SizedBox(height: 16),
                    _isLoading
                        ? const CircularProgressIndicator()
                        : Column(
                            children: [
                              Text(
                                _networkInfo?.carrier ?? 'Unknown',
                                style: const TextStyle(
                                  fontSize: 22,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                              const SizedBox(height: 8),
                              Text(
                                'النمط الفعلي: ${_networkInfo?.networkType ?? 'Unknown'}',
                                style: const TextStyle(
                                  fontSize: 16,
                                  color: Colors.grey,
                                ),
                              ),
                            ],
                          ),
                  ],
                ),
              ),
              const SizedBox(height: 24),
              ElevatedButton.icon(
                onPressed: _openSettings,
                icon: const Icon(Icons.settings_suggest),
                label: const Text('فتح إعدادات الراديو (LTE Only)'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF0284C7),
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(
                    horizontal: 24,
                    vertical: 16,
                  ),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
              ),
              const SizedBox(height: 16),
              IconButton(
                onPressed: _loadData,
                icon: const Icon(Icons.refresh),
                tooltip: 'تحديث فوري',
              ),
              const SizedBox(height: 24),
              const Align(
                alignment: Alignment.centerRight,
                child: Text(
                  'الأنماط المتاحة:',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: Color(0xFF38BDF8),
                  ),
                ),
              ),
              const SizedBox(height: 12),
              ...NetworkMode.standardPresets.map((mode) {
                final isSelected = _preferredMode?.id == mode.id;
                return Container(
                  margin: const EdgeInsets.only(bottom: 8),
                  decoration: BoxDecoration(
                    color: isSelected
                        ? const Color(0xFF0284C7).withValues(alpha: 0.2)
                        : const Color(0xFF1E293B),
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(
                      color: isSelected
                          ? const Color(0xFF38BDF8)
                          : Colors.transparent,
                    ),
                  ),
                  child: ListTile(
                    title: Text(
                      mode.name,
                      style: const TextStyle(fontWeight: FontWeight.w600),
                    ),
                    subtitle: Text(
                      mode.description,
                      style: const TextStyle(fontSize: 12, color: Colors.grey),
                    ),
                    trailing: isSelected
                        ? const Icon(Icons.check_circle, color: Color(0xFF38BDF8))
                        : null,
                    onTap: () async {
                      await _managePreferredModeUseCase.save(mode);
                      setState(() {
                        _preferredMode = mode;
                      });
                    },
                  ),
                );
              }),
            ],
          ),
        ),
      ),
    );
  }
}
