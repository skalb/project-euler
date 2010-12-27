'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from primesieve import getPrimes

if __name__ == '__main__':
    index = 10001    
    primes = getPrimes(1000000)
    print primes[index-1]