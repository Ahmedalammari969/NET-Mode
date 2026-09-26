import 'dart:convert';
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

/// التنفيذ الفعلي لـ [LocalPreferencesDataSource] مع دعم تشفير الـ JSON ومعالجة الأخطاء.
class LocalPreferencesDataSourceImpl implements LocalPreferencesDataSource {
  static const String keyPatternHistory = 'CACHED_PATTERN_HISTORY';
  static const String keyLastAppliedMode = 'CACHED_LAST_APPLIED_MODE';

  final Map<String, dynamic> _storage = <String, dynamic>{};
  final List<PatternHistoryModel> _history = <PatternHistoryModel>[];
  int? _lastAppliedMode;

  LocalPreferencesDataSourceImpl({dynamic sharedPreferences});

  @override
  Future<void> savePatternHistory(PatternHistoryModel pattern) async {
    try {
      _history.insert(0, pattern);
      final jsonList = _history.map((e) => e.toJson()).toList();
      _storage[keyPatternHistory] = jsonEncode(jsonList);
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في حفظ سجل النمط محلياً: $e',
        details: e,
      );
    }
  }

  @override
  Future<List<PatternHistoryModel>> getPatternHistory() async {
    try {
      final jsonString = _storage[keyPatternHistory] as String?;
      if (jsonString == null || jsonString.trim().isEmpty) {
        return List<PatternHistoryModel>.unmodifiable(_history);
      }

      final dynamic decoded = jsonDecode(jsonString);
      if (decoded is List) {
        return decoded
            .map((item) => PatternHistoryModel.fromJson(
                Map<String, dynamic>.from(item as Map)))
            .toList();
      }
      return List<PatternHistoryModel>.unmodifiable(_history);
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في قراءة سجل الأنماط المحلي: $e',
        details: e,
      );
    }
  }

  @override
  Future<void> clearPatternHistory() async {
    try {
      _history.clear();
      _storage.remove(keyPatternHistory);
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في مسح سجل الأنماط: $e',
        details: e,
      );
    }
  }

  @override
  Future<void> saveLastAppliedMode(int mode) async {
    try {
      _lastAppliedMode = mode;
      _storage[keyLastAppliedMode] = mode;
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في حفظ آخر نمط مطبق: $e',
        details: e,
      );
    }
  }

  @override
  Future<int?> getLastAppliedMode() async {
    try {
      final val = _storage[keyLastAppliedMode];
      if (val is int) return val;
      return _lastAppliedMode;
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في قراءة آخر نمط مطبق: $e',
        details: e,
      );
    }
  }

  @override
  Future<void> setStringPreference(String key, String value) async {
    try {
      _storage[key] = value;
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في حفظ التفضيل $key: $e',
        details: e,
      );
    }
  }

  @override
  Future<String?> getStringPreference(String key) async {
    try {
      return _storage[key]?.toString();
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في قراءة التفضيل $key: $e',
        details: e,
      );
    }
  }

  @override
  Future<void> setBoolPreference(String key, bool value) async {
    try {
      _storage[key] = value;
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في حفظ التفضيل المنطقي $key: $e',
        details: e,
      );
    }
  }

  @override
  Future<bool?> getBoolPreference(String key) async {
    try {
      final val = _storage[key];
      if (val is bool) return val;
      return null;
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في قراءة التفضيل المنطقي $key: $e',
        details: e,
      );
    }
  }

  @override
  Future<void> clearAllPreferences() async {
    try {
      _storage.clear();
      _history.clear();
      _lastAppliedMode = null;
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في مسح كافة التفضيلات: $e',
        details: e,
      );
    }
  }
}
