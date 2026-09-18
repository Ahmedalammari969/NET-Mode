import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'إتقان Flutter - تطبيق تحفيزي',
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: Colors.transparent,
        textTheme: const TextTheme(
       
        ),
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      home: const Directionality(
        textDirection: TextDirection.rtl,
        child: MotivationalApp(),
      ),
    );
  }
}


class MotivationalApp extends StatefulWidget {
  const MotivationalApp({super.key});

  @override
  State<MotivationalApp> createState() => _MotivationalAppState();
}

class _MotivationalAppState extends State<MotivationalApp> {
  final List<String> _quotes = [
    'ابدأ الآن — أفضل وقت للعمل على فكرتك هو اليوم.',
    'لا تنتظر الإتقان، ابدأ بالإجراءات البسيطة.',
    'الفشل خطوة نحو النجاح — تعلّم ثم انطلق أقوى.',
    'ثقة واحدة في نفسك تصنع فرقاً كبيراً.',
    'كل سطر كود تكتبه يقربك من حلمك.'
  ];

  int _index = 0;
  bool _showCredit = false;

  void _next() {
    setState(() {
      if (_index < _quotes.length - 1) {
        _index++;
      } else {
        _showCredit = true;
      }
    });
  }

  void _restart() {
    setState(() {
      _index = 0;
      _showCredit = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final bool isLast = _index == _quotes.length - 1;
    return Scaffold(
      body: Stack(
        children: [
          // الخلفية والواجهة
          Container(
            width: double.infinity,
            height: double.infinity,
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  Color(0xFF6A11CB),
                  Color(0xFF2575FC),
                ],
              ),
            ),
            child: SafeArea(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  // العنوان
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 24.0),
                    child: Text(
                      'تطبيق تحفيزي',
                      style: TextStyle(
                        color: Colors.white.withOpacity(0.95),
                        fontSize: 36, // زيادة حجم الخط
                        fontWeight: FontWeight.bold,
                        letterSpacing: 1.5,
                        fontFamily: 'Arial', // تغيير الخط إلى Arial للوضوح
                      ),
                      textAlign: TextAlign.center,
                    ),
                  ),
                  const SizedBox(height: 40),
                  // البطاقة الرئيسية
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 20.0),
                    child: Container(
                      constraints: const BoxConstraints(minHeight: 220, maxWidth: 700),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(30),
                        border: Border.all(color: Colors.white.withOpacity(0.3)),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.2),
                            offset: const Offset(0, 10),
                            blurRadius: 30,
                          ),
                        ],
                      ),
                      padding: const EdgeInsets.all(25),
                      child: Center(
                        child: AnimatedSwitcher(
                          duration: const Duration(milliseconds: 600),
                          transitionBuilder: (child, animation) {
                            return FadeTransition(opacity: animation, child: child);
                          },
                          child: _showCredit
                              ? Column(
                            key: const ValueKey('credit'),
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(
                                Icons.emoji_events_rounded,
                                size: 80,
                                color: Colors.amber.shade600,
                              ),
                              const SizedBox(height: 12),
                              Text(
                                'مبروك! أنت الآن أقرب لتحقيق هدفك.',
                                style: TextStyle(
                                  fontSize: 22,
                                  fontWeight: FontWeight.w700,
                                  color: Colors.white,
                                  fontFamily: 'Arial', // استخدام خط واضح
                                ),
                                textAlign: TextAlign.center,
                              ),
                              const SizedBox(height: 18),
                              Text(
                                'برمجة وتنفيذ المطور:\nعيسى الجماعي',
                                style: TextStyle(
                                  fontSize: 16,
                                  color: Colors.white.withOpacity(0.85),
                                  fontWeight: FontWeight.w500,
                                  fontFamily: 'Arial', // استخدام خط واضح
                                ),
                                textAlign: TextAlign.center,
                              ),
                            ],
                          )
                              : Container(
                            key: ValueKey(_index),
                            padding: const EdgeInsets.symmetric(
                                horizontal: 14, vertical: 10),
                            child: Column(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Text(
                                  _quotes[_index],
                                  style: TextStyle(
                                    fontSize: 26, // زيادة حجم الخط
                                    color: Colors.white,
                                    height: 1.5, // زيادة المسافة بين الأسطر
                                    fontWeight: FontWeight.w700,
                                    fontFamily: 'Arial', // استخدام خط واضح
                                  ),
                                  textAlign: TextAlign.center,
                                ),
                                const SizedBox(height: 12),
                                Text(
                                  'نصيحة ${_index + 1} من ${_quotes.length}',
                                  style: TextStyle(
                                    fontSize: 16, // زيادة حجم النص
                                    color: Colors.white.withOpacity(0.8),
                                    fontFamily: 'Arial', // استخدام خط واضح
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 26),
                  // الأزرار
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          elevation: 15,
                          backgroundColor: Colors.white,
                          foregroundColor: Colors.deepPurple,
                          padding: const EdgeInsets.symmetric(horizontal: 22, vertical: 14),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(25)),
                          shadowColor: Colors.black.withOpacity(0.3),
                        ),
                        onPressed: _showCredit ? _restart : _next,
                        child: Text(
                          _showCredit ? 'إعادة' : (isLast ? 'إنهاء' : 'التالي'),
                          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w600),
                        ),
                      ),
                      const SizedBox(width: 12),
                      OutlinedButton(
                        style: OutlinedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
                          side: BorderSide(color: Colors.white.withOpacity(0.2)),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(25)),
                        ),
                        onPressed: () {
                          // مشاركة الفكرة أو حفظ
                          ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(content: Text('شارك الحافز مع صديق!')),
                          );
                        },
                        child: Text(
                          'مشاركة',
                          style: TextStyle(color: Colors.white.withOpacity(0.95), fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 40),
                  // مؤشر بسيط في الأسفل
                  AnimatedOpacity(
                    duration: const Duration(milliseconds: 400),
                    opacity: _showCredit ? 1.0 : 0.9,
                    child: Text(
                      _showCredit
                          ? 'برمجة وتنفيذ المطور عيسى الجماعي'
                          : 'ابدأ رحلتك الآن — خطوة صغيرة كل يوم',style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w600),    ),
                  ),
                ],
              ),
            ),
          ),
          // الفوتر
          Positioned(
            bottom: 0,
            left: 0,
            right: 0,
            child: Container(
              color: Colors.black.withOpacity(0.8), // لون خلفية الفوتر
              padding: const EdgeInsets.symmetric(vertical: 15),
              child: Column(
                children: [
                  Text(
                    'برمجة وتنفيذ: المهندس عيسى الجماعي',
                    style: TextStyle(
                      fontSize: 18,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      letterSpacing: 1.2,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'رقم الجوال: 775346074',
                    style: TextStyle(
                      fontSize: 20,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}


