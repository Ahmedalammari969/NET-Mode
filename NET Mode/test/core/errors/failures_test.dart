import 'package:flutter_test/flutter_test.dart';
import 'package:net_mode/core/errors/exceptions.dart';
import 'package:net_mode/core/errors/failures.dart';

void main() {
  group('Issue #17: Unified Failures and Exception Architecture', () {
    test('Exceptions instantiate correctly with message, code and details', () {
      const devEx = DeviceException(
        message: 'Modem error',
        code: 'MODEM_01',
        details: {'info': 'failed'},
      );
      expect(devEx.message, 'Modem error');
      expect(devEx.code, 'MODEM_01');
      expect(devEx.details, {'info': 'failed'});
      expect(devEx.toString(), contains('DeviceException'));

      const permEx = PermissionException(message: 'Permission denied', code: 'PERM_DENIED');
      expect(permEx.message, 'Permission denied');

      const cacheEx = CacheException(message: 'Cache read error');
      expect(cacheEx.message, 'Cache read error');

      const netEx = NetworkException(message: 'Network offline');
      expect(netEx.message, 'Network offline');

      const unexpEx = UnexpectedException(message: 'Unknown crash');
      expect(unexpEx.message, 'Unknown crash');
    });

    test('Failure.fromException maps DeviceException to DeviceFailure', () {
      const ex = DeviceException(message: 'Radio fail', code: 'ERR_RADIO');
      final failure = Failure.fromException(ex);
      expect(failure, isA<DeviceFailure>());
      expect(failure.message, 'Radio fail');
      expect(failure.code, 'ERR_RADIO');
    });

    test('Failure.fromException maps PermissionException to PermissionFailure', () {
      const ex = PermissionException(message: 'No READ_PHONE_STATE', code: 'PERM_ERR');
      final failure = Failure.fromException(ex);
      expect(failure, isA<PermissionFailure>());
      expect(failure.message, 'No READ_PHONE_STATE');
      expect(failure.code, 'PERM_ERR');
    });

    test('Failure.fromException maps CacheException to CacheFailure', () {
      const ex = CacheException(message: 'Corrupt storage');
      final failure = Failure.fromException(ex);
      expect(failure, isA<CacheFailure>());
      expect(failure.message, 'Corrupt storage');
    });

    test('Failure.fromException maps NetworkException to NetworkFailure', () {
      const ex = NetworkException(message: 'Cellular disconnected');
      final failure = Failure.fromException(ex);
      expect(failure, isA<NetworkFailure>());
      expect(failure.message, 'Cellular disconnected');
    });

    test('Failure.fromException maps unexpected exceptions to UnexpectedFailure', () {
      final failure = Failure.fromException(const FormatException('Bad input'));
      expect(failure, isA<UnexpectedFailure>());
      expect(failure.message, contains('FormatException'));
    });

    test('Failures support value equality and hashCode', () {
      const f1 = DeviceFailure(message: 'Err', code: 'C1');
      const f2 = DeviceFailure(message: 'Err', code: 'C1');
      const f3 = DeviceFailure(message: 'Different', code: 'C1');

      expect(f1, equals(f2));
      expect(f1.hashCode, equals(f2.hashCode));
      expect(f1 == f3, isFalse);
    });
  });
}
