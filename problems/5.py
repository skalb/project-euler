'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from util import primesieve
import math

if __name__ == '__main__':    
    max = 20    
    numbers = range(2,max+1,1)
    primes = primesieve.getPrimes(numbers[-1])
    result = 1   
    
    # Per the fundamental theorem of arithmetic:
    # http://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    # Every number can be factored as a multiple of primes in the form:
    # p1 ^ i1 * p2 ^ i2 * p3 ^ i3 ... pi ^ in
    # Therefore, the only numbers we need to multiply are the primes, but
    # the tricky part is to figure out the specific exponents of each prime
    # To do that we would need to determine the largest exponent of our prime 
    # that would "fit" in the number           
    
    for p in primes:
        
        # We need to find the smallest integer that satisfies this
        # p^x <= max <= p^(x+1)
        # x * log(p) = log(max)
        # x = log(max) / log(p)
        # x = floor(log(max)/log(p)
        
        x = math.floor(math.log(max)/math.log(p))
        result = result * pow(p, x)
        
    print int(result)