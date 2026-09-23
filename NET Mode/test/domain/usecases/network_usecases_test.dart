import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/domain/entities/network_info.dart';
import 'package:net_mode/domain/entities/network_mode.dart';
import 'package:net_mode/domain/repositories/network_repository.dart';
import 'package:net_mode/domain/usecases/network_usecases.dart';

class MockNetworkRepository implements NetworkRepository {
  NetworkMode? _savedMode;

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
  Future<NetworkMode?> getPreferredMode() async => _savedMode;

  @override
  Future<void> savePreferredMode(NetworkMode mode) async {
    _savedMode = mode;
  }

  @override
  Future<bool> setNetworkMode(NetworkMode mode) async {
    _savedMode = mode;
    return true;
  }
}

void main() {
  late MockNetworkRepository mockRepo;

  setUp(() {
    mockRepo = MockNetworkRepository();
  });

  test(
    'GetInstantNetworkSnapshotUseCase returns expected network info',
    () async {
      final useCase = GetInstantNetworkSnapshotUseCase(mockRepo);
      final result = await useCase();

      expect(result.carrier, 'Yemen Mobile');
      expect(result.networkType, '4G LTE');
      expect(result.hasSimCard, true);
    },
  );

  test('ManagePreferredModeUseCase saves and reads mode correctly', () async {
    final useCase = ManagePreferredModeUseCase(mockRepo);
    await useCase.save(NetworkMode.lteOnly);
    final current = await useCase.get();

    expect(current, NetworkMode.lteOnly);
  });

  test('SetNetworkModeUseCase applies Yemen presets correctly', () async {
    final useCase = SetNetworkModeUseCase(mockRepo);

    // Yemen Mobile+4G → code 7
    final r1 = await useCase(NetworkMode.yemenMobile4G);
    expect(r1, true);
    expect(mockRepo._savedMode?.networkTypeCode, 7);

    // 3G Yemen Mobile → code 4
    final r2 = await useCase(NetworkMode.yemenMobile3G);
    expect(r2, true);
    expect(mockRepo._savedMode?.networkTypeCode, 4);

    // sabafon+you → code 10
    final r3 = await useCase(NetworkMode.sabafonYou);
    expect(r3, true);
    expect(mockRepo._savedMode?.networkTypeCode, 10);

    // VoLTE → code 11
    final r4 = await useCase(NetworkMode.volte);
    expect(r4, true);
    expect(mockRepo._savedMode?.networkTypeCode, 11);

    // تلقائي → code 0
    final r5 = await useCase(NetworkMode.autoYemen);
    expect(r5, true);
    expect(mockRepo._savedMode?.networkTypeCode, 0);
  });
}
