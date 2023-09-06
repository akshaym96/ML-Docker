from flask import Flask, jsonify, request
import joblib

#Used to create a Flask web application instance.
app = Flask(__name__)

# Load the above-saved model
model = joblib.load('titanic_prediction_v1.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Extract features from the input data 
    # Assume you need only below 3 features to predict.
    features = [data['Pclass'], data['Age'], data['SibSp']]

    # Perform predictions using the loaded model
    predictions = model.predict_proba([features])

    # Return the predictions as JSON response
    return jsonify({'predictions': predictions.tolist()})


#If you're running the script directly, __name__ will be "__main__", and Flask will know to use the current directory as the root path.
#If you're importing the script as a module in another script, __name__ will be set to the module's name, and Flask will use that to determine the correct root path.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)