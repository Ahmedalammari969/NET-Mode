import 'dart:convert';
import 'dart:io';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'package:net_mode/core/errors/exceptions.dart';
import 'package:net_mode/core/errors/failures.dart';
import 'package:net_mode/core/permissions/permission_handler.dart';
import 'package:net_mode/data/datasources/local_preferences_datasource.dart';
import 'package:net_mode/data/datasources/radio_device_datasource.dart';
import 'package:net_mode/data/models/pattern_history_model.dart';
import 'package:net_mode/data/repositories/network_repository_impl.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('Issue #17: Unified Failures and Exception Architecture', () {
    test('Exceptions instantiate correctly with message, code and details', () {
      const devEx = DeviceException(
        message: 'Modem error',
        code: 'MODEM_01',
        details: {'info': 'failed'},
      );
      expect(devEx.message, 'Modem error');
      expect(devEx.code, 'MODEM_01');
      expect(devEx.details, {'info': 'failed'});
      expect(devEx.toString(), contains('DeviceException'));

      const permEx = PermissionException(message: 'Permission denied', code: 'PERM_DENIED');
      expect(permEx.message, 'Permission denied');

      const cacheEx = CacheException(message: 'Cache read error');
      expect(cacheEx.message, 'Cache read error');

      const netEx = NetworkException(message: 'Network offline');
      expect(netEx.message, 'Network offline');

      const unexpEx = UnexpectedException(message: 'Unknown crash');
      expect(unexpEx.message, 'Unknown crash');
    });

    test('Failure.fromException maps DeviceException to DeviceFailure', () {
      const ex = DeviceException(message: 'Radio fail', code: 'ERR_RADIO');
      final failure = Failure.fromException(ex);
      expect(failure, isA<DeviceFailure>());
      expect(failure.message, 'Radio fail');
      expect(failure.code, 'ERR_RADIO');
    });

    test('Failure.fromException maps PermissionException to PermissionFailure', () {
      const ex = PermissionException(message: 'No READ_PHONE_STATE', code: 'PERM_ERR');
      final failure = Failure.fromException(ex);
      expect(failure, isA<PermissionFailure>());
      expect(failure.message, 'No READ_PHONE_STATE');
      expect(failure.code, 'PERM_ERR');
    });

    test('Failure.fromException maps CacheException to CacheFailure', () {
      const ex = CacheException(message: 'Corrupt storage');
      final failure = Failure.fromException(ex);
      expect(failure, isA<CacheFailure>());
      expect(failure.message, 'Corrupt storage');
    });

    test('Failure.fromException maps NetworkException to NetworkFailure', () {
      const ex = NetworkException(message: 'Cellular disconnected');
      final failure = Failure.fromException(ex);
      expect(failure, isA<NetworkFailure>());
      expect(failure.message, 'Cellular disconnected');
    });

    test('Failure.fromException maps unexpected exceptions to UnexpectedFailure', () {
      final failure = Failure.fromException(FormatException('Bad input'));
      expect(failure, isA<UnexpectedFailure>());
      expect(failure.message, contains('FormatException'));
    });

    test('Failures support value equality and hashCode', () {
      const f1 = DeviceFailure(message: 'Err', code: 'C1');
      const f2 = DeviceFailure(message: 'Err', code: 'C1');
      const f3 = DeviceFailure(message: 'Different', code: 'C1');

      expect(f1, equals(f2));
      expect(f1.hashCode, equals(f2.hashCode));
      expect(f1 == f3, isFalse);
    });
  });

  group('Issue #13: RadioDeviceDataSourceImpl via MethodChannel', () {
    const channelName = RadioDeviceDataSourceImpl.defaultChannelName;
    late List<MethodCall> methodCalls;
    late RadioDeviceDataSourceImpl dataSource;

    setUp(() {
      methodCalls = <MethodCall>[];
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(const MethodChannel(channelName), (call) async {
        methodCalls.add(call);
        switch (call.method) {
          case 'isRadioEnabled':
            return true;
          case 'getPreferredNetworkMode':
            return 9; // LTE, GSM/WCDMA
          case 'setPreferredNetworkMode':
            return true;
          case 'getRawNetworkInfo':
            return <String, dynamic>{
              'operatorName': 'TestCarrier',
              'networkType': 'LTE',
              'isDataConnected': true,
            };
          case 'getCellIdentity':
            return <String, dynamic>{
              'cid': 12345,
              'lac': 678,
              'pci': 42,
            };
          case 'getSignalStrengthDbm':
            return -85;
          case 'customMethod':
            return 'customResult';
          default:
            return null;
        }
      });
      dataSource = RadioDeviceDataSourceImpl();
    });

    tearDown(() {
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(const MethodChannel(channelName), null);
    });

    test('isRadioEnabled returns true when channel responds true', () async {
      final result = await dataSource.isRadioEnabled();
      expect(result, isTrue);
      expect(methodCalls.first.method, 'isRadioEnabled');
    });

    test('getPreferredNetworkMode passes subId and returns mode integer', () async {
      final mode = await dataSource.getPreferredNetworkMode(subId: 1);
      expect(mode, 9);
      expect(methodCalls.first.arguments, {'subId': 1});
    });

    test('setPreferredNetworkMode sends mode and optional subId', () async {
      final success = await dataSource.setPreferredNetworkMode(mode: 20, subId: 2);
      expect(success, isTrue);
      expect(methodCalls.first.arguments, {'networkMode': 20, 'subId': 2});
    });

    test('getRawNetworkInfo retrieves map safely', () async {
      final info = await dataSource.getRawNetworkInfo();
      expect(info['operatorName'], 'TestCarrier');
      expect(info['networkType'], 'LTE');
      expect(info['isDataConnected'], true);
    });

    test('getCellIdentity retrieves cell data safely', () async {
      final cell = await dataSource.getCellIdentity();
      expect(cell, isNotNull);
      expect(cell!['cid'], 12345);
      expect(cell['pci'], 42);
    });

    test('getSignalStrengthDbm retrieves signal in dBm', () async {
      final dbm = await dataSource.getSignalStrengthDbm();
      expect(dbm, -85);
    });

    test('invokeRawMethod executes generic method', () async {
      final res = await dataSource.invokeRawMethod('customMethod', {'arg': 1});
      expect(res, 'customResult');
    });

    test('MethodChannel PlatformException is caught and wrapped in RadioDeviceException', () async {
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(const MethodChannel(channelName), (call) async {
        throw PlatformException(code: 'HARDWARE_ERR', message: 'Radio off');
      });

      expect(
        () async => await dataSource.isRadioEnabled(),
        throwsA(isA<RadioDeviceException>().having(
          (e) => e.code,
          'code',
          'HARDWARE_ERR',
        )),
      );
    });
  });

  group('Issue #15: LocalPreferencesDataSource & PatternHistoryModel', () {
    test('PatternHistoryModel serialization & deserialization round-trip', () {
      final model = PatternHistoryModel(
        id: '123456789',
        networkMode: 20,
        modeName: 'NR only (5G)',
        subId: 1,
        timestamp: DateTime.parse('2026-09-25T12:00:00.000Z'),
        isSuccess: true,
        extraData: {'band': 'n78'},
      );

      final jsonMap = model.toJson();
      expect(jsonMap['id'], '123456789');
      expect(jsonMap['networkMode'], 20);
      expect(jsonMap['modeName'], 'NR only (5G)');
      expect(jsonMap['extraData'], {'band': 'n78'});

      final restored = PatternHistoryModel.fromJson(jsonMap);
      expect(restored.id, model.id);
      expect(restored.networkMode, model.networkMode);
      expect(restored.modeName, model.modeName);
      expect(restored.subId, model.subId);
      expect(restored.timestamp, model.timestamp);
      expect(restored.isSuccess, model.isSuccess);
      expect(restored.extraData, model.extraData);
      expect(restored, equals(model));
    });

    test('PatternHistoryModel handles missing or null JSON fields safely', () {
      final restored = PatternHistoryModel.fromJson({});
      expect(restored.id, '');
      expect(restored.networkMode, 0);
      expect(restored.modeName, '');
      expect(restored.subId, isNull);
      expect(restored.isSuccess, isTrue);
      expect(restored.extraData, isNull);
    });

    test('LocalPreferencesDataSourceImpl saves, retrieves, and clears history & preferences', () async {
      SharedPreferences.setMockInitialValues({});
      final prefs = await SharedPreferences.getInstance();
      final dataSource = LocalPreferencesDataSourceImpl(sharedPreferences: prefs);

      // Verify empty history initially
      final initialHistory = await dataSource.getPatternHistory();
      expect(initialHistory, isEmpty);

      // Save history entry
      final entry = PatternHistoryModel(
        id: 'entry_1',
        networkMode: 9,
        modeName: 'LTE, GSM/WCDMA',
        timestamp: DateTime.now(),
      );
      await dataSource.savePatternHistory(entry);

      final historyAfter = await dataSource.getPatternHistory();
      expect(historyAfter.length, 1);
      expect(historyAfter.first.id, 'entry_1');
      expect(historyAfter.first.networkMode, 9);

      // Save last applied mode
      await dataSource.saveLastAppliedMode(20);
      final lastMode = await dataSource.getLastAppliedMode();
      expect(lastMode, 20);

      // String and Bool preferences
      await dataSource.setStringPreference('pref_theme', 'dark');
      expect(await dataSource.getStringPreference('pref_theme'), 'dark');

      await dataSource.setBoolPreference('pref_auto_switch', true);
      expect(await dataSource.getBoolPreference('pref_auto_switch'), isTrue);

      // Clear pattern history
      await dataSource.clearPatternHistory();
      expect(await dataSource.getPatternHistory(), isEmpty);
      expect(await dataSource.getLastAppliedMode(), 20); // other pref untouched

      // Clear all preferences
      await dataSource.clearAllPreferences();
      expect(await dataSource.getLastAppliedMode(), isNull);
      expect(await dataSource.getStringPreference('pref_theme'), isNull);
    });
  });

  group('Issue #14: NetworkRepositoryImpl with Model Mappers', () {
    late FakeRadioDataSource fakeRadio;
    late FakePreferencesDataSource fakePrefs;
    late NetworkRepositoryImpl repository;

    setUp(() {
      fakeRadio = FakeRadioDataSource();
      fakePrefs = FakePreferencesDataSource();
      repository = NetworkRepositoryImpl(
        radioDeviceDataSource: fakeRadio,
        localPreferencesDataSource: fakePrefs,
      );
    });

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

  group('Issue #16: Phone State Permission Handler & Manifest', () {
    const channelName = PermissionHandler.defaultChannelName;
    late List<MethodCall> calls;
    late PermissionHandler handler;

    setUp(() {
      calls = <MethodCall>[];
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(const MethodChannel(channelName), (call) async {
        calls.add(call);
        switch (call.method) {
          case 'checkPhoneStatePermission':
            return true;
          case 'requestPhoneStatePermission':
            return 'granted';
          case 'shouldShowRequestPermissionRationale':
            return false;
          default:
            return null;
        }
      });
      handler = const PermissionHandler();
    });

    tearDown(() {
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(const MethodChannel(channelName), null);
    });

    test('isPhoneStatePermissionGranted returns true when granted', () async {
      expect(await handler.isPhoneStatePermissionGranted(), isTrue);
      expect(calls.first.method, 'checkPhoneStatePermission');
    });

    test('requestPhoneStatePermission maps permission strings to enum correctly', () async {
      expect(await handler.requestPhoneStatePermission(), TelephonyPermissionStatus.granted);
    });

    test('ensurePhoneStatePermission succeeds if permission is already granted', () async {
      await expectLater(handler.ensurePhoneStatePermission(), completes);
    });

    test('ensurePhoneStatePermission throws PermissionFailureException if denied', () async {
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(const MethodChannel(channelName), (call) async {
        if (call.method == 'checkPhoneStatePermission') return false;
        if (call.method == 'requestPhoneStatePermission') return 'denied';
        return null;
      });

      expect(
        () async => await handler.ensurePhoneStatePermission(),
        throwsA(isA<PermissionFailureException>().having(
          (e) => e.code,
          'code',
          'denied',
        )),
      );
    });

    test('Transparency rationale provides detailed Play Store justification message', () {
      final rationale = handler.getTransparencyRationale();
      expect(rationale, contains('READ_PHONE_STATE'));
      expect(rationale, contains('لا يصل إطلاقاً إلى سجل المكالمات'));
    });

    test('AndroidManifest.xml contains READ_PHONE_STATE and ACCESS_NETWORK_STATE', () {
      final manifestFile = File('android/app/src/main/AndroidManifest.xml');
      expect(manifestFile.existsSync(), isTrue);
      final content = manifestFile.readAsStringSync();
      expect(content, contains('android.permission.READ_PHONE_STATE'));
      expect(content, contains('android.permission.ACCESS_NETWORK_STATE'));
    });
  });

  group('Issue #18: Play Store Privacy & Data Safety Documentation', () {
    test('PRIVACY_POLICY.md exists and covers zero transmission, user control, contacts info', () {
      final file = File('docs/PRIVACY_POLICY.md');
      expect(file.existsSync(), isTrue);
      final content = file.readAsStringSync();
      expect(content, contains('Zero Remote Transmission'));
      expect(content, contains('No Third-Party Sharing'));
      expect(content, contains('READ_PHONE_STATE'));
      expect(content, contains('support@talabatuk.app'));
    });

    test('DATA_SAFETY.md exists and contains standard Google Play answers and reviewer justification', () {
      final file = File('docs/DATA_SAFETY.md');
      expect(file.existsSync(), isTrue);
      final content = file.readAsStringSync();
      expect(content, contains('Google Play Console Data Safety Guide'));
      expect(content, contains('English Reviewer Justification'));
      expect(content, contains('cellular network diagnostic and radio mode switcher utility'));
      expect(content, contains('clearPatternHistory'));
    });
  });
}

// =============================================================================
// Test Doubles (Fakes)
// =============================================================================

class FakeRadioDataSource extends RadioDeviceDataSource {
  bool radioEnabled = true;
  int? preferredMode = 9;
  bool setModeSuccess = true;
  int? lastSetMode;
  int? lastSetSubId;

  @override
  Future<bool> isRadioEnabled() async => radioEnabled;

  @override
  Future<int?> getPreferredNetworkMode({int? subId}) async => preferredMode;

  @override
  Future<bool> setPreferredNetworkMode({required int mode, int? subId}) async {
    lastSetMode = mode;
    lastSetSubId = subId;
    return setModeSuccess;
  }

  @override
  Future<Map<String, dynamic>> getRawNetworkInfo({int? subId}) async {
    return {'operatorName': 'FakeOperator', 'networkType': 'LTE'};
  }

  @override
  Future<Map<String, dynamic>?> getCellIdentity({int? subId}) async {
    return {'cid': 111, 'lac': 222, 'pci': 333};
  }

  @override
  Future<int?> getSignalStrengthDbm({int? subId}) async => -90;

  @override
  Future<dynamic> invokeRawMethod(String method, [dynamic arguments]) async => 'fake';
}

class FakePreferencesDataSource implements LocalPreferencesDataSource {
  List<PatternHistoryModel> savedHistory = [];
  int? savedLastAppliedMode;
  Map<String, dynamic> prefs = {};

  @override
  Future<void> savePatternHistory(PatternHistoryModel pattern) async {
    savedHistory.insert(0, pattern);
  }

  @override
  Future<List<PatternHistoryModel>> getPatternHistory() async => savedHistory;

  @override
  Future<void> clearPatternHistory() async {
    savedHistory.clear();
  }

  @override
  Future<void> saveLastAppliedMode(int mode) async {
    savedLastAppliedMode = mode;
  }

  @override
  Future<int?> getLastAppliedMode() async => savedLastAppliedMode;

  @override
  Future<void> setStringPreference(String key, String value) async {
    prefs[key] = value;
  }

  @override
  Future<String?> getStringPreference(String key) async => prefs[key] as String?;

  @override
  Future<void> setBoolPreference(String key, bool value) async {
    prefs[key] = value;
  }

  @override
  Future<bool?> getBoolPreference(String key) async => prefs[key] as bool?;

  @override
  Future<void> clearAllPreferences() async {
    savedHistory.clear();
    savedLastAppliedMode = null;
    prefs.clear();
  }
}
