'''
Factor Sum unit test
'''
import unittest
from factor_sum import factor_sum


class Test(unittest.TestCase):
    def testName(self):
        f = factor_sum(1000)
        self.assertEquals(f.get_factor_sum(0), 0)
        self.assertEquals(f.get_factor_sum(1), 0)
        self.assertEquals(f.get_factor_sum(2), 1)
        self.assertEquals(f.get_factor_sum(10), 1 + 2 + 5)
        self.assertEquals(f.get_factor_sum(23), 1)
        self.assertEquals(f.get_factor_sum(25), 1 + 5)
        self.assertEquals(f.get_factor_sum(100), 1 + 2 + 50 + 4 + 20 + 5 + 25 + 10)
        self.assertEquals(f.get_factor_sum(220), 284)
        self.assertEquals(f.get_factor_sum(284), 220)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()