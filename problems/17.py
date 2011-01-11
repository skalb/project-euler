'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

ones_lookup = { 0:"", 1:"one", 2:"two", 3:"three", 4:"four", 
                5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

teens_lookup = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
                15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen" }

tens_lookup = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 
               6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}   

def get_written_number(n):
    if n < 10:
        return ones_lookup[n]
    if n < 20:
        return teens_lookup[n]
    if n < 100:
        tens = int(n/10)
        ones = n - tens * 10
        return tens_lookup[tens] + " " + get_written_number(ones)    
    if n == 100:
        return "one hundred"  
    if n < 1000:
        hundreds = int(n/100)
        tens = n - hundreds * 100
        return ones_lookup[hundreds] + " hundred and " + get_written_number(tens)
  
    return "one thousand"
    

if __name__ == '__main__':
    written_numbers = [get_written_number(n) for n in xrange(1,1001,1)]
    
    # Need to strip spaces!
    print sum (len(w.replace(' ', '')) for w in written_numbers)
    