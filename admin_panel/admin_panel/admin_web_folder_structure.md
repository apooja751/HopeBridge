# HopeBridge Admin Web Panel - Folder Structure

Below is the organized source code for the Admin Web Panel, structured according to your requirements. 

## Folder: `admin_web/`

### 1. `admin_web/css/style.css`
This file contains the core design tokens and styling based on the **Benevolent Clarity** design system.

```css
/* admin_web/css/style.css */
:root {
  --primary-teal: #2C7A7B;
  --bg-gradient-start: #f7faf9;
  --bg-white: #ffffff;
  --text-dark: #2d3748;
  --text-muted: #718096;
  --radius: 16px;
  --urgent: #e53e3e; /* Red */
  --medium: #ecc94b; /* Yellow */
  --low: #38a169;    /* Green */
  --info: #3182ce;   /* Blue */
}

body {
  font-family: 'Poppins', 'Inter', sans-serif;
  background: linear-gradient(135deg, var(--bg-gradient-start) 0%, #ffffff 100%);
  color: var(--text-dark);
}

.sidebar {
  background-color: var(--primary-teal);
  color: white;
  width: 260px;
  height: 100vh;
  position: fixed;
  border-radius: 0 var(--radius) var(--radius) 0;
}

.card {
  background: var(--bg-white);
  border-radius: var(--radius);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  border: none;
}

.btn-primary {
  background-color: var(--primary-teal);
  border: none;
  border-radius: 12px;
}

/* Status Badges */
.badge-urgent { background-color: var(--urgent); color: white; }
.badge-medium { background-color: var(--medium); color: white; }
.badge-low { background-color: var(--low); color: white; }
```

### 2. `admin_web/dashboard.html`
The main overview page featuring charts and the verification list.

```html
<!-- admin_web/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="css/style.css">
    <title>HopeBridge | Admin Dashboard</title>
</head>
<body>
    <div class="sidebar">
        <!-- Sidebar Navigation -->
    </div>
    <main class="main-content">
        <header>
            <h1>Overview</h1>
            <div class="admin-profile">...</div>
        </header>
        
        <!-- Metrics Cards -->
        <div class="metrics-grid">
            <div class="card">Pending Verifications: 24</div>
            <div class="card">Total Orphanages: 142</div>
        </div>

        <!-- Charts Section -->
        <div class="charts-row">
            <div class="card" id="donation-trend"></div>
            <div class="card" id="donation-types"></div>
        </div>

        <!-- Table -->
        <div class="card">
            <h3>Verification List</h3>
            <table>...</table>
        </div>
    </main>
    <script src="js/script.js"></script>
</body>
</html>
```

### 3. `admin_web/manage_requests.html`
Grid view of active humanitarian aid requests.

```html
<!-- admin_web/manage_requests.html -->
<div class="requests-grid">
    <!-- Loop through requests -->
    <div class="card">
        <span class="badge badge-urgent">URGENT</span>
        <h4>Funding for New Mattresses</h4>
        <div class="progress">
            <div class="progress-bar" style="width: 75%"></div>
        </div>
        <button class="btn-primary">Approve</button>
    </div>
</div>
```

### 4. `admin_web/reports.html`
Financial and transaction history page.

```html
<!-- admin_web/reports.html -->
<div class="card">
    <h3>Recent Transactions</h3>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Gateway</th>
                <th>Amount</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <!-- Stripe, Razorpay, PayPal entries -->
        </tbody>
    </table>
</div>
```

### 5. `admin_web/js/script.js`
Handles charts and UI interactions.

```javascript
// admin_web/js/script.js
// Initialize Charts (e.g., using Chart.js)
const ctxTrend = document.getElementById('donation-trend').getContext('2d');
new Chart(ctxTrend, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Donation Trend',
            borderColor: '#2C7A7B',
            backgroundColor: 'rgba(44, 122, 123, 0.1)',
            fill: true
        }]
    }
});
```

### 6. `admin_web/js/api.js`
Standard functions for connecting to your FastAPI backend.

```javascript
// admin_web/js/api.js
const API_BASE = "http://localhost:8000/api";

async function fetchRequests() {
    const response = await fetch(`${API_BASE}/requests/`);
    return await response.json();
}
```

---
*Note: You can view the full, production-ready code for each page by selecting a screen on the canvas and clicking the **</> View Code** button.*
