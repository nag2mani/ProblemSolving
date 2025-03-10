#My solution;

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        colors = colors + colors[:2]
        result=0
        for i in range(n):
            alt = True
            for j in range(i, i+2):
                if colors[j] == colors[j+1]:
                    alt= False
                    break
            if alt:
                result += 1
        return result
    

# Good Solution;

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        colors += colors
        res = 0

        for i in range(n):
            if colors[i] == colors[i+2] and colors[i] != colors[i+1]:
                res +=1
        
        return res