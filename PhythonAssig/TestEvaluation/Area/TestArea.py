import unittest
import AreaTriangle

class Atriangle (unittest.TestCase):
    def test_area (self):
        result = AreaTriangle.Area_Triangle(5, 4)
        expected = result

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
    
