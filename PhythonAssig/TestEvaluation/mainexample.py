import unittest
from Calculator import Calculator

class TddInPhyton(unittest.Testcase):

    def test_calculator(self):
        calc= Calculator()
        result = calc.add (2,2)
        self.asserEqual(4,result)
    def test_calc_return(self):
        self.asserEqual
