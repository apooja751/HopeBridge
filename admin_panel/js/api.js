const BASE_URL = "http://127.0.0.1:8000";

// 🔐 Login
async function login(email, password) {
    const res = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    localStorage.setItem("token", data.access_token);
    return data;
}

// 📦 Get Requests
async function getRequests() {
    const token = localStorage.getItem("token");

    const res = await fetch(`${BASE_URL}/request`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    return await res.json();
}