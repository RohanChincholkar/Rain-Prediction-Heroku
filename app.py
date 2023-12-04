from flask import Flask, render_template,render_template_string, request, redirect
import pickle
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    # return redirect(location="/predict", code=302)

@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the form data here
    #     input_data = request.form['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
    #    'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
    #    'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
    #    'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
    #    'Temp3pm', 'RainToday', 'year', 'month_sin', 'month_cos', 'day_sin',
    #    'day_cos']
        input_data = request.get_json()
        python_dict = json.loads(input_data)
        input_data = [value for key, value in python_dict.items()]


        input_data= list(map(float, input_data))
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        return "Prediction of rain is : " + str(model.predict(input_data))
    



    
    if __name__ == "__main__":
        app.run(debug=True)