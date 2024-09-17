class Solution:
    def romanToInt1(self, s: str) -> int:
        sin = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        dob = {'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9,'IV':4}
        result = 0
        n = len(s)
        i = 0
        while (i < n):
            if i < n and s[i:i+2] in dob:
                result = result + dob[s[i:i+2]]
                i = i+2
                continue
            if i < n and s[i] in sin:
                result = result + sin[s[i]]
                i = i+1
                continue
        return result

