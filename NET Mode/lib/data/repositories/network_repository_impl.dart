import '../../domain/entities/network_info.dart';
import '../../domain/entities/network_mode.dart';
import '../../domain/repositories/network_repository.dart';
import '../datasources/radio_device_datasource.dart';
import '../datasources/local_preferences_datasource.dart';
import '../models/pattern_history_model.dart';

/// مدمج ومستودع الشبكة الملموس الذي يربط مصادر بيانات الراديو والتفضيلات المحلية
/// ويحقق عقد [NetworkRepository] النطاقي مع توفير محولات النماذج (Model Mappers).
class NetworkRepositoryImpl implements NetworkRepository {
  final RadioDeviceDataSource radioDeviceDataSource;
  final LocalPreferencesDataSource? localPreferencesDataSource;
  NetworkMode? _cachedPreferredMode;

  NetworkRepositoryImpl({
    RadioDeviceDataSource? radioDeviceDataSource,
    RadioDeviceDataSource? radioDataSource,
    this.localPreferencesDataSource,
  }) : radioDeviceDataSource = radioDeviceDataSource ??
            radioDataSource ??
            RadioDeviceDataSourceImpl();

  RadioDeviceDataSource get _radioDataSource => radioDeviceDataSource;

  // ===========================================================================
  // عمليات عقد [NetworkRepository] الأساسية
  // ===========================================================================

  @override
  Future<NetworkInfo> getInstantNetworkSnapshot() async {
    final rawSnapshot = await _radioDataSource.getInstantNetworkSnapshot();

    return NetworkInfo(
      carrier: rawSnapshot['carrier']?.toString() ??
          rawSnapshot['operatorName']?.toString() ??
          'No Carrier',
      networkType: rawSnapshot['networkType']?.toString() ?? 'Unknown',
      hasSimCard: rawSnapshot['simState'] == true,
      isAirplaneMode: rawSnapshot['isAirplaneMode'] == true,
    );
  }

  @override
  Future<bool> openRadioTestingSettings() {
    return _radioDataSource.openRadioMenu();
  }

  @override
  Future<void> savePreferredMode(NetworkMode mode) async {
    _cachedPreferredMode = mode;
    if (localPreferencesDataSource != null) {
      await localPreferencesDataSource!.saveLastAppliedMode(mode.networkTypeCode);
      final historyEntry = PatternHistoryModel(
        id: DateTime.now().millisecondsSinceEpoch.toString(),
        networkMode: mode.networkTypeCode,
        modeName: mode.name,
        timestamp: DateTime.now(),
        isSuccess: true,
      );
      await localPreferencesDataSource!.savePatternHistory(historyEntry);
    }
  }

  @override
  Future<NetworkMode?> getPreferredMode() async {
    if (_cachedPreferredMode != null) {
      return _cachedPreferredMode;
    }
    if (localPreferencesDataSource != null) {
      final savedCode = await localPreferencesDataSource!.getLastAppliedMode();
      if (savedCode != null) {
        for (final m in NetworkMode.standardPresets) {
          if (m.networkTypeCode == savedCode) {
            _cachedPreferredMode = m;
            return m;
          }
        }
      }
    }
    return null;
  }

  @override
  Future<bool> setNetworkMode(NetworkMode mode) async {
    final success = await _radioDataSource.setNetworkMode(mode.networkTypeCode);
    if (success) {
      await savePreferredMode(mode);
    }
    return success;
  }

  // ===========================================================================
  // عمليات Issue #14 وعتاد الراديو المتقدم
  // ===========================================================================

  /// التحقق من حالة تفعيل راديو الهاتف الخلوي.
  Future<bool> isRadioEnabled() async {
    return await radioDeviceDataSource.isRadioEnabled();
  }

  /// جلب نمط الشبكة المفضل الحالي للمنصة.
  Future<int?> getPreferredNetworkMode({int? subId}) async {
    return await radioDeviceDataSource.getPreferredNetworkMode(subId: subId);
  }

  /// تعيين نمط الشبكة المفضل وحفظ العملية وسجلها في التفضيلات المحلية تلقائياً عند النجاح.
  Future<bool> setPreferredNetworkMode({
    required int mode,
    int? subId,
    String? modeName,
  }) async {
    final bool isSuccess = await radioDeviceDataSource.setPreferredNetworkMode(
      mode: mode,
      subId: subId,
    );

    if (isSuccess && localPreferencesDataSource != null) {
      await localPreferencesDataSource!.saveLastAppliedMode(mode);

      final String resolvedModeName = modeName ?? mapNetworkModeToName(mode);
      final PatternHistoryModel historyEntry = PatternHistoryModel(
        id: DateTime.now().millisecondsSinceEpoch.toString(),
        networkMode: mode,
        modeName: resolvedModeName,
        subId: subId,
        timestamp: DateTime.now(),
        isSuccess: true,
      );
      await localPreferencesDataSource!.savePatternHistory(historyEntry);
    }

    return isSuccess;
  }

  /// جلب معلومات وبيانات الشبكة مع تعيينها وتجريدها عبر الـ Mapper.
  Future<Map<String, dynamic>> getNetworkInfo({int? subId}) async {
    final Map<String, dynamic> rawInfo =
        await radioDeviceDataSource.getRawNetworkInfo(subId: subId);
    return mapRawNetworkInfo(rawInfo);
  }

  /// جلب وتعيين هوية البرج والخلية الحالية بأمان وانعدام صارم.
  Future<Map<String, dynamic>?> getCellIdentity({int? subId}) async {
    final Map<String, dynamic>? rawCell =
        await radioDeviceDataSource.getCellIdentity(subId: subId);
    if (rawCell == null) return null;
    return mapRawCellIdentity(rawCell);
  }

  /// جلب قوة الإشارة بوحدة dBm.
  Future<int?> getSignalStrengthDbm({int? subId}) async {
    return await radioDeviceDataSource.getSignalStrengthDbm(subId: subId);
  }

  // ===========================================================================
  // عمليات التفضيلات وسجل الأنماط (Preferences & History Operations)
  // ===========================================================================

  /// استرجاع سجل الأنماط السابقة المحفوظة محلياً.
  Future<List<PatternHistoryModel>> getPatternHistory() async {
    if (localPreferencesDataSource == null) return [];
    return await localPreferencesDataSource!.getPatternHistory();
  }

  /// مسح سجل الأنماط من التخزين المحلي.
  Future<void> clearPatternHistory() async {
    if (localPreferencesDataSource != null) {
      await localPreferencesDataSource!.clearPatternHistory();
    }
  }

  /// استرجاع آخر نمط شبكة تم تطبيقه بنجاح.
  Future<int?> getLastAppliedMode() async {
    if (localPreferencesDataSource == null) return null;
    return await localPreferencesDataSource!.getLastAppliedMode();
  }

  /// حفظ سجل نمط يدوي أو مخصص في التفضيلات المحلية.
  Future<void> savePatternHistory(PatternHistoryModel pattern) async {
    if (localPreferencesDataSource != null) {
      await localPreferencesDataSource!.savePatternHistory(pattern);
    }
  }

  // ===========================================================================
  // محولات النماذج والبيانات الخام (Model & DTO Mappers)
  // ===========================================================================

  /// تحويل كود نمط الشبكة الرقمي (Android Telephony mode integer) إلى اسم وصفي واضح.
  String mapNetworkModeToName(int mode) {
    switch (mode) {
      case 0:
        return 'WCDMA preferred (3G/2G)';
      case 1:
        return 'GSM only (2G)';
      case 2:
        return 'WCDMA only (3G)';
      case 3:
        return 'GSM/WCDMA auto';
      case 9:
        return 'LTE, GSM/WCDMA';
      case 10:
        return 'LTE only (4G)';
      case 11:
        return 'LTE/WCDMA';
      case 12:
        return 'CDMA / EvDo';
      case 20:
        return 'NR only (5G)';
      case 21:
        return 'NR/LTE (5G/4G)';
      case 22:
        return 'NR, LTE, GSM/WCDMA (5G/4G/3G/2G)';
      default:
        return 'Network Mode ($mode)';
    }
  }

  /// تحويل قوة الإشارة بوحدة dBm إلى تصنيف جودة قابل للقراءة للمستخدم.
  String mapSignalDbmToQuality(int? dbm) {
    if (dbm == null) return 'غير متوفر';
    if (dbm >= -80) return 'ممتازة (Excellent)';
    if (dbm >= -95) return 'جيدة جداً (Very Good)';
    if (dbm >= -105) return 'متوسطة (Fair)';
    if (dbm >= -115) return 'ضعيفة (Poor)';
    return 'ضعيفة جداً أو معدومة';
  }

  /// محول بيانات معلومات الشبكة الخام لتجريد الحقول وضمان تناسق الأنواع.
  Map<String, dynamic> mapRawNetworkInfo(Map<String, dynamic> raw) {
    return <String, dynamic>{
      'operatorName': raw['operatorName'] ?? raw['operator'] ?? 'غير معروف',
      'networkType': raw['networkType'] ?? 'Unknown',
      'isDataConnected': raw['isDataConnected'] ?? false,
      'isRoaming': raw['isRoaming'] ?? false,
      'simState': raw['simState'] ?? 'UNKNOWN',
      'carrierId': raw['carrierId'],
      'rawDetails': raw,
    };
  }

  /// محول بيانات هوية البرج والخلية مع التحقق من الحقول المعتادة (CID, LAC, TAC, PCI).
  Map<String, dynamic> mapRawCellIdentity(Map<String, dynamic> raw) {
    return <String, dynamic>{
      'cellId': raw['cid'] ?? raw['cellId'] ?? raw['ci'],
      'areaCode': raw['lac'] ?? raw['tac'] ?? raw['tacCode'],
      'physicalCellId': raw['pci'] ?? raw['psc'],
      'trackingAreaCode': raw['tac'],
      'mcc': raw['mcc'] ?? raw['mccString'],
      'mnc': raw['mnc'] ?? raw['mncString'],
      'rawCellData': raw,
    };
  }
}