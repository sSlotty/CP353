from flask import Flask, render_template, request,jsonify

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def BMI():
    BMI = ''
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        BMI = calc_bmi(weight, height)

    return render_template('bmi.html', data=BMI)

@app.route('/bmi2', methods=['POST'])
def BMI2():

    data = request.json
    weight = data['weight']
    height = data['height']
    BMI = calc_bmi(weight, height)
    return_data = {"weight":weight, "height":height, "bmi":BMI}
    
    return jsonify(return_data)


def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)