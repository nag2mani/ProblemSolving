#My solution;
class Solution:
    def largestPerimeter(self, nums):
        n = len(nums)
        nums.sort()
        for i in range(n-1, 1, -1):
            if nums[i] >= sum(nums[:i]):
                continue
            else:
                return sum(nums[:i+1])

        return -1



#Optimised Solution;
class Solution:
    def largestPerimeter(self, nums):
        while(True):
            if len(nums) != 0:
                m = max(nums)
            else:
                break
            nums.remove(m)
            if sum(nums) > m:
                return sum(nums) + m
        return -1