#Only 35/48 test cases passes.

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
    


#Other solution
