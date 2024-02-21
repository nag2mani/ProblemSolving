#solution is given by someone in comments


class Solution:
    def countWays(self, n, s):
    # Initialize DP tables for true and false
        # code here
        from functools import lru_cache
        
        @lru_cache(None)
        
        def count(i, j, result=True):
            if i == j:
                if result:
                    return int(s[i:j+1] == 'T')
                else:
                    return int(s[i:j+1] == 'F')
            r = 0
            
            for k in range(i+1, j, 2):
                if s[k] == '&':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                        r += count(i, k-1, True) * count(k+1, j, False)
                        
                        
                if s[k] == '|':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                        r += count(i, k-1, True) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                        
                        
                if s[k] == '^':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                        r += count(i, k-1, True) * count(k+1, j, True)
                        
            return r % 1003
            
        return count(0, n-1)