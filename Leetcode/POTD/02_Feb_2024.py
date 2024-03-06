# 01 Febraury 2024
import numpy as np
class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if i + 2 < len(nums):
                if nums[i + 2] - nums[i] > k:
                    return []
                res.append([nums[i], nums[i + 1], nums[i + 2]])

        return res



# 02 February 2024
class Solution:
    def sequentialDigits(self, low, high):
        res = []
        for i in range(1, 10):
            temp = i
            for j in range(i + 1, 10):
                temp = 10 * temp + j
                if temp in range(low, high + 1):
                    res.append(temp)
        res.sort()
        return res



# 03 February 2024




# 04 February 2024




# 05 February 2024



# 06 February 2024




# 07 February 2024





# 08 February 2024
# 09 February 2024
# 10 February 2024
# 11 February 2024
# 12 February 2024
# 13 February 2024
# 14 February 2024
# 15 February 2024
# 16 February 2024
# 17 February 2024
# 18 February 2024
# 19 February 2024
# 20 February 2024
# 21 February 2024
# 22 February 2024
# 23 February 2024
# 24 February 2024
# 25 February 2024
# 26 February 2024
# 27 February 2024
# 28 February 2024
# 29 February 2024