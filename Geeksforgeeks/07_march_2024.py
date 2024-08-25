class Solution:
    def longestSubstring(self, s , n):
        res, maxi = "", -1
        for i in range(n):
            x = ""
            for j in range(i,n):
                x += s[j]
                if x in s[j+1:]:
                    if maxi<len(x):
                        maxi = len(x)
                        res = x
                else:
                    break
        return res if res !="" else "-1"