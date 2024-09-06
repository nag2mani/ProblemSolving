# 2028. Find Missing Observations

from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

#solution-1(Myself)

        #Greedy approach first allot min to all then distribute.
        m = len(rolls)
        s1 = sum(rolls)
        s2 = mean * (m+n) - sum(rolls)
        if ((s2 > 6 * n) or (s2 < 1 * n)):
            return []
        else:
            result = [1]*n
            s2 = s2 - n
            while (s2 > 0) :
                for i in range(n):
                    if (s2 > 0) :
                        result[i] = result[i] + 1
                        s2 = s2 - 1
                    else:
                        return result
        return result
    
#solution-2(chatgpt)

        # m = len(rolls)
        # total_sum = mean * (n + m)
        # known_sum = sum(rolls)
        # missing_sum = total_sum - known_sum
        # if missing_sum < n or missing_sum > 6 * n:
        #     return []
        # result = [1] * n
        # missing_sum -= n
        # i = 0
        # while missing_sum > 0:
        #     add = min(5, missing_sum)
        #     result[i] += add
        #     missing_sum -= add
        #     i += 1
        # return result

#solution-3(top on leetcode)

        # m = len(rolls)
        # totalSum = mean * (m + n)
        # rollsSum = sum(rolls)
        # missingSum = totalSum - rollsSum
        # if missingSum < n or missingSum > 6 * n:
        #     return []
        # quotient, remainder = divmod(missingSum, n)
        # return [quotient + (1 if i < remainder else 0) for i in range(n)]




