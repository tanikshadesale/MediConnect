from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import sqlite3

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Database setup
def init_db():
    with sqlite3.connect('mediconnect.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT UNIQUE,
                          password TEXT)''')
        conn.commit()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    with sqlite3.connect('mediconnect.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (data['username'], data['password']))
            conn.commit()
            return jsonify({"message": "User registered successfully"}), 201
        except:
            return jsonify({"message": "Username already exists"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    with sqlite3.connect('mediconnect.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (data['username'], data['password']))
        user = cursor.fetchone()
        if user:
            token = create_access_token(identity=user[1])
            return jsonify(access_token=token)
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    hospitals = [
        {"name": "City Hospital", "location": "Downtown", "beds_available": 5},
        {"name": "Green Valley Clinic", "location": "Uptown", "beds_available": 2}
    ]
    return jsonify(hospitals)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get("message")
    return jsonify({"response": f"AI Bot: I received your message - {user_message}"})

@app.route('/emergency', methods=['GET'])
@jwt_required()
def emergency():
    return jsonify({"message": "Emergency services contacted!"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
