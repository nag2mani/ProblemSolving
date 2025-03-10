#My Solution;

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = 0
        alt = 1
        for i in range(n + k - 2):
            alt = (1 if colors[i % n] == colors[(i - 1) % n] else alt + 1)
            if alt >= k:
                ans += 1
        return ans
    
# My better sol;
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count= 0
        l = 0
        limit=n+k-1

        while(l<n):
            r=l+1
            while(r<limit and colors[(r-1)%n] != colors[r%n]):
                r+=1
            if (r-l)>=k:
                count += (r-l) - k + 1
            l=r
        return count
#Good SOl;

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        l = []
        n = len(colors)
        for i in range(n - 1):
            if colors[i] == colors[i + 1]:
                l.append(i)

        if colors[n - 1] == colors[0]:
            l.append(n - 1)
        if len(l) == 0:
            return n

        l.append(l[0] + n)
        res = 0
        for i in range(len(l) - 1):
            res += max(0, l[i + 1] - l[i] - k + 1)

        return res