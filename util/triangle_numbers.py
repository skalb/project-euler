'''
Simple triangle number generator
'''

def triangle_number():
    a = 1
    b = 2
    while 1:
        yield a
        a,b = a+b, b+1