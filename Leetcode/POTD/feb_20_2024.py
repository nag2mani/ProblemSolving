#My solution.

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sl = sum(nums)
        s = (n * (n+1)) // 2
        return s - sl