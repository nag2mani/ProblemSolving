#my solution

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPal(w):
            s = []
            for i in range(len(w)//2):
                s.append(w[i])
            if len(w) % 2 != 0:
                for j in range(len(w)//2 +1 , len(w)):
                    if w[j] == s[-1]:
                        s.pop()
                        continue
                    else:
                        return False
            if len(w) % 2 == 0:
                for j in range(len(w)//2 , len(w)):
                    if w[j] == s[-1]:
                        s.pop()
                        continue
                    else:
                        return False
            return True

        for k in words:
            if isPal(k) == True:
                return k
        return ""
    


#good solution
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        return ""