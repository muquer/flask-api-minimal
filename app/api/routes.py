from app import app
from flask import jsonify, request
from flask import Response

@app.route("/api/test", methods=["GET"])
def get_test():
    return jsonify({'info': 'this is a test json'})


@app.route("/api/test", methods=["POST"])
def post_test():
    try:
        data = request.json
        data = data["test"]
        return jsonify({'info': 'this is a test json'})

    except:
        return Response(status=400)

    
    
    
