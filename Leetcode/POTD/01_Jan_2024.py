# 01 January 2024
class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            if not stack:
                stack.append(i)
                ans[i] = 0
            else:
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()

                if not stack:
                    ans[i] = 0
                else:
                    ans[i] = stack[-1] - i

                stack.append(i)

        return ans
    


# 02 January 2024
# 03 January 2024
# 04 January 2024
# 05 January 2024
# 06 January 2024
# 07 January 2024
# 08 January 2024
# 09 January 2024
# 10 January 2024
# 11 January 2024
# 12 January 2024
# 13 January 2024
# 14 January 2024
# 15 January 2024
# 16 January 2024
# 17 January 2024
# 18 January 2024
# 19 January 2024
# 20 January 2024
# 21 January 2024
# 22 January 2024
# 23 January 2024
# 24 January 2024
# 25 January 2024
# 26 January 2024
# 27 January 2024
# 28 January 2024
# 29 January 2024
# 30 January 2024
# 31 January 2024




