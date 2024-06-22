from fbprophet import Prophet
import joblib
import pandas as pd

def train_predictive_model(df):
    model = Prophet()
    model.fit(df)
    joblib.dump(model, 'predictive_model.pkl')

def forecast_future(periods=365):
    model = joblib.load('predictive_model.pkl')
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
