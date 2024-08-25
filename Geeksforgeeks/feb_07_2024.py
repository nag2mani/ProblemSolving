'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self,root,a,b):
        if a==b:
            return 0
        self.ans=0
        def lca(node):
            if node==None:
                return 0
                
            lh=lca(node.left)
            rh=lca(node.right)
            
            if node.data==a or node.data==b:
                if lh>0:
                    self.ans=lh
                elif rh>0:
                    self.ans=rh
                else:
                    return 1
                

            if lh>0 and rh>0:
                self.ans=lh+rh
            elif rh!=0:
                return rh+1
            elif lh!=0:
                return lh+1
                
            return 0
            
        lca(root)
        return self.ans