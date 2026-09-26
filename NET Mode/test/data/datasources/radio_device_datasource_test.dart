import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/core/errors/exceptions.dart';
import 'package:net_mode/data/datasources/radio_device_datasource.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

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
          case 'getInstantNetworkSnapshot':
            return <String, dynamic>{
              'networkType': '4G LTE',
              'carrier': 'Yemen Mobile',
              'simState': true,
              'isAirplaneMode': false,
            };
          case 'openRadioSettings':
            return true;
          case 'setNetworkMode':
            return true;
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
      final cell = await dataSource.getCellIdentity(subId: 1);
      expect(cell, isNotNull);
      expect(cell!['cid'], 12345);
      expect(cell['lac'], 678);
    });

    test('getSignalStrengthDbm retrieves signal in dBm', () async {
      final dbm = await dataSource.getSignalStrengthDbm();
      expect(dbm, -85);
    });

    test('invokeRawMethod executes generic method', () async {
      final result = await dataSource.invokeRawMethod('customMethod', {'arg': 1});
      expect(result, 'customResult');
    });

    test('MethodChannel PlatformException is caught and wrapped in RadioDeviceException', () async {
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(const MethodChannel(channelName), (call) async {
        throw PlatformException(code: 'SECURITY_ERROR', message: 'Knox Security Lock');
      });

      expect(
        () async => await dataSource.isRadioEnabled(),
        throwsA(isA<RadioDeviceException>()),
      );
    });

    test('getInstantNetworkSnapshot returns safe fallback on PlatformException', () async {
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(const MethodChannel(channelName), (call) async {
        throw PlatformException(code: 'UNAVAILABLE');
      });

      final snapshot = await dataSource.getInstantNetworkSnapshot();
      expect(snapshot['networkType'], 'Unknown');
      expect(snapshot['carrier'], 'No Carrier');
      expect(snapshot['simState'], false);
    });
  });
}
