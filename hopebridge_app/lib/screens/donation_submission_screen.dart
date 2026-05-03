import 'package:flutter/material.dart';
import '../utils/app_theme.dart';

class DonationSubmissionScreen extends StatefulWidget {
  final String orphanageName;

  const DonationSubmissionScreen({super.key, required this.orphanageName});

  @override
  State<DonationSubmissionScreen> createState() =>
      _DonationSubmissionScreenState();
}

class _DonationSubmissionScreenState extends State<DonationSubmissionScreen> {
  String _donationType = 'Money'; // Toggle between 'Money' and 'Item'

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.backgroundLight,
      appBar: AppBar(
        title: const Text(
          "Make a Donation",
          style: TextStyle(color: AppTheme.textDark),
        ),
        backgroundColor: AppTheme.backgroundLight,
        elevation: 0,
        iconTheme: const IconThemeData(color: AppTheme.primaryTeal),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              "Donating to: ${widget.orphanageName}",
              style: const TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: AppTheme.primaryTeal,
              ),
            ),
            const SizedBox(height: 24),

            // 1. TOGGLE: Money or Items
            const Text(
              "What would you like to donate?",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                color: AppTheme.textDark,
              ),
            ),
            const SizedBox(height: 8),
            Row(
              children: [
                Expanded(
                  child: RadioListTile<String>(
                    title: const Text("Money", style: TextStyle(fontSize: 14)),
                    value: 'Money',
                    groupValue: _donationType,
                    activeColor: AppTheme.primaryTeal,
                    contentPadding: EdgeInsets.zero,
                    onChanged: (value) =>
                        setState(() => _donationType = value!),
                  ),
                ),
                Expanded(
                  child: RadioListTile<String>(
                    title: const Text("Items", style: TextStyle(fontSize: 14)),
                    value: 'Item',
                    groupValue: _donationType,
                    activeColor: AppTheme.primaryTeal,
                    contentPadding: EdgeInsets.zero,
                    onChanged: (value) =>
                        setState(() => _donationType = value!),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 24),

            // 2. DYNAMIC FORM FIELDS
            if (_donationType == 'Money') ...[
              _buildTextField(
                "Amount (₹)",
                Icons.currency_rupee,
                isNumber: true,
              ),
              const SizedBox(height: 16),
              const Text(
                "Secure Payment Gateway (Razorpay/Stripe) will process this safely.",
                style: TextStyle(color: AppTheme.textGrey, fontSize: 12),
              ),
            ] else ...[
              _buildTextField(
                "Item Description (e.g. 10 Books)",
                Icons.description,
              ),
              const SizedBox(height: 16),
              _buildTextField("Quantity", Icons.numbers, isNumber: true),
              const SizedBox(height: 16),
              _buildTextField("Pickup Address", Icons.location_on),
              const SizedBox(height: 16),
              _buildTextField(
                "Preferred Pickup Date (DD/MM/YYYY)",
                Icons.calendar_today,
              ),
            ],

            const SizedBox(height: 40),

            // 3. SUBMIT BUTTON
            SizedBox(
              width: double.infinity,
              height: 50,
              child: ElevatedButton(
                onPressed: () {
                  // Show success message and go back
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(
                      content: Text(
                        "Donation submitted successfully! Thank you.",
                      ),
                    ),
                  );
                  Navigator.pop(context); // Returns to Dashboard
                },
                child: const Text(
                  "Confirm Donation",
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // Helper Widget for clean TextFields with the Deep Teal theme
  Widget _buildTextField(String label, IconData icon, {bool isNumber = false}) {
    return Container(
      decoration: BoxDecoration(
        color: AppTheme.white,
        borderRadius: BorderRadius.circular(12),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.1),
            blurRadius: 8,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: TextField(
        keyboardType: isNumber ? TextInputType.number : TextInputType.text,
        decoration: InputDecoration(
          labelText: label,
          prefixIcon: Icon(icon, color: AppTheme.textGrey),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(
            vertical: 16,
            horizontal: 16,
          ),
        ),
      ),
    );
  }
}
