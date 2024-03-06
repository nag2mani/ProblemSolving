# 01 March 2024
class Solution:
    def maximumOddBinaryNumber(self, s):
        n = len(s)
        no_of_one = s.count('1')
        if no_of_one == 1:
            return (n-1) * '0' + '1'
        else:
            return (no_of_one-1) * '1' + (n - no_of_one) * '0' + '1'



# 02 March 2024
class Solution:
    def sortedSquares(self, nums):
        squares = [num * num for num in nums]
        squares.sort()
        return squares


# 03 March 2024
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head, n):
        nd = ListNode(0)
        nd.next = head
        first = nd
        second = nd

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return nd.next


# 04 March 2024


# 05 March 2024


# 06 March 2024

class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        return False