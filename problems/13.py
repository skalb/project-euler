'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''

if __name__ == '__main__':
    with open('../input/13.txt') as file:
        lines = file.readlines()
    
        # Only the first 11 digits will affect the final 10 digits
        numbers = [long(l[:12]) for l in lines]
        print str(sum(numbers))[:10]
    
    # Also in 1 (messy) line for fun    
    print str(sum([long(l[:12]) for l in open('../input/13.txt').readlines()]))[:10]