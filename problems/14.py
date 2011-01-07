'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n ->  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

from datetime import datetime

def get_next(n):
    # Check lowest bit for odd. Slightly faster than modulo!
    if n & 1:
        return 3 * n + 1
    else:
        return n / 2        

if __name__ == '__main__':
    start = datetime.now()
    maxCount, startingNumber = 0,0
    cache = {}
    
    for n in xrange(2,1000000,1):
        count = 0
        num = n
        while num > 1:
            if cache.has_key(num):
                count = count + cache[num]
                break
            else:
                num = get_next(num)   
                count = count + 1
    
        cache[n] = count
    
        if count > maxCount:
            startingNumber = n
            maxCount = count
    
    print startingNumber
    print (datetime.now() - start).microseconds / 100