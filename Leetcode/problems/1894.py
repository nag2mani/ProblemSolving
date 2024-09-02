# 1894. Find the Student that Will Replace the Chalk

class Solution:
    def chalkReplacer(self, chalk, k):
        # # Time Limit Exceeded
        n = len(chalk)
        # i = 0
        # while(i>=0):
        #     for j in range(n):
        #         k = k - chalk[j]
        #         if k < 0:
        #             return j
        #     i = i+1


        s = sum(chalk)
        r = k//s
        k = k - r*s
        for j in range(n):
            k = k - chalk[j]
            if k < 0:
                return j
    