## Demo Video
[Watch here](https://www.loom.com/share/27cc85858e9a4089ae5b0daeb507275f)


# 🩺 MediCheck — AI Healthcare Symptom Checker

AI-powered symptom checker built using **Python (Flask)**, **Grok LLM (xAI)**, and **HTML/CSS/JavaScript**.

> **Disclaimer:** This project is for educational purposes only and does not replace professional medical advice.

---

## Features

- Input symptoms in natural language
- AI suggests possible conditions
- Shows likelihood of conditions
- Provides recommended next steps
- Identifies emergency red-flag symptoms
- Displays urgency level
- Stores query history in SQLite
- Simple responsive frontend

---

## Project Structure

```
healthcare-symptom-checker/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   └── index.html
└── README.md
```

---

## Setup

### 1. Get API Key

Create an API key from  
https://console.x.ai/

---

### 2. Backend Setup

```bash
cd backend

python -m venv venv

# Activate virtual environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
```

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 3. Run Server

```bash
python app.py
```

Server runs at:

```
http://localhost:5000
```

---

### 4. Open Frontend

Open this file in your browser:

```
frontend/index.html
```

---

## API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | `/` | Server status |
| POST | `/api/check-symptoms` | Analyze symptoms |
| GET | `/api/history` | Last 10 queries |

---

## Example Request

```bash
curl -X POST http://localhost:5000/api/check-symptoms \
-H "Content-Type: application/json" \
-d '{"symptoms":"fever and headache"}'
```

---

## Tech Stack

- **LLM:** Grok (xAI)
- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
