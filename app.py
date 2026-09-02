from flask import Flask, render_template, request

# Import your core logic modules
from add import add
from sub import subtract
from mult import multiply
from division import divide

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    num1 = None
    num2 = None
    operation = None

    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')

            if operation == 'add':
                result = add(num1, num2)
            elif operation == 'sub':
                result = subtract(num1, num2)
            # elif operation == 'mult':
            #     result = multiply(num1, num2)
            # elif operation == 'div':
            #     result = divide(num1, num2)
                
            # Formatting results cleanly if they are whole numbers
            if result is not None and result.is_integer():
                result = int(result)
                
        except ValueError as e:
            result = f"Error: {str(e)}"
        except Exception:
            result = "Invalid Input"

    return render_template('index.html', result=result, num1=num1, num2=num2, operation=operation)

if __name__ == '__main__':
    # Binds to port 80 globally to allow direct public IP browsing access
    app.run(host='0.0.0.0', port=80)

