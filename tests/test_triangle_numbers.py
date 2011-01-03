'''
Triangle Number Unit Tests
'''
import unittest
from triangle_numbers import triangle_number

class Test(unittest.TestCase):

    def test_triangle_numbers(self):
        t = triangle_number()
        self.assertEquals(t.next(), 1)
        self.assertEquals(t.next(), 3)
        self.assertEquals(t.next(), 6)
        self.assertEquals(t.next(), 10)
        self.assertEquals(t.next(), 15)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()