'''
Tree node path tests
'''
import unittest
from tree_node_path import get_max_tree_node_path


class Test(unittest.TestCase):


    def testName(self):
        path = get_max_tree_node_path([[5]])
        self.assertEqual(path, 5)
        
        path = get_max_tree_node_path([[5], [6, 7]])
        self.assertEqual(path, 12)
        
        path = get_max_tree_node_path([[5], [6, 7], [10, 9, 8]])
        self.assertEqual(path, 21)
        
        path = get_max_tree_node_path([[5], [6, 7], [10, 9, 8], [11, 12, 13, 14]])
        self.assertEqual(path, 34)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()