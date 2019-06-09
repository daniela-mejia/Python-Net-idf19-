#Test Hello world

import unittest
import HelloWorld

class obviousCode(unittest.TestCase):
    def test_HelloWorld (self):
        result = HelloWorld.words()
        expected = 'Hello World'

        self.assertEqual(expected, result)
if __name__ == '__main__':
    unittest.main()
