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
    def getCommon(self, nums1, nums2):
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



# 10 March 2024

#My solution
class Solution:
    def intersection(self, nums1, nums2):
        s = set()
        for i in nums1:
            if i in nums2:
                s.add(i)
        return s

# Other solution using Symmetric Difference between Two Sets
class Solution:
    def intersection(self, nums1, nums2):
        x = set(nums1)
        y = set(nums2)
        return list(y-(y-x))


# 11 March 2024
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        i = [0,0]
        j = [n-1, n-1]
        count = 0
        while(i[0] != n and j[0] != -1):
            if mat1[i[0]][i[1]] +  mat2[j[0]][j[1]] == x:
                count += 1 
                i[1] += 1
                j[1] -= 1
            elif mat1[i[0]][i[1]] + mat2[j[0]][j[1]] > x:
                j[1] -=1 
            elif mat1[i[0]][i[1]] + mat2[j[0]][j[1]] < x:
                i[1] += 1
            if i[1] == n:
                i[0] += 1 
                i[1] = 0
            if j[1] == -1 :
                j[0] -=1 
                j[1] = n-1
        return count

#Optimise solution;
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        s = set(j for i in mat1 for j in i)
        return sum(1 for i in mat2 for j in i if x - j in s)
    


# 12 March 2024
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head):
        #done by other
        node = head
        sum_ , res = 0, {}
        while node:
            sum_ += node.val
            if sum_ == 0:
                head = node.next
                res = {}
            else:
                if res.get(sum_):
                    temp = res[sum_].next
                    current_sum = sum_
                    while temp != node:
                        current_sum += temp.val
                        del res[current_sum]
                        temp = temp.next
                    res[sum_].next = node.next
                else:
                    res[sum_] = node
            node = node.next
        return head



# 13 March 2024
import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        nums = [i for i in range(1, n+1)]
        for i in range(n):
            if sum(nums[:i]) == sum(nums[i-1:]):
                return i
        return -1
    
        # # by other;
        # x = math.sqrt(n*(n+1)/2)
        # converted = int(x)
        # return converted if converted == x else -1



# 14 March 2024






    