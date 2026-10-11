import unittest
from app import predict


class TestPrediction(unittest.TestCase):

    def test_high(self):
        self.assertEqual(predict(75), "High")

    def test_low(self):
        self.assertEqual(predict(25), "Low")


if __name__ == "__main__":
    unittest.main()
