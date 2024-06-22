from flask import Flask, render_template, jsonify
import predictive_model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predictions')
def get_predictions():
    # Example data for demonstration
    predictions = {
        "anomalies": [{"timestamp": "2023-01-01T00:00:00Z", "value": 120}],
        "cost_predictions": [{"timestamp": "2023-01-02T00:00:00Z", "value": 110}]
    }
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
