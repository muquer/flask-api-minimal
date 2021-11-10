from app import app
from flask import jsonify

@app.route("/api/test", methods=["GET"])
def login():
    return jsonify({'info': 'this is a test json'})