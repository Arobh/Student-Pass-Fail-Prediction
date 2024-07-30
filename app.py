# app.py

from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
 
# Load the dataset
url = 'https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/student-pass-fail-data.csv'
df = pd.read_csv(url)

# Data preprocessing
X = df[['Self_Study_Daily', 'Tutorials_Monthly']].values
y = df['Pass_Or_Fail'].values

# Train the model
model = LinearRegression() 
model.fit(X, y)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    self_study = float(request.form['self_study'])
    tutorials = float(request.form['tutorials'])
    
    # Predict probability of passing (0 to 100%)
    prediction = model.predict([[self_study, tutorials]])
    probability = prediction[0] * 100  # Convert to percentage
    
    # Ensure probability is between 0 and 100
    probability = min(max(probability, 0), 100)
      
    return jsonify({'result': probability})   

if __name__ == '__main__':
    app.run(debug=True)
