# 2022. Convert 1D Array Into 2D Array

class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m*n:
            return []
        result = []
        for i in range(0,len(original), n):
            result.append(original[i:i+n])
        return result

        # if len(original) != m * n:
        #     return []
        # result = []
        # for i in range(m):
        #     row = original[i * n:(i + 1) * n]
        #     result.append(row)
        # return result