import 'exceptions.dart';

/// الفئة الأساسية المجردة لجميع الأعطال (Failures) في طبقة النطاق (Domain).
abstract class Failure {
  final String message;
  final String? code;

  const Failure({
    required this.message,
    this.code,
  });

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Failure &&
          runtimeType == other.runtimeType &&
          message == other.message &&
          code == other.code;

  @override
  int get hashCode => message.hashCode ^ (code?.hashCode ?? 0);

  @override
  String toString() => '$runtimeType(message: $message, code: $code)';

  /// محول ذكي يحول استثناءات المنصة والبيانات إلى أعطال مهيكلة سهلة للمستخدم.
  factory Failure.fromException(Object error) {
    if (error is DeviceException) {
      return DeviceFailure(
        message: error.message.isNotEmpty
            ? error.message
            : 'تعذر الاتصال بعتاد الراديو أو أجهزة الهاتف.',
        code: error.code,
      );
    } else if (error is PermissionException) {
      return PermissionFailure(
        message: error.message.isNotEmpty
            ? error.message
            : 'يتطلب التطبيق منح الإذن المطلوب للمتابعة.',
        code: error.code,
      );
    } else if (error is CacheException) {
      return CacheFailure(
        message: error.message.isNotEmpty
            ? error.message
            : 'حدث خطأ في قراءة أو تخزين البيانات المحلية.',
        code: error.code,
      );
    } else if (error is NetworkException) {
      return NetworkFailure(
        message: error.message.isNotEmpty
            ? error.message
            : 'تعذر الاتصال بالشبكة المطلوبة.',
        code: error.code,
      );
    } else {
      return UnexpectedFailure(
        message: 'حدث عطل غير متوقع: $error',
      );
    }
  }
}

/// عطل متعلق بأجهزة المودم وعتاد الراديو وقنوات المنصة.
class DeviceFailure extends Failure {
  const DeviceFailure({
    required super.message,
    super.code,
  });
}

/// عطل متعلق بنقص أو رفض أذونات النظام الأساسية.
class PermissionFailure extends Failure {
  const PermissionFailure({
    required super.message,
    super.code,
  });
}

/// عطل متعلق بالذاكرة المحلية والتخزين المؤقت وسجل الأنماط.
class CacheFailure extends Failure {
  const CacheFailure({
    required super.message,
    super.code,
  });
}

/// عطل متعلق بالاتصال بالشبكة الخلوية أو شبكة البيانات.
class NetworkFailure extends Failure {
  const NetworkFailure({
    required super.message,
    super.code,
  });
}

/// عطل عام لأي استثناء غير متوقع.
class UnexpectedFailure extends Failure {
  const UnexpectedFailure({
    required super.message,
    super.code,
  });
}
