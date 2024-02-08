# Using queue
from collections import deque

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        if not root:
            return True
        
        leaf_levels = set()  # Set to store levels of leaf nodes
        queue = [root]  # Initialize queue for level-order traversal
        level = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                
                if not node.left and not node.right:
                    # Leaf node encountered, add its level to set
                    leaf_levels.add(level)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        # If there's only one level in the set, all leaf nodes are at the same level
        return len(leaf_levels) == 1
    





# using dequeue

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        if not root:
            return True
        
        leaf_levels = set()  # Set to store levels of leaf nodes
        queue = deque([(root, 0)])  # Initialize queue for level-order traversal
        
        while queue:
            node, level = queue.popleft()
            
            if not node.left and not node.right:
                # Leaf node encountered, add its level to set
                leaf_levels.add(level)
            
            if node.left:
                queue.append((node.left, level + 1))
                
            if node.right:
                queue.append((node.right, level + 1))
        
        # If there's only one level in the set, all leaf nodes are at the same level
        return len(leaf_levels) == 1