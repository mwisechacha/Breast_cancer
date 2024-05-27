from flask import Flask, request, render_template, jsonify
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler

clf = load('models/breast-cancer-xgboostClassifier.joblib')
scaler = StandardScaler()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    final_features = scaler.transform(final_features)    
    preds = clf.predict(final_features)
    if preds[0] == 1:
        return render_template('index.html', prediction_text='The patient has breast cancer')
    else:
        return render_template('index.html', prediction_text='The patient does not have breast cancer')

@app.route('/predict_api',methods=['POST'])
def predict_api():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
