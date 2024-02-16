#my sol, 1110/1115 passes;
class Solution:
    def flattenBST(self, root):
        if root is None:
            return None
        
        def inorder(node, lst):
            if node is None:
                return
            inorder(node.left, lst)
            lst.append(node.data)
            inorder(node.right, lst)
        
        # Perform inorder traversal to get sorted values
        sorted_values = []
        inorder(root, sorted_values)
        
        # Reconstruct the tree from sorted values
        head = Node(sorted_values[0])
        current = head
        for val in sorted_values[1:]:
            new_node = Node(val)
            current.right = new_node
            current = new_node
        
        return head

#Good solution;

class Solution:
    def flattenBST(self, root):
        if root is None:
            return None

        # Create dummy node to hold the head of the flattened linked list
        dummy = Node(-1)
        prev = dummy
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            # Construct linked list on the fly
            prev.right = current
            prev = current
            # Disconnect left child
            current.left = None
            current = current.right

        # Return head of the flattened linked list (excluding dummy node)
        return dummy.right