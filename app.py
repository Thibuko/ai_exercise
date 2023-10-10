from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json

app = Flask(__name__)

# Load questions from the JSON file
with open('questions.json', 'r') as json_file:
    data = json.load(json_file)
    questions = data["questions"]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    question_responses = []

    for question in questions:
        user_answer = request.form.get(question['question'])
        correct_answer = question['correct_answer']

        if user_answer == correct_answer:
            score += 1

        question_responses.append((question['question'], user_answer, correct_answer))

    return render_template('result.html', score=score, total_questions=len(questions), question_responses=question_responses)

if __name__ == '__main__':
    app.secret_key = 'your_secret_key_here'
    app.run()
