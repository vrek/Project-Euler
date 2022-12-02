"""This is a UNITTEST for Problem #2"""
import unittest
from Problem_2 import prob2

if __name__ == '__main__':
    unittest.main()

class TestProb2(unittest.TestCase):
    """This tests if problem 2 gives correct answers""" 
    def test_sum_multi(self):
        self.assertAlmostEqual(prob2(100),44)
        self.assertAlmostEqual(prob2(4e6),4613732)
