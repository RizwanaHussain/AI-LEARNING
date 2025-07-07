from flask import Flask, render_template, request

app = Flask(__name__)

# Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    operation = ''
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        choice = request.form['operation']

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        else:
            result = "Invalid Operation Selected"
            operation = '❓'

        return render_template('result.html', num1=num1, num2=num2, operation=operation, result=result)
    
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
