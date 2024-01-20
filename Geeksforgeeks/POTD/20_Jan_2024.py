'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def distributeCandy(self, root):
        moves = [0]  # Initialize the moves count as a list to allow modification within recursive calls
        self.distribute(root, moves)
        return moves[0]

    def distribute(self, node, moves):
        if not node:
            return 0
        
        # Recursively calculate moves for left and right subtrees
        moves_left = self.distribute(node.left, moves)
        moves_right = self.distribute(node.right, moves)
        
        # Update moves for the current subtree
        moves[0] += abs(moves_left) + abs(moves_right)
        
        # Calculate the net candies at the current node
        net_candies = node.data + moves_left + moves_right - 1
        
        return net_candies