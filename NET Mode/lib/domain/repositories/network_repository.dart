import '../entities/network_info.dart';
import '../entities/network_mode.dart';

abstract class NetworkRepository {
  /// Fetches an instant snapshot of the device's cellular state.
  Future<NetworkInfo> getInstantNetworkSnapshot();

  /// Triggers the native platform settings or hidden radio activity.
  Future<bool> openRadioTestingSettings();

  /// Saves the user's preferred network mode locally.
  Future<void> savePreferredMode(NetworkMode mode);

  /// Retrieves the saved preferred network mode.
  Future<NetworkMode?> getPreferredMode();

  /// Applies the given network mode to the device modem via the platform channel.
  /// Returns true if the mode was applied directly, false if it fell back to the radio UI.
  Future<bool> setNetworkMode(NetworkMode mode);
}
