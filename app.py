from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite veritabanını yapılandır
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Kullanıcı modelini tanımla
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    best_score = db.Column(db.Integer, nullable=False, default=0)

# Soru modelini tanımla
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    correct_answer = db.Column(db.String(80), nullable=False)

# Veritabanı tablolarını oluştur ve başlangıç verilerini ekle
with app.app_context():
    db.create_all()
    if not Question.query.first():  # Eğer sorular yoksa başlangıç verilerini ekle
        questions = [
            Question(question_text="Which Python library is used for deep learning?", correct_answer="TensorFlow"),
            Question(question_text="Select the correct statement:", correct_answer="1"),
            Question(question_text="Which library can be used directly to create a neural network model in Python?", correct_answer="PyTorch"),
            Question(question_text="Which of the following algorithms is a supervised learning algorithm?", correct_answer="SVM")
        ]
        db.session.add_all(questions)
        db.session.commit()

@app.route('/')
def home():
    return render_template('quiz_template.html')

@app.route('/submit', methods=['POST'])
def submit_quiz():
    username = request.form.get('username')
    answers = {
        "question1": request.form.get('question1'),
        "question2": request.form.get('question2'),
        "question3": request.form.get('question3'),
        "question4": request.form.get('question4')
    }

    # Veritabanındaki doğru cevaplara göre puanı hesapla ve kullanıcı yanıtlarını topla
    score = 0
    question_results = []
    questions = Question.query.all()
    for i, question in enumerate(questions, start=1):
        user_answer = answers.get(f'question{i}')
        is_correct = user_answer and user_answer.strip().lower() == question.correct_answer.strip().lower()
        if is_correct:
            score += 10
        question_results.append({
            'question': question.question_text,
            'correct_answer': question.correct_answer,
            'user_answer': user_answer or "No answer",
            'is_correct': is_correct
        })

    # Kullanıcıyı veritabanına ekle veya güncelle
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username, best_score=score)
        db.session.add(user)
    db.session.commit()

    # Tüm kullanıcılar arasında en yüksek puanı bul
    highest_score = db.session.query(db.func.max(User.best_score)).scalar()

    return jsonify({
        'score': score,
        'highest_score': highest_score,
        'questions': question_results
    })

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/get_best_score')
def get_best_score():
    best_score = db.session.query(db.func.max(User.best_score)).scalar() or 0
    return jsonify({'best_score': best_score})

@app.route('/view_data')
def view_data():
    users = User.query.all()
    questions = Question.query.all()
    return render_template('view_data.html', users=users, questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
