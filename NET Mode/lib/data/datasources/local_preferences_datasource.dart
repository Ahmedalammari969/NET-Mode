import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
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

/// التنفيذ الفعلي لـ [LocalPreferencesDataSource] بالاعتماد على [SharedPreferences] وتخزين JSON.
class LocalPreferencesDataSourceImpl implements LocalPreferencesDataSource {
  static const String keyPatternHistory = 'CACHED_PATTERN_HISTORY';
  static const String keyLastAppliedMode = 'CACHED_LAST_APPLIED_MODE';

  final SharedPreferences? _prefsInstance;

  LocalPreferencesDataSourceImpl({SharedPreferences? sharedPreferences})
      : _prefsInstance = sharedPreferences;

  Future<SharedPreferences> get _prefs async =>
      _prefsInstance ?? await SharedPreferences.getInstance();

  @override
  Future<void> savePatternHistory(PatternHistoryModel pattern) async {
    try {
      final SharedPreferences prefs = await _prefs;
      final List<PatternHistoryModel> currentHistory =
          await getPatternHistory();
      final List<PatternHistoryModel> updatedHistory = [
        pattern,
        ...currentHistory,
      ];

      final String encodedJson = jsonEncode(
        updatedHistory.map((e) => e.toJson()).toList(),
      );
      await prefs.setString(keyPatternHistory, encodedJson);
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
      final SharedPreferences prefs = await _prefs;
      final String? jsonString = prefs.getString(keyPatternHistory);

      if (jsonString == null || jsonString.trim().isEmpty) {
        return <PatternHistoryModel>[];
      }

      final dynamic decoded = jsonDecode(jsonString);
      if (decoded is List) {
        return decoded
            .map((item) =>
                PatternHistoryModel.fromJson(Map<String, dynamic>.from(item as Map)))
            .toList();
      }
      return <PatternHistoryModel>[];
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
      final SharedPreferences prefs = await _prefs;
      await prefs.remove(keyPatternHistory);
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
      final SharedPreferences prefs = await _prefs;
      await prefs.setInt(keyLastAppliedMode, mode);
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
      final SharedPreferences prefs = await _prefs;
      return prefs.getInt(keyLastAppliedMode);
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
      final SharedPreferences prefs = await _prefs;
      await prefs.setString(key, value);
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
      final SharedPreferences prefs = await _prefs;
      return prefs.getString(key);
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
      final SharedPreferences prefs = await _prefs;
      await prefs.setBool(key, value);
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
      final SharedPreferences prefs = await _prefs;
      return prefs.getBool(key);
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
      final SharedPreferences prefs = await _prefs;
      await prefs.clear();
    } catch (e) {
      throw LocalPreferencesException(
        message: 'فشل في مسح كافة التفضيلات: $e',
        details: e,
      );
    }
  }
}
