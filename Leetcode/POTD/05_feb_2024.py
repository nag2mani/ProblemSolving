class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.rindex(s[i]) == s.index(s[i]):
                return i
        return -1


#Mind blowing.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.index(char) for char in set(s) if s.count(char) == 1] or [-1])