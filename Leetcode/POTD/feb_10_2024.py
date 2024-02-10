class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][i] = True
            count += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count




##Best solution

class Solution:
    def countSubstrings(self, S: str) -> int:
        ans, n, i = 0, len(S), 0
        while (i < n):
            j, k = i - 1, i
            while k < n - 1 and S[k] == S[k+1]: k += 1                
            ans += (k - j) * (k - j + 1) // 2
            i, k = k + 1, k + 1
            while ~j and k < n and S[k] == S[j]:
                j, k, ans = j - 1, k + 1, ans + 1
        return ans