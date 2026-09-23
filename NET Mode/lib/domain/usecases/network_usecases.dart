import '../entities/network_info.dart';
import '../entities/network_mode.dart';
import '../repositories/network_repository.dart';

class GetInstantNetworkSnapshotUseCase {
  final NetworkRepository _repository;
  const GetInstantNetworkSnapshotUseCase(this._repository);

  Future<NetworkInfo> call() => _repository.getInstantNetworkSnapshot();
}

class OpenRadioSettingsUseCase {
  final NetworkRepository _repository;
  const OpenRadioSettingsUseCase(this._repository);

  Future<bool> call() => _repository.openRadioTestingSettings();
}

class ManagePreferredModeUseCase {
  final NetworkRepository _repository;
  const ManagePreferredModeUseCase(this._repository);

  Future<void> save(NetworkMode mode) => _repository.savePreferredMode(mode);
  Future<NetworkMode?> get() => _repository.getPreferredMode();
}

/// تُرسِل كود RIL الخاص بالنمط المختار مباشرةً إلى مودم الجهاز.
/// تُرجع true إذا طُبِّق التغيير فوراً، أو false إذا فتح التطبيق قائمة الراديو كـ Fallback.
class SetNetworkModeUseCase {
  final NetworkRepository _repository;
  const SetNetworkModeUseCase(this._repository);

  Future<bool> call(NetworkMode mode) => _repository.setNetworkMode(mode);
}
