from flask import Flask, render_template, request
from math import cos, sin, tan, pi
app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST', 'GET'])
def form():
    num_1 = request.form.get('num_1')
    num_2 = float(request.form.get('num_2'))
    num_3 = int(request.form.get('num_3'))
    num_4 = request.form.get('num_4')

    arg = num_2
    if num_4 == 'on':
        answer = '°'
        num_2 = num_2 * pi / 180
    else:
        answer = 'рад'
    if num_1 == 'cos':
        str = 'cos'
        result = cos(num_2).__round__(num_3)
    elif num_1 == 'sin':
        str = 'sin'
        result = sin(num_2).__round__(num_3)
    elif num_1 == 'tan':
        str = 'tan'
        try:
            result = tan(num_2).__round__(num_3)
        except ZeroDivisionError:
            result = 'нет решения'
    elif num_1 == 'ctg':
        str = 'ctg'
        try:
            result = (1 / (tan(num_2))).__round__(num_3)
        except ZeroDivisionError:
            result = 'нет решения'
    else:
        str = 'такой функции нет'
        result = 'нет решения'
    ans = f'{str}({arg} {answer})={result}'

    return render_template('index.html', ans=ans)

app.run()