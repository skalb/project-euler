'''
Prime Sieve

This module uses the Sieve of Eratosthenes 
to generate primes in range 1 to N

Original algorithm based on definition at: 
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Optimizations included from solution provided at: 
http://projecteuler.net/index.php?section=problems&id=3
'''

from math import ceil, sqrt

# Returns list of primes less than upper bound n
def get_primes(n):
    
    if n <= 1:
        return []

    # Determine the number of odd prime candidates
    sievebound = int(ceil(n-1) / 2) + 1

    # We know that for any number n with factors (a,b)
    # such that n = a * b, MIN(a,b) <= SQRT(n)
    # With this in mind, we only need to check factors
    # up to SQRT(n) since any factor greater would have a
    # corresponding smaller factor pair
    cross = int(ceil((sqrt(n)-1) / 2))

    # Initialize array of prime candidates
    # sieve[i] = 2 * i + 1 => 1, 3, 5...
    sieve = [False] * (sievebound)    
    sieve[0] = True

    # Test all n from 1...cross => 3..SQRT(n)
    for i in xrange(1, cross, 1):

        # By definition, any i with no factors is prime
        if sieve[i] == False:
            # We can now set each multiple of i to true 
            # since it can longer be prime
            # Sieving goes from candidate p^2 to 
            # sievebound with step p
            # If the nth element has value 2i + 1, 
            # then to get the index of p^2:
            # p to p^2 = (p^2 - 1)/2 
            #          = (4i^2 + 4i)/2 
            #          = 2i(i + 1)
            start = 2*i*(i+1)
            step = 2*i+1
            for j in xrange(start, sievebound, step):
                # Set the index j to true to
                # mark this number as having
                # factors and thus not prime
                sieve[j] = True

    # Since we ignore all even numbers, add 2 to our list
    primes = [2]
    
    # All candidates with no factors are prime numbers    
    for i in xrange(0, sievebound, 1):
        if sieve[i] == False:
            primes.append(2*i + 1)            
         
    return primes