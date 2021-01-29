from flask import Flask, render_template, request,jsonify

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def BMI():
    BMI = 0
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        BMI = calc_bmi(weight, height)
    
    if BMI > 40:
        bmi_text = "Very severely obese"
    elif BMI > 35:
        bmi_text = "Severely obese"
    elif BMI > 30:
        bmi_text = "Moderately obese"
    elif BMI > 25:
        bmi_text = "Overweight"
    elif BMI > 18.5:
        bmi_text = "Normal (healthy weight)"
    elif BMI > 16:
        bmi_text = "Underweight"
    elif BMI > 15:
        bmi_text = "Severely underweight"
    elif BMI < 15:
        bmi_text = "Very severely underweight"
    else:
        bmi_text = ""

    data_set = {"BMI": BMI, "message": bmi_text}
    print(data_set)
    return render_template('bmi.html', data=data_set)

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