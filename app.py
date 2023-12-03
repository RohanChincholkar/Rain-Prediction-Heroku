from flask import Flask, render_template,render_template_string, request
import pickle


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the form data here
        input_data = request.form.getlist(['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
       'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
       'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
       'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
       'Temp3pm', 'RainToday', 'year', 'month_sin', 'month_cos', 'day_sin',
       'day_cos'])
        input_data= list(map(float, input_data))
        # Do something with the input_data list
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        return render_template_string( "Prediction of rain is : " + str(model.predict(input_data)))
    



    
    if __name__ == "__main__":
        app.run(debug=True)