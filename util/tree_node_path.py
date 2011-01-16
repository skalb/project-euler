'''
Return max path from a m x n grid of values that represents a tree
'''

from util.tree_node import tree_node

def get_max_tree_node_path(grid):
    
    # Hold all nodes to reference parents when creating children
    branches = []
    
    for rowIndex in xrange(0, len(grid), 1):
        branch = []
        
        row = grid[rowIndex]
        
        for columnIndex in xrange(0, len(row), 1):
            leftParent, rightParent = None, None
            if rowIndex > 0:
                parentBranch = branches[rowIndex-1]
                
                if columnIndex < len(row) - 1:        
                    rightParent = parentBranch[columnIndex]
                
                if columnIndex > 0:
                    leftParent = parentBranch[columnIndex - 1]
                
            node = tree_node(leftParent, rightParent, row[columnIndex])
            branch.append(node)            
            
        branches.append(branch)
        
    return max(n.value for n in branches[-1])
                
            
        