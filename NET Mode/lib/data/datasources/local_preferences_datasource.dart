import '../models/pattern_history_model.dart';

/// استثناء مخصص لأخطاء التخزين المحلي واسترجاع التفضيلات.
class LocalPreferencesException implements Exception {
  final String message;
  final dynamic details;

  const LocalPreferencesException({
    required this.message,
    this.details,
  });

  @override
  String toString() =>
      'LocalPreferencesException(message: $message, details: $details)';
}

/// العقد المجرد لمصدر بيانات التفضيلات وسجل الأنماط المخزنة محلياً.
abstract class LocalPreferencesDataSource {
  /// حفظ عملية تطبيق نمط جديدة في سجل الجهاز المحلي.
  Future<void> savePatternHistory(PatternHistoryModel pattern);

  /// استرجاع قائمة سجل الأنماط السابقة المحفوظة بصيغة كائنات نماذج.
  Future<List<PatternHistoryModel>> getPatternHistory();

  /// مسح سجل الأنماط المحفوظة محلياً.
  Future<void> clearPatternHistory();

  /// حفظ آخر نمط شبكة تم اختياره أو تطبيقه.
  Future<void> saveLastAppliedMode(int mode);

  /// استرجاع آخر نمط شبكة تم تطبيقه.
  Future<int?> getLastAppliedMode();

  /// حفظ قيمة نصية عامة في التفضيلات.
  Future<void> setStringPreference(String key, String value);

  /// جلب قيمة نصية من التفضيلات.
  Future<String?> getStringPreference(String key);

  /// حفظ قيمة منطقية (Boolean) في التفضيلات.
  Future<void> setBoolPreference(String key, bool value);

  /// جلب قيمة منطقية من التفضيلات.
  Future<bool?> getBoolPreference(String key);

  /// مسح كافة التفضيلات المخزنة.
  Future<void> clearAllPreferences();
}

/// تنفيذ افتراضي في الذاكرة (In-Memory) لتسهيل الفحص المعماري بدون اعتماديات خارجية.
class InMemoryPreferencesDataSourceImpl implements LocalPreferencesDataSource {
  final Map<String, dynamic> _storage = <String, dynamic>{};
  final List<PatternHistoryModel> _history = <PatternHistoryModel>[];
  int? _lastAppliedMode;

  @override
  Future<void> savePatternHistory(PatternHistoryModel pattern) async {
    _history.insert(0, pattern);
  }

  @override
  Future<List<PatternHistoryModel>> getPatternHistory() async {
    return List<PatternHistoryModel>.unmodifiable(_history);
  }

  @override
  Future<void> clearPatternHistory() async {
    _history.clear();
  }

  @override
  Future<void> saveLastAppliedMode(int mode) async {
    _lastAppliedMode = mode;
  }

  @override
  Future<int?> getLastAppliedMode() async {
    return _lastAppliedMode;
  }

  @override
  Future<void> setStringPreference(String key, String value) async {
    _storage[key] = value;
  }

  @override
  Future<String?> getStringPreference(String key) async {
    return _storage[key] as String?;
  }

  @override
  Future<void> setBoolPreference(String key, bool value) async {
    _storage[key] = value;
  }

  @override
  Future<bool?> getBoolPreference(String key) async {
    return _storage[key] as bool?;
  }

  @override
  Future<void> clearAllPreferences() async {
    _storage.clear();
    _history.clear();
    _lastAppliedMode = null;
  }
}
