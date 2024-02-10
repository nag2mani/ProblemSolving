class Solution:
    def numberOfPath (self, n, k, arr):
        dp = {}
        def dfs(r,c,k):
            if max(r,c) >= n or arr[r][c] > k:
                return 0
            if (r,c,k) in dp:
                return dp[(r,c,k)]
            if r == c == n - 1:
               return 1 if arr[r][c] == k else 0
            right = dfs(r,c+1,k - arr[r][c])
            down = dfs(r+1,c,k - arr[r][c])
            result = dp[(r,c,k)] = right + down
            return result
        return dfs(0,0,k)