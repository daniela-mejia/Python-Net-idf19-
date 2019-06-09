#TestAddVariables.py

#import statements
import unittest
import AssignVariables

class calSum(unittest.TestCase):
    #Formula for unittest method names is....
    #test_functionName_testDescription
    
    def test_calcSum(self):
        #Capture the results of the function
        result = AssignVariables.calcSum(10, 14)
        expected = 24
        #check for expected output
        self.assertEqual(expected, result)

#Run the tests

if __name__ == '__main__':
    unittest.main()
    
