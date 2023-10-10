from flask import Flask, render_template, request, redirect, url_for, flash, session
import json

app = Flask(__name__)

# Load questions from the JSON file
with open('questions.json', 'r') as json_file:
    data = json.load(json_file)
    questions = data["questions"]

# Initialize the session variables
app.secret_key = 'your_secret_key_here'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    # Initialize or reset session variables
    session['question_index'] = 0
    session['score'] = 0
    session['question_responses'] = []

    return render_template('index.html', question=questions[0])

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the user's answer for the current question
    user_answer = request.form.get('user_answer')

    # Get the current question and correct answer
    current_question = questions[session['question_index']]
    correct_answer = current_question['correct_answer']

    # Check if the user's answer is correct
    if user_answer == correct_answer:
        session['score'] += 1

    # Store the user's response for the current question
    session['question_responses'].append({
        'question': current_question['question'],
        'user_answer': user_answer,
        'correct_answer': correct_answer
    })

    # Move to the next question or display the result
    session['question_index'] += 1

    if session['question_index'] < len(questions):
        return render_template('index.html', question=questions[session['question_index']])
    else:
        return redirect(url_for('result'))

@app.route('/result')
def result():
    correct_count = sum(1 for response in session['question_responses'] if response['user_answer'] == response['correct_answer'])
    incorrect_count = len(session['question_responses']) - correct_count
    return render_template('result.html', score=session['score'], total_questions=len(questions),
                           question_responses=session['question_responses'],
                           correct_count=correct_count, incorrect_count=incorrect_count)


if __name__ == '__main__':
    app.run()
