import 'package:flutter/material.dart';
import '../services/api_service.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'donor_dashboard.dart';

class LoginScreen extends StatelessWidget {
  LoginScreen({super.key});

  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Login")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: emailController,
              decoration: const InputDecoration(labelText: "Email"),
            ),
            TextField(
              controller: passwordController,
              decoration: const InputDecoration(labelText: "Password"),
              obscureText: true,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () async {
                final api = ApiService();

                final response = await api.login(
                  emailController.text,
                  passwordController.text,
                );

                print(response);

                if (response["access_token"] != null) {
                  // 1. Save the token securely
                  const storage = FlutterSecureStorage();
                  await storage.write(
                    key: "jwt_token",
                    value: response["access_token"],
                  );

                  // 2. Show Success Message
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text("Login Success")),
                  );

                  // 3. Navigate to Dashboard
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(
                      builder: (context) => const DonorDashboard(),
                    ),
                  );
                } else {
                  ScaffoldMessenger.of(
                    context,
                  ).showSnackBar(const SnackBar(content: Text("Login Failed")));
                }
              },
              child: const Text("Login"),
            ),
          ],
        ),
      ),
    );
  }
}
