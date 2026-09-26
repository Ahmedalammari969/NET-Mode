import 'package:flutter/services.dart';
import '../../core/errors/exceptions.dart';

/// العقد المجرد لمصدر بيانات عتاد الراديو ومودم الهاتف (Radio Device DataSource Contract).
///
/// يلتزم هذا العقد بمبادئ Clean Architecture و SOLID:
/// - SRP: عزل استدعاءات عتاد الراديو عن أي تفضيلات محلية أو منطق واجهة.
/// - Defensive Fallback: معالجة الأخطاء والـ Exceptions عبر [RadioDeviceException].
abstract class RadioDeviceDataSource {
  // --- عمليات الفحص والالتقاط اللحظي للشبكة ---
  Future<Map<String, dynamic>> getInstantNetworkSnapshot();
  Future<bool> openRadioMenu();
  Future<bool> setNetworkMode(int networkTypeCode);

  // --- عمليات التحكم الدقيق بمودم الراديو وهندسة التيليمتري (Issue #13 Engine) ---
  Future<bool> isRadioEnabled();
  Future<int?> getPreferredNetworkMode({int? subId});
  Future<bool> setPreferredNetworkMode({required int mode, int? subId});
  Future<Map<String, dynamic>> getRawNetworkInfo({int? subId});
  Future<Map<String, dynamic>?> getCellIdentity({int? subId});
  Future<int?> getSignalStrengthDbm({int? subId});
  Future<dynamic> invokeRawMethod(String method, [dynamic arguments]);
}

/// التنفيذ الفعلي لـ [RadioDeviceDataSource] عبر MethodChannel باسم com.netmode.app/radio.
class RadioDeviceDataSourceImpl implements RadioDeviceDataSource {
  static const String defaultChannelName = 'com.netmode.app/radio';
  final MethodChannel _channel;

  /// يدعم حقن قناة وهمية (Mock Channel) لتسهيل الفحص الآلي (Testability).
  RadioDeviceDataSourceImpl({MethodChannel? channel})
      : _channel = channel ?? const MethodChannel(defaultChannelName);

  // ===========================================================================
  // عمليات التوافق اللحظي مع واجهة المستخدم
  // ===========================================================================

  @override
  Future<Map<String, dynamic>> getInstantNetworkSnapshot() async {
    try {
      final result = await _channel.invokeMapMethod<String, dynamic>(
        'getInstantNetworkSnapshot',
      );
      return result ??
          {
            'networkType': 'Unknown',
            'carrier': 'No Carrier',
            'simState': false,
            'isAirplaneMode': false,
          };
    } on PlatformException catch (_) {
      return {
        'networkType': 'Unknown',
        'carrier': 'No Carrier',
        'simState': false,
        'isAirplaneMode': false,
      };
    }
  }

  @override
  Future<bool> openRadioMenu() async {
    try {
      final bool? success = await _channel.invokeMethod<bool>(
        'openRadioSettings',
      );
      return success ?? false;
    } on PlatformException catch (_) {
      return false;
    }
  }

  @override
  Future<bool> setNetworkMode(int networkTypeCode) async {
    try {
      final bool? applied = await _channel.invokeMethod<bool>(
        'setNetworkMode',
        {'networkTypeCode': networkTypeCode},
      );
      return applied ?? false;
    } on PlatformException catch (_) {
      return false;
    }
  }

  // ===========================================================================
  // عمليات Issue #13 المتقدمة للأجهزة وعتاد الراديو (Hardware RIL Telemetry)
  // ===========================================================================

  @override
  Future<bool> isRadioEnabled() async {
    try {
      final bool? isEnabled =
          await _channel.invokeMethod<bool>('isRadioEnabled');
      return isEnabled ?? false;
    } on PlatformException catch (e) {
      throw RadioDeviceException(
        message: e.message ?? 'فشل في التحقق من حالة تشغيل الراديو',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw RadioDeviceException(
        message: 'خطأ غير متوقع أثناء فحص حالة الراديو: $e',
      );
    }
  }

  @override
  Future<int?> getPreferredNetworkMode({int? subId}) async {
    try {
      final Map<String, dynamic>? args =
          subId != null ? <String, dynamic>{'subId': subId} : null;
      final int? mode =
          await _channel.invokeMethod<int>('getPreferredNetworkMode', args);
      return mode;
    } on PlatformException catch (e) {
      throw RadioDeviceException(
        message: e.message ?? 'فشل في جلب نمط الشبكة المفضل',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw RadioDeviceException(
        message: 'خطأ غير متوقع أثناء جلب نمط الشبكة المفضل: $e',
      );
    }
  }

  @override
  Future<bool> setPreferredNetworkMode({
    required int mode,
    int? subId,
  }) async {
    try {
      final Map<String, dynamic> args = <String, dynamic>{
        'networkMode': mode,
      };
      if (subId != null) {
        args['subId'] = subId;
      }
      final bool? success =
          await _channel.invokeMethod<bool>('setPreferredNetworkMode', args);
      return success ?? false;
    } on PlatformException catch (e) {
      throw RadioDeviceException(
        message: e.message ?? 'فشل في تعيين نمط الشبكة المفضل',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw RadioDeviceException(
        message: 'خطأ غير متوقع أثناء تعيين نمط الشبكة المفضل: $e',
      );
    }
  }

  @override
  Future<Map<String, dynamic>> getRawNetworkInfo({int? subId}) async {
    try {
      final Map<String, dynamic>? args =
          subId != null ? <String, dynamic>{'subId': subId} : null;
      final dynamic result =
          await _channel.invokeMethod<dynamic>('getRawNetworkInfo', args);

      if (result == null) {
        return <String, dynamic>{};
      }
      if (result is Map) {
        return Map<String, dynamic>.from(result);
      }
      return <String, dynamic>{'raw': result};
    } on PlatformException catch (e) {
      throw RadioDeviceException(
        message: e.message ?? 'فشل في استخراج بيانات الشبكة الخام',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw RadioDeviceException(
        message: 'خطأ غير متوقع أثناء استخراج بيانات الشبكة الخام: $e',
      );
    }
  }

  @override
  Future<Map<String, dynamic>?> getCellIdentity({int? subId}) async {
    try {
      final Map<String, dynamic>? args =
          subId != null ? <String, dynamic>{'subId': subId} : null;
      final dynamic result =
          await _channel.invokeMethod<dynamic>('getCellIdentity', args);

      if (result == null) {
        return null;
      }
      if (result is Map) {
        return Map<String, dynamic>.from(result);
      }
      return <String, dynamic>{'raw': result};
    } on PlatformException catch (e) {
      throw RadioDeviceException(
        message: e.message ?? 'فشل في استخراج هوية البرج والخلية',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw RadioDeviceException(
        message: 'خطأ غير متوقع أثناء استخراج هوية الخلية: $e',
      );
    }
  }

  @override
  Future<int?> getSignalStrengthDbm({int? subId}) async {
    try {
      final Map<String, dynamic>? args =
          subId != null ? <String, dynamic>{'subId': subId} : null;
      final int? dbm =
          await _channel.invokeMethod<int>('getSignalStrengthDbm', args);
      return dbm;
    } on PlatformException catch (e) {
      throw RadioDeviceException(
        message: e.message ?? 'فشل في استخراج قوة الإشارة',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw RadioDeviceException(
        message: 'خطأ غير متوقع أثناء قراءة قوة الإشارة: $e',
      );
    }
  }

  @override
  Future<dynamic> invokeRawMethod(String method, [dynamic arguments]) async {
    try {
      return await _channel.invokeMethod<dynamic>(method, arguments);
    } on PlatformException catch (e) {
      throw RadioDeviceException(
        message: e.message ?? 'فشل استدعاء دالة المنصة: $method',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw RadioDeviceException(
        message: 'خطأ غير متوقع أثناء استدعاء $method: $e',
      );
    }
  }
}
