'''
Prime Sieve Unit Tests
'''
import unittest
from primesieve import get_primes

class Test(unittest.TestCase):

    def test_primes(self):
        self.assertEquals(get_primes(0), [])
        self.assertEquals(get_primes(1), [])
        self.assertEquals(get_primes(2), [2])
        self.assertEquals(get_primes(3), [2,3])
        self.assertEquals(get_primes(20), [2,3,5,7,11,13,17,19])

if __name__ == "__main__":
    unittest.main()
