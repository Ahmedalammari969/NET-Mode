import 'dart:io';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/core/permissions/permission_handler.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

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
        throwsA(isA<PermissionFailureException>()),
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
}
