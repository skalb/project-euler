'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

if __name__ == '__main__':
    start = 999
    end = 100
    
    largest = 0
    
    for i in xrange(start, end, -1):
        for j in xrange(start, i-1, -1):
            n = i * j
            
            # No need to keep checking since numbers will only get smaller
            if n < largest:
                break
                        
            candidate = str(n)
            
            # Slice and stride to reverse
            if candidate == candidate[::-1] and n > largest:
                largest = n
                
    print largest