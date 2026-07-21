from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Microservice!",
        "service": "user-service",
        "version": "1.0.0",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/users')
def get_users():
    users = [
        {"id": 1, "name": "Adarsh"},
        {"id": 2, "name": "Priya"},
        {"id": 3, "name": "Rahul"}
    ]
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)