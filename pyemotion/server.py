from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import timedelta
import lightgbm as lgb
import numpy as np
import cv2
import os
import joblib
from auth import authenticate
from database import db, User
from llm_inference import analyze_text
from cnn_training import load_model, preprocess_image
from emotion_analysis import get_emotion_statistics

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify(message="Username and password are required."), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    logging.info(f"User registered: {username}")
    return jsonify(message="User registered successfully!"), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = authenticate(username, password)
    if user:
        logging.info(f"User logged in: {username}")
        return jsonify(message="Login successful!"), 200
    logging.warning(f"Login failed for user: {username}")
    return jsonify(message="Invalid credentials!"), 401

@app.route('/profile', methods=['GET'])
def profile():
    if 'user_id' not in session:
        return jsonify(message="User not logged in"), 401
    user = User.query.get(session['user_id'])
    return jsonify(username=user.username)

@app.route('/analyze/statistics', methods=['GET'])
def analyze_statistics():
    if 'user_id' not in session:
        return jsonify(message="User not logged in"), 401
    stats = get_emotion_statistics(session['user_id'])
    return jsonify(statistics=stats)

@app.route('/analyze/text', methods=['POST'])
def analyze_text_route():
    text = request.json.get('text')
    emotion = analyze_text_emotion(text)  # Use your LLM model for analysis
    return jsonify(emotion=emotion)

@app.route('/analyze/image', methods=['POST'])
def analyze_image_route():
    if 'image' not in request.files:
        return jsonify(error="No image provided"), 400
    image_file = request.files['image']
    img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = preprocess_image(img)  # Preprocess image for CNN
    model = load_model()  # Load your CNN model
    emotion = model.predict(img)  # Make a prediction
    return jsonify(emotion=emotion)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables if not exists
    app.run(host='0.0.0.0', port=5000)
