
class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] stores the length of the largest divisible subset ending at index i
        prev = [-1] * n  # prev[i] stores the index of the previous element in the largest divisible subset

        max_len = 1
        max_idx = 0

        # Compute dp array
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_idx = i

        # Reconstruct the largest divisible subset
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev[max_idx]

        return result[::-1]
