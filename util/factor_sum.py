'''
Utility to returns the sum of a given number's factors
'''

from primesieve import get_primes
from math import sqrt
from math import floor
from math import pow

class factor_sum:
    primes = {}
    
    def __init__(self, max):        
        # Store all the primes up to the max number to speed up calls
        for p in get_primes(max):
            self.primes[p] = True
        
    def get_factor_sum(self, n):
        if n <= 1:
            return 0
        # If the number is prime, it will only have two factors: itself and 1
        if self.primes.has_key(n):
            return 1
        
        sum = 1
        
        start, step, max = 2, 1, int(floor(sqrt(n)))
        if n & 1:
            start, step = 3, 2
            
        for i in xrange(start, max, step):
            if n % i == 0:
                sum += i + n / i
                
        # Special case for perfect squares
        if pow(max, 2) == n:
            sum += max

        return sum
    