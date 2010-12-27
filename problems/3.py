'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from primesieve import getPrimes

if __name__ == '__main__':
    num = 600851475143
    
    # Largest distinct factor is <= to SQRT
    max = round(pow(600851475143, .5))
    
    primes = getPrimes(max)
    
    # Since we're looking for the largest, start at the end
    primes.reverse()
    
    for p in primes:
        if num % p == 0:
            print p
            break
