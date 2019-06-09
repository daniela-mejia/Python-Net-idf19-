#TestKilometersvsMiles

import unittest
import Kilometers 
    

class converter(unittest.TestCase):
    def test_kilometers (self):
        result = Kilometers.kmCalc(50)
        expected = result 
        self.assertEqual(expected, result)
if __name__ == '__main__':

    unittest.main()
        
