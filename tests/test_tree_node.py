'''
Tree node tests
'''
import unittest
from util.tree_node import tree_node


class Test(unittest.TestCase):
    
    def test_tree_nodes(self):
        t1 = tree_node(None, None, 0)
        self.assertEquals(t1.value, 0)
        
        t2 = tree_node(None, None, 5)
        self.assertEquals(t2.value, 5)
        
        t3 = tree_node(t1, None, 10)
        self.assertEquals(t3.value, 10)
        
        t3 = tree_node(None, t2, 10)
        self.assertEquals(t3.value, 15)
        
        t3 = tree_node(t1, t2, 10)
        self.assertEquals(t3.value, 15)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()