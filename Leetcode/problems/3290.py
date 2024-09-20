from typing import List

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[-float('inf')] * 4 for _ in range(n)]
        print(dp)
        dp[0][0] = a[0] * b[0]
        print(dp)

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], a[0] * b[i])
            print(dp)
            for j in range(1, 4):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[j] * b[i])
                print(dp)

        return dp[n-1][3]

s = Solution()
a= [3,2,5,6]
b= [2,-6,4,-5,-3,2,-7]
print(s.maxScore(a,b))
