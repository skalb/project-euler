'''
Prime Sieve Unit Tests
'''
import unittest
from primesieve import getPrimes

class Test(unittest.TestCase):

    def testPrimes(self):
        self.assertEquals(getPrimes(0), [])
        self.assertEquals(getPrimes(1), [])
        self.assertEquals(getPrimes(2), [2])
        self.assertEquals(getPrimes(3), [2,3])
        self.assertEquals(getPrimes(20), [2,3,5,7,11,13,17,19])

if __name__ == "__main__":
    unittest.main()
