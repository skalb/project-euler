'''
n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
'''
import math

if __name__ == '__main__':
    print sum(int(d) for d in str(math.factorial(100)))