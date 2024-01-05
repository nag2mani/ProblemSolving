class Solution:
    def smallestSubstring(self, S):
        res = 999999
     
        # To check 0, 1 and 2
        zero = 0
        one = 0
        two = 0
     
        # To store indexes of 0, 1 and 2
        zeroindex = 0
        oneindex = 0
        twoindex = 0
        for i in range(len(S)):
            if (S[i] == '0'):
                zero = 1
                zeroindex = i
     
            elif (S[i] == '1'):
                one = 1
                oneindex = i
     
            elif (S[i] == '2'):
                two = 1
                twoindex = i
     
            # Calculating length
            if (zero and one and two):
                res = min(res,
                          max([zeroindex, oneindex, twoindex])
                          - min([zeroindex, oneindex, twoindex]))
     
        # In case if there is no substring that contains 0,1 and 2
        if (res == 999999):
            return -1
        return res + 1