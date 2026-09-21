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
}
