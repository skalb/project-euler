'''
Created on Oct 28, 2010

@author: Sameer
'''
import unittest
from util.fibonacci import fibonacci

class Test(unittest.TestCase):


    def testName(self):
        f = fibonacci()
        self.assertEquals(f.next(), 1)
        self.assertEquals(f.next(), 2)
        self.assertEquals(f.next(), 3)
        self.assertEquals(f.next(), 5)
        self.assertEquals(f.next(), 8)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()