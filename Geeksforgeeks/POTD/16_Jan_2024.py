class Solution:
    def numberSequence(self, m, n):
        if m < n:
            return 0
        if n == 0:
            return 1
        return self.numberSequence(m - 1, n) + self.numberSequence((m >> 1), n - 1)

s = Solution()
k = s.numberSequence(10, 4)
print(k)
k = s.numberSequence(5, 2)
print(k)


