
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Length of the input array
        n = len(arr)
        
        # Memoization dictionary
        memo = {}

        # Recursive function to find the maximum sum after partitioning
        def dfs(i):
            # Base case: end of the array
            if i == n:
                return 0

            # Check if result for index i is memoized
            if i in memo:
                return memo[i]

            curMax = curSum = 0

            # Iterate over the next k elements or until the end of the array
            for j in range(i, min(i + k, n)):
                curMax = max(curMax, arr[j])
                cur = curMax * (j - i + 1) + dfs(j + 1)
                curSum = max(curSum, cur)

            # Memoize result for index i
            memo[i] = curSum
            return curSum

        return dfs(0)