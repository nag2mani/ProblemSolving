#Take much time;
class Solution:
    def wordBreak(self, n, s, dictionary):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dictionary:
                    dp[i] = True
                    break

        return 1 if dp[len(s)] else 0


#optimise sol;
class Solution:
    def wordBreak(self, n, s, dictionary):
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            for word in dictionary:
                if i + len(word) <= n and s[i:i + len(word)] == word and dp[i + len(word)] != 0:
                    dp[i] = 1

        return dp[0]