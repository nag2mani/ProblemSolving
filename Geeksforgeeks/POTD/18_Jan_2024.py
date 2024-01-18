#User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        
        #Try to find the range of every sprinkler and then leftmost then rightmost.

        n = len(gallery)
        
        # Create a list of ranges
        ranges = [[0, 0] for _ in range(n)]
        
        for i in range(n):
            if gallery[i] == -1:
                continue
            
            ranges[i][0] = max(0, i - gallery[i])
            ranges[i][1] = min(n, i + gallery[i])
        
        ranges.sort(key=lambda x: x[0])
        
        start, i, res = 0, 0, 0
        curr_max = -1
        
        while start < n:
            while i < n:
                if ranges[i][0] > start:
                    break
                curr_max = max(curr_max, ranges[i][1])
                i += 1
            
            if curr_max < start:
                return -1
            
            res += 1
            start = curr_max + 1
        
        return res
