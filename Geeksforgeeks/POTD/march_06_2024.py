# My slution

class Solution:
    def search(self, pattern, text):
        result = []
        t = len(pattern)
        i = 0
        while (i < len(text)-t + 1):
            if text[i:i+t] == pattern:
                result.append(i+1)
                i = i+1
            else:
                i = i+1
            
        return result


# Other Solution using Rabin Karp Algorithm.
class Solution:
    def search(self, pattern, text):