'''
Node object to represent a tree structure.

Each node can have two children.

The value of a given node is it's value and the max sum of it's parent's value
'''

class tree_node:
    value = 0

    def __init__(self, leftParent, rightParent, n):
        if leftParent == None:
            leftValue = 0
        else:
            leftValue = leftParent.value

        if rightParent == None:
            rightValue = 0
        else:
            rightValue = rightParent.value
        
        self.value = n + max(leftValue, rightValue)
        