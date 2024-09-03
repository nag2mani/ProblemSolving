# 1945. Sum of Digits of String After Convert.

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        fist_str_val = ""
        for char in s:
            # val = ord(char) - ord('a') + 1 #don't know earlier.
            val = ord(char) - 96
            fist_str_val = fist_str_val + str(val)
        for i in range(k):
            sum = 0
            for d in fist_str_val:
                sum = sum + int(d)
            fist_str_val = str(sum)
        return sum

