// init-mongo.js
db = db.getSiblingDB('student_db');
db.createCollection('students');
