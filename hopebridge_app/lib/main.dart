import 'package:flutter/material.dart';
import 'screens/login_screen.dart';
import 'utils/app_theme.dart'; // 👉 Added theme import
import 'screens/donor_dashboard.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false, // Removes the debug banner
      title: 'HopeBridge',
      theme: AppTheme.lightTheme, // 👉 Applied your custom Deep Teal theme
      home: DonorDashboard(),
    );
  }
}