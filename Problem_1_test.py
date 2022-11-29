import unittest
from Problem_1 import prob1

if __name__ == '__main__':
    unittest.main()

class TestProb1(unittest.TestCase):
    def test_sum_multi(self):
        #tests that answers are correct
        self.assertAlmostEqual(prob1(10,3,5),23)
        self.assertAlmostEqual(prob1(1000,3,5),233168)
