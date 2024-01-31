#Only 35/48 test cases passes.----------------------------------------------------

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = []
        for i in range(n-1):
            count = 1
            j = i
            while (temperatures[j+1] <= temperatures[i]) and j+1 < n-1:
                count = count + 1
                j=j+1

            if temperatures[j+1] > temperatures[i]:
                result.append(count)
            else:
                result.append(0)
        result.append(0)
        return result
    


#Other solution-----------------------------------------------------------------------
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
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




#Perfect solution.-------------------------------------------------------------------

def dailyTemperatures(temperatures: List[int]) -> List[int]:

    output = [0]*len(temperatures)
    stack = []
    for cindex,ctemp  in enumerate(temperatures):
        while stack and stack[-1][0] < ctemp:#cause it is monotonically decreasing
                t,i = stack.pop()
                output[i] = cindex-i
        stack.append((ctemp, cindex))
    return output
with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"[{','.join([str(x) for x in dailyTemperatures(case)])}]\n")
exit()




