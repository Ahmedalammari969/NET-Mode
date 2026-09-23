import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/domain/entities/network_info.dart';

void main() {
  group('NetworkInfo Entity', () {
    test('supports value comparisons and equality', () {
      const info1 = NetworkInfo(
        carrier: 'Yemen Mobile',
        networkType: 'LTE',
        hasSimCard: true,
      );

      const info2 = NetworkInfo(
        carrier: 'Yemen Mobile',
        networkType: 'LTE',
        hasSimCard: true,
      );

      expect(info1, equals(info2));
      expect(info1.hashCode, equals(info2.hashCode));
    });

    test('changing any field breaks equality', () {
      const base = NetworkInfo(
        carrier: 'Yemen Mobile',
        networkType: 'LTE',
        hasSimCard: true,
      );

      expect(
        base ==
            const NetworkInfo(
              carrier: 'Other Carrier',
              networkType: 'LTE',
              hasSimCard: true,
            ),
        isFalse,
      );
      expect(
        base ==
            const NetworkInfo(
              carrier: 'Yemen Mobile',
              networkType: '3G',
              hasSimCard: true,
            ),
        isFalse,
      );
      expect(
        base ==
            const NetworkInfo(
              carrier: 'Yemen Mobile',
              networkType: 'LTE',
              hasSimCard: false,
            ),
        isFalse,
      );
      // isAirplaneMode defaults to false, so it is part of the equality
      // contract even though it can be omitted at construction.
      expect(
        base ==
            const NetworkInfo(
              carrier: 'Yemen Mobile',
              networkType: 'LTE',
              hasSimCard: true,
              isAirplaneMode: true,
            ),
        isFalse,
      );
    });

    test('empty carrier is a valid no-SIM state (edge case EX-02)', () {
      const noSim = NetworkInfo(
        carrier: '',
        networkType: 'No Service',
        hasSimCard: false,
        isAirplaneMode: true,
      );

      expect(noSim.carrier, isEmpty);
      expect(noSim.networkType, equals('No Service'));
      expect(noSim.hasSimCard, isFalse);
      expect(noSim.isAirplaneMode, isTrue);
    });
  });
}
