from flask import Flask, render_template,render_template_string, request
import pickle


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the form data here
        input_data = request.form.getlist()
        # Do something with the input_data list
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        return render_template_string( "Prediction of rain is : " + str(model.predict(input_data)[0]))
    


    return render_template('index.html')
    
    if __name__ == "__main__":
    app.run()