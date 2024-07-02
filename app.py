from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongo-service:27017/')
db = client.student_db
students = db.students


@app.route('/create', methods=['POST'])
def create_student():
    data = request.json
    students.insert_one(data)
    return jsonify({"message": "Student record created successfully"}), 201


@app.route('/get', methods=['GET'])
def get_students():
    student_list = list(students.find({}, {'_id': 0}))
    return jsonify(student_list), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

