## Demo Video
[Watch here](https://www.loom.com/share/27cc85858e9a4089ae5b0daeb507275f)


[README.md](https://github.com/user-attachments/files/26421958/README.md)
[README.md](https://github.com/user-attachments/files/26421958/README.md)
# 🩺 MediCheck — AI Healthcare Symptom Checker

> **For Educational Purposes Only.** This tool uses AI to suggest possible conditions. It is NOT a substitute for professional medical advice, diagnosis, or treatment.

A full-stack AI-powered symptom checker built with **Python (Flask)** + **Grok LLM (xAI)** + **HTML/CSS/JavaScript**.

---

## 📸 Features

- 🔍 Input symptoms in plain English
- 🤖 Grok AI analyzes and returns:
  - Possible conditions with likelihood ratings
  - Recommended next steps
  - Red flag symptoms requiring emergency care
  - Urgency level (Low / Medium / High / Emergency)
- 🗄️ SQLite database stores query history
- 🌐 Clean, responsive frontend interface
- ⚠️ Medical disclaimer on every response

---

## 🗂️ Project Structure

```
healthcare-symptom-checker/
├── backend/
│   ├── app.py              ← Flask API server (main backend)
│   ├── requirements.txt    ← Python dependencies
│   └── .env                ← API key (DO NOT commit to GitHub!)
├── frontend/
│   └── index.html          ← Frontend UI
└── README.md
```

---

## ⚙️ Setup Instructions

### Step 1 — Get Your Grok API Key

1. Go to [https://console.x.ai/](https://console.x.ai/)
2. Sign in or create a free account
3. Navigate to **API Keys** and create a new key
4. Copy the key

### Step 2 — Set Up the Backend

```bash
# 1. Go to the backend folder
cd backend

# 2. Create a Python virtual environment (keeps things clean)
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Add your API key to the .env file
# Open .env and replace "your_grok_api_key_here" with your actual key
```

### Step 3 — Run the Backend

```bash
# Make sure you are in the backend/ folder with venv activated
python app.py
```

You should see:
```
✅ Database initialized
🚀 Starting Healthcare Symptom Checker API on http://localhost:5000
```

### Step 4 — Open the Frontend

Simply open `frontend/index.html` in your browser (double-click it).

That's it! Type your symptoms and click **Analyze Symptoms**.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET  | `/` | Health check |
| POST | `/api/check-symptoms` | Analyze symptoms |
| GET  | `/api/history` | View past 10 queries |

### Example API Request

```bash
curl -X POST http://localhost:5000/api/check-symptoms \
  -H "Content-Type: application/json" \
  -d '{"symptoms": "headache and fever for 2 days"}'
```

### Example Response

```json
{
  "success": true,
  "data": {
    "possible_conditions": [
      {
        "name": "Viral Upper Respiratory Infection",
        "description": "A common cold caused by a virus...",
        "likelihood": "Common"
      }
    ],
    "next_steps": [
      "Rest and stay hydrated",
      "Take over-the-counter fever reducers if needed",
      "See a doctor if fever exceeds 103°F or persists beyond 3 days"
    ],
    "red_flags": [
      "Difficulty breathing",
      "Chest pain",
      "Severe headache with stiff neck"
    ],
    "urgency_level": "Low",
    "disclaimer": "This information is for educational purposes only..."
  }
}
```

---

## 🚀 Pushing to GitHub

```bash
# In the root project folder:
git init
git add .
git commit -m "Initial commit: Healthcare Symptom Checker"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/healthcare-symptom-checker.git
git push -u origin main
```

> ⚠️ **Important:** Make sure `.env` is in your `.gitignore` so your API key is never uploaded!

Create a `.gitignore` file with:
```
.env
venv/
__pycache__/
*.db
```

---

## 🎥 Recording a Demo Video

Use any free screen recorder:
- **Windows:** Xbox Game Bar (Win + G)
- **Mac:** QuickTime Player
- **Online:** [loom.com](https://loom.com) (free, easy)

Show: typing symptoms → clicking Analyze → seeing the AI results.

---

## 🛡️ Safety & Disclaimers

- Every response includes a clear educational disclaimer
- The AI is prompted to always recommend consulting a real doctor
- The system identifies emergency red flag symptoms
- This tool does NOT store personally identifiable information

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Grok (xAI) via OpenAI-compatible API |
| Backend | Python, Flask, Flask-CORS |
| Database | SQLite (built into Python) |
| Frontend | HTML, CSS, Vanilla JavaScript |

---

*Built for Unthinkable Solutions recruitment assignment — Educational AI Project*
