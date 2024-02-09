'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        #base case
        if root is None or (root.left is None and root.right is None):
            return 1
        
        left = 0 if root.left is None else root.left.data
        right = 0 if root.right is None else root.right.data
        
        if root.data == left + right:
            # Recursively check left and right subtrees
            return (self.isSumProperty(root.left) and self.isSumProperty(root.right))
        else:
            return 0