import 'package:flutter/material.dart';
import 'presentation/screens/home_screen.dart';
import 'presentation/theme/app_theme.dart';

// إعادة التصدير لتوافقية ملفات الاختبار الموجودة التي تستورد HomeScreen من main.dart
export 'presentation/screens/home_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const NetModeApp());
}

class NetModeApp extends StatelessWidget {
  const NetModeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'NET Mode',
      // [FR-19] الثيم الداكن الرسمي الموحد من AppTheme
      theme: AppTheme.darkTheme,
      home: const HomeScreen(),
    );
  }
}

