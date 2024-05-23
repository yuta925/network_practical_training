from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('a4-2.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    x = data.get('x', 0)
    y = data.get('y', 0)
    operation = data.get('operation')

    if operation == 'add':
        x += y
    elif operation == 'subtract':
        x -= y
    elif operation == 'multiply':
        x *= y
    elif operation == 'divide':
        if y != 0:
            x = x // y  # Integer division
        else:
            return jsonify({'error': 'Division by zero is not allowed'}), 400

    return jsonify({'x': x})

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5001)
    
