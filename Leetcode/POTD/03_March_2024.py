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
class Solution:
    def minimumLength(self, s):
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left and s[right] == char:
                right -= 1
        
        return right - left + 1  



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
    


# 07 March 2024
class Solution:
    def middleNode(self, head):
        fast, slow = head , head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow



# 08 March 2024
from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums):
        # It will give dict with the frequency of every unique term.
        freq = Counter(nums)
        maxx = max([i for i in freq.values()])
        result = 0
        for j in freq:
            if freq[j] == maxx:
                result += maxx
        return result




# 09 March 2024
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        num1 = nums1
        num2 = nums2
        while i < len(num1) and j < len(num2):
            if num1[i] > num2[j]:
                j = j + 1
            elif num1[i] < num2[j]:
                i = i + 1
            else:
                return num1[i]
        return -1
