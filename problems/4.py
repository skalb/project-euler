'''
Created on Dec 22, 2010

@author: Sameer
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