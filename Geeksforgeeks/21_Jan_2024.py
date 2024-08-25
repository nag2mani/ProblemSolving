from typing import List

class Solution:
    def vertexCover(self, n: int, edges: List[List[int]]) -> int:
        def solve(edges):
            if len(edges)==0:
                return 0
            ed0=[]
            ed1=[]
            for i in edges:
                if not(i[0]==edges[0][0] or i[1]==edges[0][0]):
                    ed0.append(i)
                if not(i[0]==edges[0][1] or i[1]==edges[0][1]):
                    ed1.append(i)
            ans0=1+solve(ed0)
            ans1=1+solve(ed1)
            return min(ans0,ans1)
        return solve(edges)