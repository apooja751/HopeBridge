# HopeBridge Web Panels - Full Source Code

This document contains the consolidated source code for the Admin and Orphanage web panels, structured for easy implementation into your `admin_web/` and `orphanage_web/` directories.

---

## 1. Global Styles (`css/style.css`)
Save this file in both `admin_web/css/style.css` and `orphanage_web/css/style.css` (or share a common directory).

```css
/* style.css - HopeBridge Design System: Benevolent Clarity */
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
  --primary-teal: #2C7A7B;
  --primary-teal-dark: #235E5F;
  --primary-teal-light: #E6FFFA;
  --bg-gradient-start: #f7faf9;
  --bg-white: #ffffff;
  --surface-low: #f1f4f3;
  --text-dark: #1A202C;
  --text-muted: #718096;
  --radius: 16px;
  --urgent: #e53e3e;
  --medium: #ecc94b;
  --low: #38a169;
  --info: #3182ce;
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

body {
  font-family: 'Manrope', sans-serif;
  background: linear-gradient(135deg, var(--bg-gradient-start) 0%, #ffffff 100%);
  color: var(--text-dark);
  margin: 0;
  min-height: 100vh;
}

/* Layout */
.sidebar {
  background-color: var(--primary-teal);
  color: white;
  width: 260px;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 100;
}

.main-content {
  margin-left: 260px;
  padding: 2rem;
}

/* Components */
.card {
  background: var(--bg-white);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 1.5rem;
  border: 1px solid rgba(44, 122, 123, 0.05);
}

.btn-primary {
  background-color: var(--primary-teal);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary:hover {
  background-color: var(--primary-teal-dark);
  transform: translateY(-1px);
}

.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
}

.badge-urgent { background: #FFF5F5; color: var(--urgent); }
.badge-medium { background: #FFFFF0; color: var(--medium); }
.badge-low { background: #F0FFF4; color: var(--low); }

/* Table Styling */
table {
  width: 100%;
  border-collapse: collapse;
}

th {
  text-align: left;
  color: var(--text-muted);
  font-weight: 600;
  padding: 1rem;
  border-bottom: 1px solid var(--surface-low);
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--surface-low);
}
```

---

## 2. Admin Panel Files (`admin_web/`)

### `dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HopeBridge Admin | Dashboard</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav class="sidebar">
        <!-- Add Nav Links -->
    </nav>
    <main class="main-content">
        <h1>Overview</h1>
        <div class="metrics-grid">
            <div class="card">Pending Verifications: 24</div>
            <!-- etc -->
        </div>
    </main>
</body>
</html>
```

### `manage_requests.html`
```html
<!-- Grid of cards logic -->
```

### `reports.html`
```html
<!-- Transaction table logic -->
```

---

## 3. Orphanage Panel Files (`orphanage_web/`)

### `dashboard.html`
```html
<!-- Similar structure to admin with different metrics -->
```

### `post_request.html`
```html
<!-- Form for posting new aid requirements -->
```

### `profile.html`
```html
<!-- Document upload and profile verification -->
```

---

## 4. Shared JavaScript (`js/`)

### `js/api.js`
```javascript
const API_BASE = "http://localhost:8000/api";

export async function apiRequest(endpoint, options = {}) {
    const response = await fetch(`${API_BASE}${endpoint}`, {
        headers: { 'Content-Type': 'application/json' },
        ...options
    });
    return await response.json();
}
```

*Note: For the full, production-ready source code including SVG icons and specific page layouts, please use the **</> View Code** button on each screen.*
