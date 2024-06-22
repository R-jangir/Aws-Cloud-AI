import joblib
from sklearn.ensemble import IsolationForest
import numpy as np

def train_anomaly_detection_model(X_train):
    model = IsolationForest(n_estimators=100, contamination=0.1)
    model.fit(X_train)
    joblib.dump(model, 'anomaly_detection_model.pkl')

def detect_anomalies(X):
    model = joblib.load('anomaly_detection_model.pkl')
    return model.predict(X)
