import unittest
from Problem_4 import prob4

class TestProb4(unittest.TestCase):
    def test_sum_multi(self):
        #tests that answers are correct
        self.assertAlmostEqual(prob4(2),9009)
        self.assertAlmostEqual(prob4(3),906609)

if __name__ == '__main__':
    unittest.main()
