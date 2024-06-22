import unittest
import numpy as np
from anomaly_detection import train_anomaly_detection_model, detect_anomalies

class TestAnomalyDetection(unittest.TestCase):
    def test_anomaly_detection(self):
        X_train = np.random.randn(100, 3)
        train_anomaly_detection_model(X_train)
        anomalies = detect_anomalies(X_train)
        self.assertEqual(len(anomalies), 100)

if __name__ == '__main__':
    unittest.main()
