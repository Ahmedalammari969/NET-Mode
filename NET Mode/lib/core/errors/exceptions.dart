/// الفئة الأساسية لجميع الاستثناءات التي قد تحدث في مصادر البيانات والمنصة.
abstract class AppException implements Exception {
  final String message;
  final String? code;
  final dynamic details;

  const AppException({
    required this.message,
    this.code,
    this.details,
  });

  @override
  String toString() =>
      '$runtimeType(message: $message, code: $code, details: $details)';
}

/// استثناء ناتج عن أخطاء عتاد الراديو وقنوات التواصل مع المنصة (MethodChannel).
class DeviceException extends AppException {
  const DeviceException({
    required super.message,
    super.code,
    super.details,
  });
}

/// استثناء ناتج عن غياب أذونات النظام الضرورية (مثل READ_PHONE_STATE).
class PermissionException extends AppException {
  const PermissionException({
    required super.message,
    super.code,
    super.details,
  });
}

/// استثناء ناتج عن فشل عمليات التخزين المحلي أو التفضيلات (SharedPreferences).
class CacheException extends AppException {
  const CacheException({
    required super.message,
    super.code,
    super.details,
  });
}

/// استثناء ناتج عن فشل الاتصال بالشبكة أو عدم استقرار الاتصال.
class NetworkException extends AppException {
  const NetworkException({
    required super.message,
    super.code,
    super.details,
  });
}

/// استثناء عام للأخطاء غير المتوقعة أو غير المصنفة.
class UnexpectedException extends AppException {
  const UnexpectedException({
    required super.message,
    super.code,
    super.details,
  });
}
