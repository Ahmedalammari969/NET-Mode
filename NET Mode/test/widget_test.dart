import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/domain/entities/network_info.dart';
import 'package:net_mode/domain/entities/network_mode.dart';
import 'package:net_mode/domain/repositories/network_repository.dart';
import 'package:net_mode/domain/usecases/network_usecases.dart';
import 'package:net_mode/main.dart';

class FakeNetworkRepository implements NetworkRepository {
  NetworkMode? _mode;

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
  Future<NetworkMode?> getPreferredMode() async => _mode;

  @override
  Future<void> savePreferredMode(NetworkMode mode) async {
    _mode = mode;
  }

  @override
  Future<bool> setNetworkMode(NetworkMode mode) async {
    _mode = mode;
    return true;
  }
}

void main() {
  testWidgets('HomeScreen عرض أنماط الشبكة اليمنية الخمسة وتطبيقها', (
    WidgetTester tester,
  ) async {
    final fakeRepo = FakeNetworkRepository();
    final getSnapshot = GetInstantNetworkSnapshotUseCase(fakeRepo);
    final openRadio = OpenRadioSettingsUseCase(fakeRepo);
    final manageMode = ManagePreferredModeUseCase(fakeRepo);
    final setMode = SetNetworkModeUseCase(fakeRepo);

    await tester.pumpWidget(
      MaterialApp(
        home: HomeScreen(
          getSnapshotUseCase: getSnapshot,
          openRadioSettingsUseCase: openRadio,
          managePreferredModeUseCase: manageMode,
          setNetworkModeUseCase: setMode,
        ),
      ),
    );

    // الإطار الأول — تحميل
    expect(find.byType(CircularProgressIndicator), findsWidgets);

    // انتظر اكتمال التحميل اللاتزامني
    await tester.pumpAndSettle();

    // التحقق من ظهور معلومات المشغل
    expect(find.text('Yemen Mobile'), findsOneWidget);

    // التحقق من ظهور الأنماط اليمنية الخمسة
    expect(find.text('Yemen Mobile+4G'), findsOneWidget);
    expect(find.text('Yemen Mobile 3G Only'), findsOneWidget);
    expect(find.text('sabafon + you'), findsOneWidget);
    expect(find.text('VoLTE'), findsOneWidget);
    expect(find.text('(Auto)'), findsOneWidget);

    // اختبار الضغط على نمط وتطبيقه
    await tester.tap(find.text('Yemen Mobile+4G'));
    await tester.pumpAndSettle();

    // التحقق من أن SnackBar ظهر
    expect(find.textContaining('Yemen Mobile+4G'), findsWidgets);
  });

  testWidgets('HomeScreen يعرض وضع الطيران بشكل دقيق عند تفعيله', (
    WidgetTester tester,
  ) async {
    final fakeRepo = FakeAirplaneRepository();
    final getSnapshot = GetInstantNetworkSnapshotUseCase(fakeRepo);
    final openRadio = OpenRadioSettingsUseCase(fakeRepo);
    final manageMode = ManagePreferredModeUseCase(fakeRepo);
    final setMode = SetNetworkModeUseCase(fakeRepo);

    await tester.pumpWidget(
      MaterialApp(
        home: HomeScreen(
          getSnapshotUseCase: getSnapshot,
          openRadioSettingsUseCase: openRadio,
          managePreferredModeUseCase: manageMode,
          setNetworkModeUseCase: setMode,
        ),
      ),
    );

    await tester.pumpAndSettle();

    // التحقق من أن النص ليس "الشبكة متصلة" بل يوضح وضع الطيران
    expect(find.text('الشبكة متصلة'), findsNothing);
    expect(find.text('وضع الطيران (غير متصلة)'), findsOneWidget);
  });
}

class FakeAirplaneRepository implements NetworkRepository {
  @override
  Future<NetworkInfo> getInstantNetworkSnapshot() async {
    return const NetworkInfo(
      carrier: 'وضع الطيران',
      networkType: 'الراديو متوقف (وضع الطيران)',
      hasSimCard: true,
      isAirplaneMode: true,
    );
  }

  @override
  Future<bool> openRadioTestingSettings() async => true;

  @override
  Future<NetworkMode?> getPreferredMode() async => null;

  @override
  Future<void> savePreferredMode(NetworkMode mode) async {}

  @override
  Future<bool> setNetworkMode(NetworkMode mode) async => true;
}

