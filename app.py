from flask import Flask, request, render_template, jsonify
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler

clf = load('breast-cancer-xgboostClassifier.joblib')
scaler = load('breast-cancer-standardScaler.joblib')

selected_feature_indices = [21, 22, 8, 24, 28, 27, 29, 14, 23]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    print("Predict route hit")
    features = [float(x) for x in request.form.values()]
    print(features)  # Print the features to verify

    # Check that the length of features matches the expected number
    if len(features) != 9:
        return "Invalid number of features submitted. Expected 9 features."

    # Select the features based on the specified indices
    selected_features = [features[i] for i in selected_feature_indices]
    final_features = np.array(selected_features).reshape(1, -1)  # Reshape to 2D array
    final_features = scaler.transform(final_features)  # Transform using the pre-fitted scaler
    preds = clf.predict(final_features)
    if preds[0]== 1:
        result = 'Patients tumor is malignant, patient has breast cancer'
    else:
        result = "Patient's tumor is benign, patient doesn't have breast cancer"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
