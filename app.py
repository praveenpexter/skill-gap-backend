from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Skill Gap Backend is Running on Render!"

@app.route('/api/profile')
def get_profile():
    return jsonify({
        "name": "Amit",
        "role": "Java Developer",
        "skills": ["Java", "OOP", "MySQL"]
    })

@app.route('/api/gaps')
def get_gaps():
    current_skills = set(["Java", "OOP", "MySQL"])
    required_skills = set(["Java", "Spring Boot", "Microservices", "MySQL"])
    gaps = list(required_skills - current_skills)
    return jsonify({"skill_gaps": gaps})

# ✅ Production-ready settings: Bind to 0.0.0.0 and use Render's port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

