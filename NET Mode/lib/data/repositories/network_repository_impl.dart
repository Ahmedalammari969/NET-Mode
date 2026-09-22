import '../../domain/entities/network_info.dart';
import '../../domain/entities/network_mode.dart';
import '../../domain/repositories/network_repository.dart';
import '../datasources/radio_device_datasource.dart';

/// Concrete implementation of [NetworkRepository] adhering to Clean Architecture.
///
/// Bridges the Domain layer with platform data sources (MethodChannel & local state).
class NetworkRepositoryImpl implements NetworkRepository {
  final RadioDeviceDataSource _radioDataSource;
  NetworkMode? _cachedPreferredMode;

  NetworkRepositoryImpl({
    required RadioDeviceDataSource radioDataSource,
  }) : _radioDataSource = radioDataSource;

  @override
  Future<NetworkInfo> getInstantNetworkSnapshot() async {
    final rawSnapshot = await _radioDataSource.getInstantNetworkSnapshot();

    return NetworkInfo(
      carrier: rawSnapshot['carrier']?.toString() ?? 'No Carrier',
      networkType: rawSnapshot['networkType']?.toString() ?? 'Unknown',
      hasSimCard: rawSnapshot['simState'] == true,
      isAirplaneMode: false,
    );
  }

  @override
  Future<bool> openRadioTestingSettings() {
    return _radioDataSource.openRadioMenu();
  }

  @override
  Future<void> savePreferredMode(NetworkMode mode) async {
    _cachedPreferredMode = mode;
  }

  @override
  Future<NetworkMode?> getPreferredMode() async {
    return _cachedPreferredMode;
  }

  @override
  Future<bool> setNetworkMode(NetworkMode mode) {
    return _radioDataSource.setNetworkMode(mode.networkTypeCode);
  }
}
