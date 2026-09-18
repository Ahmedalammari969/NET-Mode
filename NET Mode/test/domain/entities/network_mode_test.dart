import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/domain/entities/network_mode.dart';

void main() {
  group('NetworkMode Entity', () {
    test('supports value comparisons and equality', () {
      const mode1 = NetworkMode(
        id: 'lte_only',
        name: 'LTE Only',
        networkTypeCode: 11,
        generation: NetworkGeneration.fourG,
        isLockMode: true,
      );

      const mode2 = NetworkMode(
        id: 'lte_only',
        name: 'LTE Only',
        networkTypeCode: 11,
        generation: NetworkGeneration.fourG,
        isLockMode: true,
      );

      expect(mode1, equals(mode2));
      expect(mode1.hashCode, equals(mode2.hashCode));
    });

    test('copyWith returns modified copy correctly', () {
      const mode = NetworkMode.lteOnly;
      final updated = mode.copyWith(name: 'Force 4G LTE');

      expect(updated.id, equals(mode.id));
      expect(updated.name, equals('Force 4G LTE'));
      expect(updated.networkTypeCode, equals(mode.networkTypeCode));
      expect(updated.generation, equals(mode.generation));
      expect(updated.isLockMode, isTrue);
    });

    test('standardPresets includes standard radio profiles', () {
      expect(NetworkMode.standardPresets, contains(NetworkMode.lteOnly));
      expect(NetworkMode.standardPresets, contains(NetworkMode.nrOnly));
      expect(NetworkMode.standardPresets, contains(NetworkMode.autoGlobal));
      expect(NetworkMode.standardPresets, contains(NetworkMode.wcdmaOnly));
      expect(NetworkMode.standardPresets, contains(NetworkMode.gsmOnly));
    });
  });
}
