#TestCalculatorFunctions.py

#import statements
import unittest
import CalculatorFunctions

class KnownValues(unittest.TestCase):
    #Formula for unittest method names is....
    #test_functionName_testDescription
    
    def test_calculateBMI_forLowerBoundary(self):
        #Capture the results of the function
        result = CalculatorFunctions.calculateBMI(58,91)
        expected = 19
        #check for expected output
        self.assertEqual(expected, result)

#Run the tests

if __name__ == '__main__':
    unittest.main()
    
