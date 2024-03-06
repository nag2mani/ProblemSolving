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
class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        n = len(tokens)
        score = 0
        max_score = 0
        left = 0
        right = n - 1
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
                
        return max_score


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