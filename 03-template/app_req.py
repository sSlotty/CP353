from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/score', methods=['GET'])
def score():
    val1 = request.args.get('val1', default = 1, type=int)
    val2 = request.args.get('val2', default=0.5, type=float)
    return f"val1 is {val1}, val2 is {val2}"
    
@app.route('/user',methods=['POST'])
def user():
    data = request.json
    return jsonify(data)

@app.route('/bmi', methods=['GET'])
def BMI():
    weight = request.args.get('weight',default = 0, type = int)
    height = request.args.get('height', default=0, type=int)
    
    BMI = calc_bmi(weight, height)
    return render_template('bmi.html', data = BMI)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)