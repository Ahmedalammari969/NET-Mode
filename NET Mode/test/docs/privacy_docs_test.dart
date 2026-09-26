import 'dart:io';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('Issue #18: Play Store Privacy & Data Safety Documentation', () {
    test('PRIVACY_POLICY.md exists and covers zero transmission, user control, contacts info', () {
      final file = File('docs/PRIVACY_POLICY.md');
      expect(file.existsSync(), isTrue);
      final content = file.readAsStringSync();
      expect(content, contains('Zero Remote Transmission'));
      expect(content, contains('No Third-Party Sharing'));
      expect(content, contains('READ_PHONE_STATE'));
      expect(content, contains('support@talabatuk.app'));
    });

    test('DATA_SAFETY.md exists and contains standard Google Play answers and reviewer justification', () {
      final file = File('docs/DATA_SAFETY.md');
      expect(file.existsSync(), isTrue);
      final content = file.readAsStringSync();
      expect(content, contains('Google Play Console Data Safety Guide'));
      expect(content, contains('English Reviewer Justification'));
      expect(content, contains('cellular network diagnostic and radio mode switcher utility'));
      expect(content, contains('clearPatternHistory'));
    });
  });
}
