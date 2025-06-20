from flask import Flask, request, render_template
import numpy as np
import pickle
import os 

# Load models
dtr = pickle.load(open('D:\\EDP\\BP\\P3\\model\\dtr.pkl', 'rb'))
preprocessor = pickle.load(open('D:\\EDP\\BP\\P3\\model\\preprocessor.pkl', 'rb'))

# Flask app
template_dir = os.path.abspath('D:/EDP/BP/P3/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        Year = float(request.form['Year'])
        average_rain_fall_mm_per_year = float(request.form['average_rain_fall_mm_per_year'])
        pesticides_tonnes = float(request.form['pesticides_tonnes'])
        avg_temp = float(request.form['avg_temp'])
        Area = request.form['Area']
        Item = request.form['Item']

        # Create features array and preprocess
        features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = dtr.predict(transformed_features)

        return render_template('index.html', prediction=prediction[0])

    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', prediction="Error occurred during prediction")

if __name__ == "__main__":
    app.run(debug=True)

