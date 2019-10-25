from flask import Flask
from flask import render_template, request
import random
import comment
from comment import generate_lit_comments, Student, main

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    out = ""
    return render_template('index.html', out=out)


@app.route('/', methods=['POST'])
def comment():
    student_name = request.form['student_name']
    exam_grade = int(request.form['exam_grade'])
    part_grade = int(request.form['part_grade'])
    homework_grade = int(request.form['homework_grade'])
    adj1 = request.form['adj1']
    adj2 = request.form['adj2']
    adj3 = request.form['adj3']
    gen = generate_lit_comments(student_name, exam_grade, part_grade, homework_grade, adj1, adj2, adj3)

    out = gen
    return render_template('index.html', out=out)

    
if __name__ == '__main__':
    app.run()
