from flask import Flask, request, render_template, jsonify
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler

clf = load('breast-cancer-xgboostClassifier.joblib')
scaler = load('breast-cancer-standardScaler.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    print("Predict route hit")
    features = [float(x) for x in request.form.values()]
    print(features)

    # Select the features based on the specified indices
    final_features = np.array(features).reshape(1, -1)  # Reshape to 2D array
    final_features = scaler.transform(final_features)  # Transform using the pre-fitted scaler
    preds = clf.predict(final_features)
    if preds[0]== 1:
        result = 'Patients tumor is malignant, patient has breast cancer'
    else:
        result = "Patient's tumor is benign, patient doesn't have breast cancer"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
