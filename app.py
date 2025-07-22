from flask import Flask, jsonify
import os

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "✅ Backend is working! Try /api/profile or /api/gaps"

# Simulated profile data
@app.route('/api/profile')
def get_profile():
    return jsonify({
        "name": "Amit",
        "role": "Java Developer",
        "skills": ["Java", "OOP", "MySQL"]
    })

# Skill gap analysis
@app.route('/api/gaps')
def get_gaps():
    current_skills = set(["Java", "OOP", "MySQL"])
    required_skills = set(["Java", "Spring Boot", "Concurrency"])
    missing_skills = list(required_skills - current_skills)
    return jsonify({"missing_skills": missing_skills})

# Run app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
