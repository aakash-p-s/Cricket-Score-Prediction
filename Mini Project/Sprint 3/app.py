from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your machine learning model
model = joblib.load('ml_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        batting_team = int(request.form['batting_team'])
        bowling_team = int(request.form['bowling_team'])
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        prev_5_overs_runs = int(request.form['prev_5_overs_runs'])
        prev_5_overs_wickets = int(request.form['prev_5_overs_wickets'])

        # Perform prediction using your model
        prediction = model.predict([[batting_team, bowling_team, runs, wickets, overs, prev_5_overs_runs, prev_5_overs_wickets]])

        return render_template('predict.html', prediction=int(round(prediction[0])))

    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
