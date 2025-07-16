# 🛡️ PhishSim+ – Rogue Wi-Fi & Phishing Attack Simulator (Awareness Training Only)

> ⚠️ **Disclaimer:** This project is strictly for cybersecurity education and internal awareness training. It must **never** be used for unauthorized or malicious activities. All demonstrations must be done in isolated environments with informed participants.

---

## 🎯 Objective

PhishSim+ is a cybersecurity awareness toolkit that simulates phishing attacks in a **controlled, ethical setting** using:

- ✅ A **rogue Wi-Fi access point**
- ✅ A **screenshot-based phishing page** — preserving the look of a real site
- ✅ A Flask backend that captures fake credentials and logs keystrokes
- ✅ Tools like **Wifiphisher** and **Bettercap** to simulate MITM threats

Rather than duplicating the full website, this toolkit captures a **snapshot (screenshot)** of the target site and overlays a **simulated login form** — making it **lighter, faster, and safer**.

---

## 🧱 Project Architecture

```
phishing-simulator/
├── scraper/                  → Takes screenshot + extracts login form
│   └── screenshot_and_form.py
├── backend/                  → Flask app to display phishing page
│   ├── app.py
│   ├── templates/index.html
│   └── static/keylogger.js
├── rogue_ap/                 → WiFi scripts (Wifiphisher / Airgeddon configs)
│   └── setup_wifi.sh
├── requirements.txt          → Python dependencies
└── README.md
```

---

## 🔧 Technologies Used

| Component              | Stack / Tools Used                                |
|------------------------|---------------------------------------------------|
| 📸 Page Snapshot        | Playwright (screenshot)                          |
| 🧠 Form Cloning         | BeautifulSoup HTML parser                        |
| 🌐 Web Server           | Flask (Python)                                   |
| 🧠 Keylogger Injection  | JavaScript + DOM event logging                   |
| 📡 Rogue Wi-Fi AP       | Wifiphisher / Airgeddon                          |
| 👁️ Sniffing             | Bettercap, Wireshark (demo only)                |

---

## 🔌 Requirements

To install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

### `requirements.txt` contents:

```
flask
beautifulsoup4
playwright
```

---

## 🚀 How It Works

### 🔹 Phase 1: Screenshot + Form Extract

1. Run:
   ```bash
   python scraper/screenshot_and_form.py
   ```
2. Enter the **target URL**
3. The tool will:
   - Take a **screenshot** of the full page
   - Extract the login `<form>` from the HTML
   - Save a combined phishing view:
     - Screenshot as a background
     - Real-looking (modified) form on top

---

### 🔹 Phase 2: Host the Phishing Page

```bash
cd backend/
python app.py
```

Open `http://localhost:5000` to view the simulated phishing page.

---

### 🔹 Phase 3: Set Up Rogue Wi-Fi (Kali or Raspberry Pi)

> Requires supported Wi-Fi adapter (e.g., Alfa AWUS036NHA)

#### 🛠 Option 1: Wifiphisher

```bash
sudo wifiphisher
```

Steps:
1. Choose your wireless adapter and select "Evil Twin" mode
2. Pick a nearby AP (e.g., "Office_WiFi")
3. When asked, select **“Custom phishing page”**
4. Point to your `backend/` folder

#### 🛠 Option 2: Airgeddon

```bash
sudo bash airgeddon.sh
```

Steps:
- Select:
  - Fake AP + DHCP + Web server
  - Choose "Custom Captive Portal"
- Point to `backend/templates/index.html`

---

### 🔹 Phase 4: Simulate Credential Capture

As users enter credentials:
- Terminal shows:
  ```bash
  [Captured] user: test@example.com  pass: hunter2
  [Keystrokes] t-e-s-t-@-e-x...
  ```

You can also view logs or optionally show Wireshark packets (if HTTPS isn’t forced).

---

## 🧠 Awareness Use Case (Live Demo)

🟢 Create a Wi-Fi network: `Company_Guest_Free`  
🟢 Let users connect, redirect to your phishing page  
🟢 Show real-time credential capture + JS keylog  
🟢 End with a powerful debrief:

> “This was all staged. But this is **exactly** what can happen in cafes, airports, or fake office networks.”

---

## 📁 Logs (Optional)

Captured credentials and keystrokes can be stored to file or shown on screen.

> Logs are **never** sent remotely. The simulation is local and ethical.

---

## 🛡️ Ethical Use Policy

You **must**:
- Only use this in test labs, cyber ranges, or private isolated networks
- Inform participants before or immediately after
- Never capture real credentials

This project is for **white-hat cybersecurity training** only.

---

## 👨‍💻 Credits

Built by [Mantek Singh Burn]  
Project developed under [The Developers Club]  
Special thanks to the open-source community

---
