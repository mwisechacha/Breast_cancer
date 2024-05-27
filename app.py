from flask import Flask, request, render_template, jsonify
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler

clf = load('breast-cancer-xgboostClassifier.joblib')
scaler = StandardScaler()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    print("Predict route hit")
    features = [float(x) for x in request.form.values()]
    print(len(features))
    selected_features = [features[i] for i in range(9)]
    scaler.fit(selected_features)
    final_features = np.array(selected_features).reshape(1, -1)
    final_features = scaler.transform(final_features)    
    preds = clf.predict(final_features)
    
    if preds[0]== 1:
        result = 'Patients tumor is malignant, patient has breast cancer'
    else:
        result = "Patient's tumor is benign, patient doesn't have breast cancer"
    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
