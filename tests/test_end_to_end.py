import unittest
import anomaly_detection
import predictive_model
import lambda_function

class TestEndToEnd(unittest.TestCase):
    def test_end_to_end(self):
        # Simulate data ingestion
        X_train = np.random.randn(100, 3)
        anomaly_detection.train_anomaly_detection_model(X_train)
        
        # Run anomaly detection
        anomalies = anomaly_detection.detect_anomalies(X_train)
        self.assertEqual(len(anomalies), 100)
        
        # Simulate predictive model training and forecasting
        data = {
            'ds': pd.date_range(start='2023-01-01', periods=100),
            'y': range(100)
        }
        df = pd.DataFrame(data)
        predictive_model.train_predictive_model(df)
        forecast = predictive_model.forecast_future(30)
        self.assertTrue(len(forecast) > 0)

        # Simulate automated response
        response = lambda_function.lambda_handler({}, {})
        self.assertTrue('StartingInstances' in response)

if __name__ == '__main__':
    unittest.main()
