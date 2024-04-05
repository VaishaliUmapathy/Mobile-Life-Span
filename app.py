from flask import Flask, render_template, request
#correct
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('mobile1.csv')

# Perform one-hot encoding on the 'brand' column
data = pd.get_dummies(data, columns=['brand'])

# Separating features and target variable
X = data.drop('usage', axis=1)
y = data['usage']

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting input values from the form
        storage_capacity = float(request.form['storage_capacity'])
        battery_capacity = float(request.form['battery_capacity'])
        rate = float(request.form['rate'])
        repair = float(request.form['repair'])
        repaired = float(request.form['repaired'])
        replacement = float(request.form['replacement'])
        charging = float(request.form['charging'])
        year = float(request.form['year'])
        app_usage = float(request.form['app_usage'])
        brand = request.form['brand']

        if f'brand_{brand}' in X.columns:
            input_data = {
                'storagecapacity': storage_capacity,
                'battreycapacity': battery_capacity,
                'rate': rate,
                'repair': repair,
                'repaired': repaired,
                'replacement': replacement,
                'charging': charging,
                'year': year,
                'appusage': app_usage
            }

            # Update the input_data for the selected brand
            input_data.update({col: 1 if col == f'brand_{brand}' else 0 for col in X.columns if col.startswith('brand_')})

            input_df = pd.DataFrame([input_data])

            # Predict usage
            predicted_usage = model.predict(input_df)[0]
            return render_template('index.html', result=f"Predicted Usage: {predicted_usage:.2f}")
        else:
            return render_template('index.html', result="Brand not found in the dataset.")
    except ValueError as e:
        return render_template('index.html', result=f"Error: {e}")
if __name__ == '__main__':
    app.run(debug=True)
