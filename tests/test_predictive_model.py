import unittest
import pandas as pd
from predictive_model import train_predictive_model, forecast_future

class TestPredictiveModel(unittest.TestCase):
    def test_predictive_model(self):
        data = {
            'ds': pd.date_range(start='2023-01-01', periods=100),
            'y': range(100)
        }
        df = pd.DataFrame(data)
        train_predictive_model(df)
        forecast = forecast_future(30)
        self.assertTrue(len(forecast) > 0)

if __name__ == '__main__':
    unittest.main()
