import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/domain/entities/network_info.dart';
import 'package:net_mode/domain/entities/network_mode.dart';
import 'package:net_mode/domain/repositories/network_repository.dart';
import 'package:net_mode/domain/usecases/network_usecases.dart';
import 'package:net_mode/main.dart';
import 'package:flutter/material.dart';

class FakeNetworkRepository implements NetworkRepository {
  NetworkMode? _mode = NetworkMode.lteOnly;

  @override
  Future<NetworkInfo> getInstantNetworkSnapshot() async {
    return const NetworkInfo(
      carrier: 'Yemen Mobile',
      networkType: '4G LTE',
      hasSimCard: true,
    );
  }

  @override
  Future<bool> openRadioTestingSettings() async => true;

  @override
  Future<NetworkMode?> getPreferredMode() async => _mode;

  @override
  Future<void> savePreferredMode(NetworkMode mode) async {
    _mode = mode;
  }
}

void main() {
  testWidgets('NetMode HomeScreen renders network telemetry and modes', (
    WidgetTester tester,
  ) async {
    final fakeRepo = FakeNetworkRepository();
    final getSnapshot = GetInstantNetworkSnapshotUseCase(fakeRepo);
    final openRadio = OpenRadioSettingsUseCase(fakeRepo);
    final manageMode = ManagePreferredModeUseCase(fakeRepo);

    await tester.pumpWidget(
      MaterialApp(
        home: HomeScreen(
          getSnapshotUseCase: getSnapshot,
          openRadioSettingsUseCase: openRadio,
          managePreferredModeUseCase: manageMode,
        ),
      ),
    );

    // Initial frame
    expect(find.text('NET Mode - التحكم بالشبكة'), findsOneWidget);

    // Let async loading finish
    await tester.pump();

    // Verify snapshot loaded from domain
    expect(find.text('Yemen Mobile'), findsOneWidget);
    expect(find.text('النمط الفعلي: 4G LTE'), findsOneWidget);

    // Verify preset modes are present
    expect(find.text('LTE Only'), findsOneWidget);
    expect(find.text('NR Only (5G)'), findsOneWidget);
  });
}
