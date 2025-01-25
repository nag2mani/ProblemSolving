class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result =0
        n=len(s)
        for i in range(n):
            if i < n - 1 and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                result -= roman_numerals[s[i]]
            else:
                result += roman_numerals[s[i]]
        
        return result