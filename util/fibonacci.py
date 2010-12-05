'''
Simple fibonacci generator
'''

def fibonacci():
    a = 1
    b = 2
    while 1:
        yield a
        a, b = b, a + b