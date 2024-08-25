
# Taking much time

class Solution:
    def recamanSequence(self, n):
        prev = 0
        ans = [0]
        for i in range(1, n):
            curr = prev - i
            if curr < 0 or curr in ans:
                curr = prev + i
            ans.append(curr)
            prev = curr
        return ans




#Optimised solution

class Solution:
    def recamanSequence(self, n):
        prev = 0
        ans = [0]
        seen = set([0])  # Use a set for faster lookup
        for i in range(1, n):
            curr = prev - i
            if curr < 0 or curr in seen:  # Check membership in the set
                curr = prev + i
            ans.append(curr)
            seen.add(curr)  # Add curr to the set
            prev = curr
        return ans
    
    