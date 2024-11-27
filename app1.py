from flask import Flask, render_template, request
from model import LoyaltyScorePredictor

app = Flask(__name__)
predictor = LoyaltyScorePredictor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {
            'Age': int(request.form['age']),
            'Items Purchased': int(request.form['items_purchased']),
            'Total Spent': float(request.form['Total Spent']),
            'Discount (%)': float(request.form['Discount (%)']),
            'Satisfaction Score': float(request.form['satisfaction_score']),
            'Warranty Extension': int(request.form['Warranty Extension']),
            'Gender': request.form['gender'],
            'Region': request.form['region'],
            'Product Category': request.form['product_category'],
            'Payment Method': request.form['payment_method'],
            'Revenue': float(request.form['Revenue']),
            'Store Rating': float(request.form['store_rating']),
            'Membership Status': float(request.form['membership_status_value']),
            'Preferred Visit Time': request.form['preferred_visit_time']  # Closing parenthesis added
        }

        prediction = predictor.predict(input_data)

        return render_template('result.html', prediction=prediction)

    except Exception as e:  # Add error handling for unexpected issues
        print("An error occurred:", e)
        return render_template('error.html')  # Optionally, render an error page

if __name__ == '__main__':
    app.run(debug=True)