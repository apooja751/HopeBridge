import 'package:flutter/material.dart';

class AppTheme {
  // Primary Brand Colors
  static const Color primaryTeal = Color(0xFF2C7A7B);
  static const Color backgroundLight = Color(0xFFF4F9F9); // Light mint/white
  static const Color white = Colors.white;

  // Status Colors
  static const Color urgentRed = Color(0xFFE53E3E);
  static const Color mediumYellow = Color(0xFFD69E2E);
  static const Color lowGreen = Color(0xFF38A169);
  static const Color infoBlue = Color(0xFF3182CE);

  // Text Colors
  static const Color textDark = Color(0xFF2D3748);
  static const Color textGrey = Color(0xFF718096);

  // Global Theme Data
  static ThemeData get lightTheme {
    return ThemeData(
      primaryColor: primaryTeal,
      scaffoldBackgroundColor: backgroundLight,
      appBarTheme: const AppBarTheme(
        backgroundColor: backgroundLight,
        elevation: 0,
        iconTheme: IconThemeData(color: primaryTeal),
        titleTextStyle: TextStyle(
          color: textDark,
          fontSize: 20,
          fontWeight: FontWeight.bold,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: primaryTeal,
          foregroundColor: white,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
          padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 24),
        ),
      ),
    );
  }
}