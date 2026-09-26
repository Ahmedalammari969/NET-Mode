import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/data/datasources/local_preferences_datasource.dart';
import 'package:net_mode/data/models/pattern_history_model.dart';

void main() {
  group('Issue #15: LocalPreferencesDataSource & PatternHistoryModel', () {
    test('PatternHistoryModel serialization & deserialization round-trip', () {
      final model = PatternHistoryModel(
        id: '123456789',
        networkMode: 20,
        modeName: 'NR only (5G)',
        subId: 1,
        timestamp: DateTime.parse('2026-09-25T12:00:00.000Z'),
        isSuccess: true,
        extraData: {'band': 'n78'},
      );

      final jsonMap = model.toJson();
      expect(jsonMap['id'], '123456789');
      expect(jsonMap['networkMode'], 20);
      expect(jsonMap['modeName'], 'NR only (5G)');
      expect(jsonMap['extraData'], {'band': 'n78'});

      final restored = PatternHistoryModel.fromJson(jsonMap);
      expect(restored.id, model.id);
      expect(restored.networkMode, model.networkMode);
      expect(restored.modeName, model.modeName);
      expect(restored.subId, model.subId);
      expect(restored.timestamp, model.timestamp);
      expect(restored.isSuccess, model.isSuccess);
      expect(restored.extraData, model.extraData);
      expect(restored, equals(model));
    });

    test('PatternHistoryModel handles missing or null JSON fields safely', () {
      final restored = PatternHistoryModel.fromJson({});
      expect(restored.id, '');
      expect(restored.networkMode, 0);
      expect(restored.modeName, '');
      expect(restored.subId, isNull);
      expect(restored.isSuccess, isTrue);
      expect(restored.extraData, isNull);
    });

    test('LocalPreferencesDataSourceImpl saves, retrieves, and clears history & preferences', () async {
      final dataSource = LocalPreferencesDataSourceImpl();

      // Verify empty history initially
      final initialHistory = await dataSource.getPatternHistory();
      expect(initialHistory, isEmpty);

      // Save history entry
      final entry = PatternHistoryModel(
        id: 'entry_1',
        networkMode: 10,
        modeName: 'LTE only (4G)',
        timestamp: DateTime.now(),
        isSuccess: true,
      );
      await dataSource.savePatternHistory(entry);

      // Retrieve history
      final history = await dataSource.getPatternHistory();
      expect(history.length, 1);
      expect(history.first.id, 'entry_1');
      expect(history.first.networkMode, 10);
      expect(history.first.modeName, 'LTE only (4G)');

      // Save and retrieve last applied mode
      await dataSource.saveLastAppliedMode(10);
      final lastMode = await dataSource.getLastAppliedMode();
      expect(lastMode, 10);

      // Save and retrieve string preference
      await dataSource.setStringPreference('user_carrier', 'Yemen Mobile');
      final carrier = await dataSource.getStringPreference('user_carrier');
      expect(carrier, 'Yemen Mobile');

      // Save and retrieve bool preference
      await dataSource.setBoolPreference('dark_theme', true);
      final isDark = await dataSource.getBoolPreference('dark_theme');
      expect(isDark, true);

      // Clear history
      await dataSource.clearPatternHistory();
      final clearedHistory = await dataSource.getPatternHistory();
      expect(clearedHistory, isEmpty);

      // Clear all preferences
      await dataSource.clearAllPreferences();
      expect(await dataSource.getLastAppliedMode(), isNull);
      expect(await dataSource.getStringPreference('user_carrier'), isNull);
      expect(await dataSource.getBoolPreference('dark_theme'), isNull);
    });
  });
}
