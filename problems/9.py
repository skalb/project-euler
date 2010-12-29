'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# a^2 + b^2 = c^2
# For every m, n where m > n
# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2

if __name__ == '__main__':
    m = 2
    found = False
    while not found:
        for n in xrange(1, m, 2):
            a = pow(m,2) - pow(n,2)
            b = 2 * m * n
            c = pow(m,2) + pow(n,2)
            if a + b + c == 1000:
                print a * b * c
                found = True
                break
        m = m + 1
                
        