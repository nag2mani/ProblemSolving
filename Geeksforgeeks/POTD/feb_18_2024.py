# My sol
class Solution:
    def sumOfLeafNodes(self, root):
        def dfs(node):
            nonlocal sol
            if not node:
                return
            if not node.left and not node.right:
                sol = sol + node.data
            
            dfs(node.left)
            dfs(node.right)
            
        sol = 0
        dfs(root)
        return sol