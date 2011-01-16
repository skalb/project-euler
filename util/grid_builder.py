'''
Converts input file of numbers into 2D array
'''

def get_grid(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        
        grid = [[int(c) for c in l.split(" ")] for l in lines]
        return grid