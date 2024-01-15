class Solution:
    def numberSequence(self, m, n):
        result = []
        sub_result = [1]
        
        for i in range(n):
            for j in range(1,m+1):
                if ((j >= 2 * sub_result[i]) and (j > 0) and (j < m)):
                    sub_result.append(j)
                    break
            result.append(sub_result)
        
        return len(result)

