#amazing solution

class Solution:
    def isPossible(self, paths):
        for i in paths:
            if i.count(1) % 2:
                return 0
        return 1