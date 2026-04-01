"""
Healthcare Symptom Checker - Backend API
Uses Groq LLM to analyze symptoms and suggest possible conditions.
FOR EDUCATIONAL PURPOSES ONLY - NOT A SUBSTITUTE FOR MEDICAL ADVICE.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
import sqlite3
import datetime
from groq import Groq

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API

# ─── Groq Client Setup ────────────────────────────────────────────────────────
from dotenv import load_dotenv
import os
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ─── Database Setup ───────────────────────────────────────────────────────────
DB_PATH = "symptom_history.db"

def init_db():
    """Create the database table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            symptoms    TEXT NOT NULL,
            response    TEXT NOT NULL,
            timestamp   TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_query(symptoms: str, response: str):
    """Save a symptom query and its response to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO queries (symptoms, response, timestamp) VALUES (?, ?, ?)",
        (symptoms, response, datetime.datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

# ─── LLM Prompt ───────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are a helpful medical information assistant for EDUCATIONAL purposes only.
You are NOT a licensed doctor and do NOT provide medical diagnoses.

When a user describes symptoms, you must:
1. List 3-5 POSSIBLE CONDITIONS (not diagnoses) that could match the symptoms.
2. For each condition, give a brief 1-2 sentence explanation.
3. Provide RECOMMENDED NEXT STEPS (e.g., rest, hydration, see a doctor, go to ER).
4. Mention RED FLAG symptoms that require immediate emergency care.
5. Always end with a clear DISCLAIMER.

Format your response as a JSON object with these keys:
{
  "possible_conditions": [
    {"name": "Condition Name", "description": "Brief explanation", "likelihood": "Common/Possible/Less Likely"}
  ],
  "next_steps": ["step 1", "step 2", ...],
  "red_flags": ["symptom 1 that needs emergency care", ...],
  "disclaimer": "Educational disclaimer text",
  "urgency_level": "Low/Medium/High/Emergency"
}

IMPORTANT: Always remind users to consult a real healthcare professional for actual diagnosis and treatment."""

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/", methods=["GET"])
def home():
    """Health check endpoint."""
    return jsonify({"status": "running", "message": "Healthcare Symptom Checker API is live!"})


@app.route("/api/check-symptoms", methods=["POST"])
def check_symptoms():
    """
    Main endpoint: accepts symptoms text, queries Groq LLM, returns analysis.

    Request body (JSON):
        { "symptoms": "I have a headache and fever for 2 days" }

    Response (JSON):
        { "success": true, "data": { ...LLM response... } }
    """
    try:
        # 1. Get the symptoms from the request
        body = request.get_json()
        if not body or "symptoms" not in body:
            return jsonify({"success": False, "error": "Please provide 'symptoms' in the request body."}), 400

        symptoms = body["symptoms"].strip()
        if len(symptoms) < 5:
            return jsonify({"success": False, "error": "Please describe your symptoms in more detail."}), 400

        # 2. Build the user message for the LLM
        user_message = f"""Based on these symptoms, suggest possible conditions and next steps with educational disclaimer.

Symptoms reported: {symptoms}

Please respond in the JSON format specified."""

        # 3. Call Groq API
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # Free model on Groq
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_message},
            ],
            temperature=0.3,    # Low temperature = more consistent medical info
            max_tokens=1500,
        )

        # 4. Parse the response
        raw_response = completion.choices[0].message.content

        # Try to parse as JSON (our prompt asks for JSON output)
        try:
            # Strip markdown code fences if present
            cleaned = raw_response.strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.split("```")[1]
                if cleaned.startswith("json"):
                    cleaned = cleaned[4:]
            result_data = json.loads(cleaned.strip())
        except json.JSONDecodeError:
            # If LLM didn't return valid JSON, wrap the text
            result_data = {
                "possible_conditions": [],
                "next_steps": ["Please consult a healthcare professional."],
                "red_flags": [],
                "disclaimer": raw_response,
                "urgency_level": "Unknown"
            }

        # 5. Save to database
        save_query(symptoms, json.dumps(result_data))

        # 6. Return the result
        return jsonify({"success": True, "data": result_data})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/history", methods=["GET"])
def get_history():
    """Return the last 10 symptom queries from the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, symptoms, timestamp FROM queries ORDER BY id DESC LIMIT 10")
        rows = cursor.fetchall()
        conn.close()

        history = [{"id": r[0], "symptoms": r[1], "timestamp": r[2]} for r in rows]
        return jsonify({"success": True, "history": history})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# ─── Run the Server ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    init_db()   # Create DB on startup
    print("✅ Database initialized")
    print("🚀 Starting Healthcare Symptom Checker API on http://localhost:5000")
    app.run(debug=True, port=5000)
