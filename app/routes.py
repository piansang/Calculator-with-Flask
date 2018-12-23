from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

from app import app

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/add', methods=['POST', 'GET'])
def addition():
    firstNum = request.args.get('firstNum', None)
    secondNum = request.args.get('secondNum', None)
    operator = request.args.get("operator")
    if(operator == 'Addition'):
        result = firstNum + secondNum
    if(operator == 'Subtraction'):
        result = firstNum - secondNum
    if(operator == 'Multiplication'):
        result = firstNum * secondNum
    if(operator == 'Division'):
        result = firstNum / secondNum
    else:
        result = 'INVALID'

    entry = result
    return render_template('add.html', entry = entry)



if __name__ == '__main__':
    app.run(debug=True)