'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from primesieve import getPrimes

if __name__ == '__main__':
    print sum(getPrimes(2000000))