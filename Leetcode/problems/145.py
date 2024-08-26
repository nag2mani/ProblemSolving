# # Using append
# list1 = [1, 2, 3]
# list1.append([4, 5])
# print(list1)  # Output: [1, 2, 3, [4, 5]]

# # Using extend (You can extend list or tuple)
# list2 = [1, 2, 3]
# list2.extend([4, 5])
# print(list2)  # Output: [1, 2, 3, 4, 5]


from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Solution1
class Solution1:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return result
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result

## Solution2
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return ans[::-1]


## Solution3
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result += [root.val]
        return result

