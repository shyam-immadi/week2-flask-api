from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def caliculator(val1,val2,operator):
    result = None
    if operator == "add":
        result = val1 + val2
    elif operator == "subtract":
        result = val1-val2
    elif operator == "multiply":
        result = val1 * val2
    elif operator == "divide":
        result = val1 / val2
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perform',methods=['GET','POST'])
def perform():
    data = request.get_json()
    print(data)
    if 'var1' not in data or 'var2' not in data or 'operation' not in data:
        return jsonify("please enter the necessary parameters")
    
    
    var1 = float(data.get('var1'))
    var2 = float(data.get('var2'))
    operator = data.get('operation')

    result = caliculator(var1,var2,operator)
    return jsonify({'result':result})


if __name__ == "__main__":
    app.run(debug=True)