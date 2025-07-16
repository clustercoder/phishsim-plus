# 🎣 Phishing Simulator & Awareness Game

This project is built for educational and cybersecurity awareness purposes. It consists of two main components:

1. **Phishing Page Generator** — Automatically clones the frontend of a website to simulate a phishing page with a dummy backend.
2. **Spot-the-Difference Game** — A gamified interface where users try to detect visual and behavioral differences between real and phishing websites.

> ❗ This tool is strictly for **educational, ethical, and awareness training** use. Do **not** use it for any illegal or malicious activities.

---

## 🧰 Tech Stack

- **Python**
  - Playwright for browser automation
  - BeautifulSoup for HTML parsing
  - Flask for backend simulation
- **HTML/CSS/JS** — for the simulated phishing pages

---

## 🚀 How to Run

### Step 1: Clone the Repo
```bash
git clone https://github.com/clustercoder/phishing-simulator.git
cd phishing-simulator
```

### Step 2: Install Dependencies
```bash
pip install flask playwright beautifulsoup4
playwright install
```

### Step 3: Scrape & Clone a Website
```bash
cd scraper
python scrape_and_modify.py
```

### Step 4: Run the Flask Server
```bash
cd ../backend
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## 📂 Project Structure

```
phishing_simulator/
├── scraper/
│   └── scrape_and_modify.py         # AI-assisted cloning script
├── backend/
│   ├── app.py                       # Flask backend
│   ├── templates/index.html         # Auto-generated phishing HTML
├── README.md
└── .gitignore
```

---

## ⚠️ Disclaimer

This project is for **research and awareness purposes only**. The authors are not responsible for any misuse. Always obtain permission before testing on any website or system.
