import 'package:flutter/services.dart';

/// حالات إذن الوصول إلى حالة الهاتف والشبكة الخلوية.
enum TelephonyPermissionStatus {
  granted,
  denied,
  permanentlyDenied,
  restricted,
  unknown;

  bool get isGranted => this == TelephonyPermissionStatus.granted;
  bool get isDenied => this == TelephonyPermissionStatus.denied;
  bool get isPermanentlyDenied =>
      this == TelephonyPermissionStatus.permanentlyDenied;
}

/// معالج ومسؤول أذونات حالة الهاتف والاتصالات (READ_PHONE_STATE)
/// يتعامل مع الأذونات بشفافية كاملة دون أي أعطال صامتة.
class PermissionHandler {
  static const String defaultChannelName = 'com.netmode.app/permissions';
  final MethodChannel _channel;

  const PermissionHandler({MethodChannel? channel})
      : _channel = channel ?? const MethodChannel(defaultChannelName);

  /// رسالة الشفافية والتبرير الموجهة للمستخدم للامتثال الصارم لسياسات Google Play.
  static const String phoneStateRationale =
      'يحتاج التطبيق إلى إذن حالة الهاتف (READ_PHONE_STATE) لتحديد نوع ونمط الشبكة '
      'الخلوية النشط (مثل 4G LTE أو 5G NR)، وقراءة قوة الإشارة وبيانات الخلية. '
      'التطبيق لا يصل إطلاقاً إلى سجل المكالمات أو جهات الاتصال أو أي بيانات خاصة بالمستخدم.';

  /// التحقق مما إذا كان إذن READ_PHONE_STATE ممنوحاً حالياً للتطبيق.
  Future<bool> isPhoneStatePermissionGranted() async {
    try {
      final bool? isGranted =
          await _channel.invokeMethod<bool>('checkPhoneStatePermission');
      return isGranted ?? false;
    } on PlatformException catch (e) {
      throw PermissionFailureException(
        message: e.message ?? 'فشل في التحقق من إذن حالة الهاتف',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw PermissionFailureException(
        message: 'حدث خطأ غير متوقع أثناء فحص إذن حالة الهاتف: $e',
      );
    }
  }

  /// طلب إذن READ_PHONE_STATE من المستخدم مع إرجاع الحالة التفصيلية.
  Future<TelephonyPermissionStatus> requestPhoneStatePermission() async {
    try {
      final String? result =
          await _channel.invokeMethod<String>('requestPhoneStatePermission');
      return _mapStringToStatus(result);
    } on PlatformException catch (e) {
      throw PermissionFailureException(
        message: e.message ?? 'فشل في طلب إذن حالة الهاتف من المنصة',
        code: e.code,
        details: e.details,
      );
    } catch (e) {
      throw PermissionFailureException(
        message: 'حدث خطأ غير متوقع أثناء طلب إذن الهاتف: $e',
      );
    }
  }

  /// التحقق مما إذا كان النظام يوصي بعرض رسالة التبرير والتوضيح (Rationale).
  Future<bool> shouldShowRequestPermissionRationale() async {
    try {
      final bool? shouldShow = await _channel
          .invokeMethod<bool>('shouldShowRequestPermissionRationale');
      return shouldShow ?? false;
    } on PlatformException {
      return true;
    } catch (_) {
      return true;
    }
  }

  /// التأكد من منح الإذن قبل تنفيذ أي عملية، ورمي استثناء شفاف في حال الرفض لمنع الأعطال الصامتة.
  Future<void> ensurePhoneStatePermission() async {
    final bool granted = await isPhoneStatePermissionGranted();
    if (!granted) {
      final TelephonyPermissionStatus status =
          await requestPhoneStatePermission();
      if (!status.isGranted) {
        throw PermissionFailureException(
          message:
              'تعذر إتمام العملية: يتطلب التطبيق إذن حالة الهاتف (READ_PHONE_STATE).',
          code: status.name,
          details: <String, dynamic>{
            'status': status.name,
            'rationale': phoneStateRationale,
          },
        );
      }
    }
  }

  /// الحصول على نص التبرير والشفافية لعرضه في واجهة المستخدم أو الحوارات التنبيهية.
  String getTransparencyRationale() => phoneStateRationale;

  TelephonyPermissionStatus _mapStringToStatus(String? status) {
    switch (status?.toLowerCase()) {
      case 'granted':
        return TelephonyPermissionStatus.granted;
      case 'denied':
        return TelephonyPermissionStatus.denied;
      case 'permanentlydenied':
        return TelephonyPermissionStatus.permanentlyDenied;
      case 'restricted':
        return TelephonyPermissionStatus.restricted;
      default:
        return TelephonyPermissionStatus.unknown;
    }
  }
}

/// استثناء شفاف مخصص لأخطاء ورفض الأذونات لتفادي أي انهيار صامت.
class PermissionFailureException implements Exception {
  final String message;
  final String? code;
  final dynamic details;

  const PermissionFailureException({
    required this.message,
    this.code,
    this.details,
  });

  @override
  String toString() =>
      'PermissionFailureException(code: $code, message: $message, details: $details)';
}
