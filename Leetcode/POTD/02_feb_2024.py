class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                num = int(s[i:j+1])

                if num > high: break
                if low <= num:
                    res.append(num)
        
        return sorted(res)


# more optimised

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 10):
            temp = i
            for j in range(i + 1, 10):
                temp = 10 * temp + j
                if temp in range(low, high + 1):
                    res.append(temp)
        res.sort()
        return res