import 'package:flutter/material.dart';
import 'presentation/screens/home_screen.dart';

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
      theme: ThemeData(
        brightness: Brightness.dark,
        scaffoldBackgroundColor: const Color(0xFF0F172A),
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFF38BDF8),
          secondary: Color(0xFF818CF8),
        ),
      ),
      home: const HomeScreen(),
    );
  }
}
