import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/data/datasources/local_preferences_datasource.dart';
import 'package:net_mode/data/datasources/radio_device_datasource.dart';
import 'package:net_mode/data/models/pattern_history_model.dart';
import 'package:net_mode/data/repositories/network_repository_impl.dart';
import 'package:net_mode/domain/entities/network_mode.dart';

class FakeRadioDataSource implements RadioDeviceDataSource {
  bool radioEnabled = true;
  bool setModeSuccess = true;
  int? lastSetMode;
  int? lastSetSubId;

  @override
  Future<Map<String, dynamic>> getInstantNetworkSnapshot() async {
    return {
      'carrier': 'Test Carrier',
      'networkType': '4G LTE',
      'simState': true,
      'isAirplaneMode': false,
    };
  }

  @override
  Future<bool> openRadioMenu() async => true;

  @override
  Future<bool> setNetworkMode(int networkTypeCode) async => setModeSuccess;

  @override
  Future<bool> isRadioEnabled() async => radioEnabled;

  @override
  Future<int?> getPreferredNetworkMode({int? subId}) async => 9;

  @override
  Future<bool> setPreferredNetworkMode({required int mode, int? subId}) async {
    lastSetMode = mode;
    lastSetSubId = subId;
    return setModeSuccess;
  }

  @override
  Future<Map<String, dynamic>> getRawNetworkInfo({int? subId}) async => {
        'operatorName': 'TestCarrier',
        'networkType': 'LTE',
      };

  @override
  Future<Map<String, dynamic>?> getCellIdentity({int? subId}) async => null;

  @override
  Future<int?> getSignalStrengthDbm({int? subId}) async => -85;

  @override
  Future<dynamic> invokeRawMethod(String method, [dynamic arguments]) async => null;
}

class FakePreferencesDataSource implements LocalPreferencesDataSource {
  int? savedLastAppliedMode;
  final List<PatternHistoryModel> savedHistory = [];

  @override
  Future<void> saveLastAppliedMode(int mode) async {
    savedLastAppliedMode = mode;
  }

  @override
  Future<int?> getLastAppliedMode() async => savedLastAppliedMode;

  @override
  Future<void> savePatternHistory(PatternHistoryModel pattern) async {
    savedHistory.insert(0, pattern);
  }

  @override
  Future<List<PatternHistoryModel>> getPatternHistory() async => savedHistory;

  @override
  Future<void> clearPatternHistory() async => savedHistory.clear();

  @override
  Future<void> setStringPreference(String key, String value) async {}

  @override
  Future<String?> getStringPreference(String key) async => null;

  @override
  Future<void> setBoolPreference(String key, bool value) async {}

  @override
  Future<bool?> getBoolPreference(String key) async => null;

  @override
  Future<void> clearAllPreferences() async {
    savedLastAppliedMode = null;
    savedHistory.clear();
  }
}

void main() {
  late NetworkRepositoryImpl repository;
  late FakeRadioDataSource fakeRadio;
  late FakePreferencesDataSource fakePrefs;

  setUp(() {
    fakeRadio = FakeRadioDataSource();
    fakePrefs = FakePreferencesDataSource();
    repository = NetworkRepositoryImpl(
      radioDeviceDataSource: fakeRadio,
      localPreferencesDataSource: fakePrefs,
    );
  });

  group('NetworkRepositoryImpl Base Domain Operations', () {
    test('maps raw data source map to Domain NetworkInfo entity', () async {
      final info = await repository.getInstantNetworkSnapshot();

      expect(info.carrier, 'Test Carrier');
      expect(info.networkType, '4G LTE');
      expect(info.hasSimCard, true);
      expect(info.isAirplaneMode, false);
    });

    test('delegates openRadioMenu to data source', () async {
      final result = await repository.openRadioTestingSettings();
      expect(result, isTrue);
    });

    test('saves and retrieves preferred mode with local persistence', () async {
      await repository.savePreferredMode(NetworkMode.lteOnly);
      final saved = await repository.getPreferredMode();

      expect(saved, equals(NetworkMode.lteOnly));
      expect(fakePrefs.savedLastAppliedMode, NetworkMode.lteOnly.networkTypeCode);
      expect(fakePrefs.savedHistory.length, 1);
    });
  });

  group('Issue #14: NetworkRepositoryImpl with Model Mappers & Telemetry', () {
    test('isRadioEnabled delegates to radio device data source', () async {
      fakeRadio.radioEnabled = true;
      expect(await repository.isRadioEnabled(), isTrue);

      fakeRadio.radioEnabled = false;
      expect(await repository.isRadioEnabled(), isFalse);
    });

    test('setPreferredNetworkMode updates device and stores history on success', () async {
      fakeRadio.setModeSuccess = true;
      final result = await repository.setPreferredNetworkMode(
        mode: 20,
        subId: 1,
        modeName: 'NR 5G',
      );

      expect(result, isTrue);
      expect(fakeRadio.lastSetMode, 20);
      expect(fakeRadio.lastSetSubId, 1);
      expect(fakePrefs.savedLastAppliedMode, 20);
      expect(fakePrefs.savedHistory.length, 1);
      expect(fakePrefs.savedHistory.first.networkMode, 20);
      expect(fakePrefs.savedHistory.first.modeName, 'NR 5G');
    });

    test('setPreferredNetworkMode does not store history if device call fails', () async {
      fakeRadio.setModeSuccess = false;
      final result = await repository.setPreferredNetworkMode(mode: 10);

      expect(result, isFalse);
      expect(fakePrefs.savedLastAppliedMode, isNull);
      expect(fakePrefs.savedHistory, isEmpty);
    });

    test('mapNetworkModeToName accurately maps telephony mode integers', () {
      expect(repository.mapNetworkModeToName(0), contains('WCDMA preferred'));
      expect(repository.mapNetworkModeToName(1), contains('GSM only'));
      expect(repository.mapNetworkModeToName(9), contains('LTE, GSM/WCDMA'));
      expect(repository.mapNetworkModeToName(10), contains('LTE only (4G)'));
      expect(repository.mapNetworkModeToName(20), contains('NR only (5G)'));
      expect(repository.mapNetworkModeToName(22), contains('NR, LTE, GSM/WCDMA'));
      expect(repository.mapNetworkModeToName(999), 'Network Mode (999)');
    });

    test('mapSignalDbmToQuality classifies dBm signal strength accurately', () {
      expect(repository.mapSignalDbmToQuality(null), 'غير متوفر');
      expect(repository.mapSignalDbmToQuality(-75), contains('ممتازة'));
      expect(repository.mapSignalDbmToQuality(-90), contains('جيدة جداً'));
      expect(repository.mapSignalDbmToQuality(-100), contains('متوسطة'));
      expect(repository.mapSignalDbmToQuality(-110), contains('ضعيفة'));
      expect(repository.mapSignalDbmToQuality(-125), contains('ضعيفة جداً'));
    });

    test('mapRawNetworkInfo abstracts raw telephony dictionary into clean contract', () {
      final mapped = repository.mapRawNetworkInfo({
        'operator': 'Carrier X',
        'networkType': '5G_SA',
        'isDataConnected': true,
        'isRoaming': false,
        'simState': 'READY',
      });

      expect(mapped['operatorName'], 'Carrier X');
      expect(mapped['networkType'], '5G_SA');
      expect(mapped['isDataConnected'], true);
      expect(mapped['isRoaming'], false);
      expect(mapped['simState'], 'READY');
      expect(mapped['rawDetails'], isA<Map>());
    });

    test('mapRawCellIdentity abstracts cell tower identity parameters safely', () {
      final mapped = repository.mapRawCellIdentity({
        'cellId': 98765,
        'tac': 321,
        'pci': 111,
        'mcc': '421',
        'mnc': '01',
      });

      expect(mapped['cellId'], 98765);
      expect(mapped['areaCode'], 321);
      expect(mapped['physicalCellId'], 111);
      expect(mapped['trackingAreaCode'], 321);
      expect(mapped['mcc'], '421');
      expect(mapped['mnc'], '01');
    });
  });
}
