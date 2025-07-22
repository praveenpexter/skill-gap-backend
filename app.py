from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

learners = [
    {
        "name": "Amit",
        "role": "Java Developer",
        "skill_score": 66,
        "gaps": ["Concurrency", "Spring Boot"],
        "course_progress": {
            "Java Multithreading – Udemy": "Done",
            "Thread Lifecycle in Java – YouTube": "In Progress"
        }
    },
    {
        "name": "Priya",
        "role": "Python Developer",
        "skill_score": 85,
        "gaps": [],
        "course_progress": {
            "Python OOP – Udemy": "Done",
            "AsyncIO Crash Course": "Done"
        }
    },
    {
        "name": "John",
        "role": "Frontend Developer",
        "skill_score": 40,
        "gaps": ["React State", "JSX"],
        "course_progress": {
            "React Basics – YouTube": "Not Started",
            "JSX Deep Dive – Medium": "Not Started"
        }
    }
]

@app.route('/')
def home():
    return "✅ Backend is working! Try /api/profile, /api/quiz, /api/admin/learners"

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
    required_skills = set(["Java", "Spring Boot", "Concurrency"])
    missing_skills = list(required_skills - current_skills)
    return jsonify({"missing_skills": missing_skills})

@app.route('/api/quiz')
def get_quiz():
    quiz = [
        {"question": "What is a thread in Java?", "options": ["Class", "Object", "Lightweight process", "Function"], "answer": 2},
        {"question": "Which Java class is used to create a thread?", "options": ["Runnable", "Callable", "Thread", "Executor"], "answer": 2},
        {"question": "What does 'synchronized' keyword do?", "options": ["Stops thread", "Locks method", "Runs fast", "None"], "answer": 1}
    ]
    for q in quiz:
        q.pop("answer")
    return jsonify(quiz)

@app.route('/api/submit-quiz', methods=['POST'])
def submit_quiz():
    correct_answers = [2, 2, 1]
    data = request.json
    user_answers = data.get("answers", [])
    score = sum([1 for ua, ca in zip(user_answers, correct_answers) if ua == ca])
    percent = int((score / len(correct_answers)) * 100)
    return jsonify({
        "score": percent,
        "message": f"You scored {percent}%. " + ("Well done!" if percent >= 70 else "You should study more.")
    })

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.json
    score = data.get("score", 0)
    if score < 70:
        return jsonify({
            "recommendations": [
                {"id": 1, "title": "Java Multithreading – Udemy"},
                {"id": 2, "title": "Thread Lifecycle – YouTube"},
                {"id": 3, "title": "Java Synchronization – Blog Article"}
            ]
        })
    else:
        return jsonify({
            "recommendations": [
                {"id": 0, "title": "✅ You scored well! No additional learning required."}
            ]
        })

@app.route('/api/admin/learners')
def get_all_learners():
    return jsonify(learners)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)

