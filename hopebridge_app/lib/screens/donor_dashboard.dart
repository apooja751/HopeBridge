import 'package:flutter/material.dart';
import '../utils/app_theme.dart';
import '../widgets/donation_card.dart';


class DonorDashboard extends StatelessWidget {
  const DonorDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.backgroundLight,
      // 1. APP BAR (Header)
      appBar: AppBar(
        backgroundColor: AppTheme.backgroundLight,
        elevation: 0,
        title: Row(
          children: [
            Icon(Icons.volunteer_activism, color: AppTheme.primaryTeal),
            const SizedBox(width: 8),
            const Text(
              "HopeBridge",
              style: TextStyle(
                color: AppTheme.primaryTeal,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
        actions: [
          IconButton(
            icon: const Icon(
              Icons.notifications_none,
              color: AppTheme.textDark,
            ),
            onPressed: () {},
          ),
          const Padding(
            padding: EdgeInsets.only(right: 16.0),
            child: CircleAvatar(
              radius: 16,
              backgroundImage: NetworkImage(
                "https://i.pravatar.cc/100",
              ), // Placeholder Avatar
            ),
          ),
        ],
      ),

      // 2. BODY
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Title
              const Text(
                "Browse Active Requests",
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.textDark,
                ),
              ),
              const SizedBox(height: 16),

              // Search and Filters Row
              Row(
                children: [
                  // Search Bar (Location)
                  Expanded(
                    flex: 2,
                    child: Container(
                      height: 40,
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
                      child: const TextField(
                        decoration: InputDecoration(
                          hintText: "Location...",
                          hintStyle: TextStyle(fontSize: 13),
                          prefixIcon: Icon(
                            Icons.search,
                            size: 20,
                            color: AppTheme.textGrey,
                          ),
                          border: InputBorder.none,
                          contentPadding: EdgeInsets.symmetric(vertical: 12),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),

                  // Priority Filter Button
                  Container(
                    height: 40,
                    padding: const EdgeInsets.symmetric(horizontal: 12),
                    decoration: BoxDecoration(
                      color: AppTheme.white,
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: Colors.grey.shade300),
                    ),
                    child: const Center(
                      child: Text(
                        "Priority ⌄",
                        style: TextStyle(
                          color: AppTheme.textDark,
                          fontSize: 13,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),

                  // Orphanage Filter Button
                  Container(
                    height: 40,
                    padding: const EdgeInsets.symmetric(horizontal: 12),
                    decoration: BoxDecoration(
                      color: AppTheme.white,
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: Colors.grey.shade300),
                    ),
                    child: const Center(
                      child: Text(
                        "Orphanage ⌄",
                        style: TextStyle(
                          color: AppTheme.textDark,
                          fontSize: 13,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),

              // Placeholder for Donation Cards
              // List of Donation Cards
              const DonationCard(
                orphanageName: "The Little Blossom Orphanage",
                title: "Funding for New Mattresses",
                progress: 0.60,
                amountRaised: "2400",
                targetAmount: "4000",
                imageUrl:
                    "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=500&q=80",
              ),
              const DonationCard(
                orphanageName: "Hope Village",
                title: "School Books for 50 Children",
                progress: 0.85,
                amountRaised: "850",
                targetAmount: "1000",
                imageUrl:
                    "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=500&q=80",
              ),
              const DonationCard(
                orphanageName: "Sunshine Home",
                title: "Monthly Grocery Supplies",
                progress: 0.30,
                amountRaised: "300",
                targetAmount: "1000",
                imageUrl:
                    "https://images.unsplash.com/photo-1542838132-92c53300491e?q=80&w=500", // 👉 New reliable grocery image
              ),
            ],
          ),
        ),
      ),

      // 3. BOTTOM NAVIGATION BAR
      bottomNavigationBar: BottomNavigationBar(
        selectedItemColor: AppTheme.primaryTeal,
        unselectedItemColor: AppTheme.textGrey,
        showUnselectedLabels: true,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: "Search"),
          BottomNavigationBarItem(
            icon: Icon(Icons.favorite_border),
            label: "Donate",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person_outline),
            label: "Profile",
          ),
        ],
      ),
    );
  }
}
