from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained ML pipeline
model = joblib.load('model/pipeline.pkl')


@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    probability = None

    yn_map = {'Yes': 1, 'No': 0}


    if request.method == 'POST':
        data = {
            'Tenure Months': int(request.form['tenure']),
            'Monthly Charges': float(request.form['MonthlyCharges']),
            'Total Charges': float(request.form['TotalCharges']),
            'Contract': request.form['Contract'],
            'Payment Method': request.form['PaymentMethod'],
            'Internet Service': request.form['InternetService'],
            'Online Security': request.form['OnlineSecurity'],
            'Tech Support': request.form['TechSupport'],
            
            'Senior Citizen': yn_map[request.form['SeniorCitizen']],
            'Partner': yn_map[request.form['Partner']],
            'Dependents': yn_map[request.form['Dependents']],
            'Paperless Billing': yn_map[request.form['PaperlessBilling']]
        }


        df = pd.DataFrame([data])

        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]

        prediction = "Yes" if pred == 1 else "No"
        probability = round(prob * 100, 2)

    return render_template(
        'index.html',
        prediction=prediction,
        probability=probability
    )


if __name__ == '__main__':
    app.run(debug=True)
