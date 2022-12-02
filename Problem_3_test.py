"""This is a UNITTEST for Problem #3"""
import unittest
from Problem_3 import prob3

if __name__ == '__main__':
    unittest.main()

class TestProb3(unittest.TestCase):
    """Test that Problem Set 3 is running correctly"""
    def test_sum_multi(self):
        self.assertAlmostEqual(prob3(13195),29)
        self.assertAlmostEqual(prob3(600851475143),6857)