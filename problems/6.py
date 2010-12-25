'''
The sum of the squares of the first ten natural numbers is 12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

if __name__ == '__main__':
    max = 100
    squareOfSum = pow((max * (max+1)) / 2, 2)
    sumOfSquares = (max * (max+1) * (2*max + 1)) / 6
    print squareOfSum - sumOfSquares