import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/data/datasources/radio_device_datasource.dart';
import 'package:net_mode/data/repositories/network_repository_impl.dart';
import 'package:net_mode/domain/entities/network_mode.dart';

class MockRadioDataSource implements RadioDeviceDataSource {
  @override
  Future<Map<String, dynamic>> getInstantNetworkSnapshot() async {
    return {
      'carrier': 'Test Carrier',
      'networkType': '4G LTE',
      'simState': true,
    };
  }

  @override
  Future<bool> openRadioMenu() async => true;

  @override
  Future<bool> setNetworkMode(int networkTypeCode) async => true;
}

void main() {
  late NetworkRepositoryImpl repository;
  late MockRadioDataSource mockDataSource;

  setUp(() {
    mockDataSource = MockRadioDataSource();
    repository = NetworkRepositoryImpl(radioDataSource: mockDataSource);
  });

  test('maps raw data source map to Domain NetworkInfo entity', () async {
    final info = await repository.getInstantNetworkSnapshot();

    expect(info.carrier, 'Test Carrier');
    expect(info.networkType, '4G LTE');
    expect(info.hasSimCard, true);
  });

  test('delegates openRadioMenu to data source', () async {
    final result = await repository.openRadioTestingSettings();
    expect(result, isTrue);
  });

  test('saves and retrieves preferred mode in memory', () async {
    await repository.savePreferredMode(NetworkMode.lteOnly);
    final saved = await repository.getPreferredMode();

    expect(saved, equals(NetworkMode.lteOnly));
  });
}
