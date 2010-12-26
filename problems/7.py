'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from util import primesieve

if __name__ == '__main__':
    index = 10001
    
    # Let's choose a safe boundary at 100 * max
    primes = primesieve.getPrimes(index * 100)
    print primes[10001]