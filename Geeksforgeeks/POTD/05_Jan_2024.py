# Your Python code here

#this doesn't pass the test case
class Solution:
    def TotalWays(self, N):
        x, y = 1, 1

        for i in range(2, N + 1):
            w = y
            z = x + y
            x, y = w, z
        
        total_ways = (x + y) * (x + y)
    
        return total_ways % (10**9 + 7)



#this pass the test case
class Solution:
    def TotalWays(self, N):
        x, y = 1, 1

        for i in range(2, N + 1):
            w, z = y, (x + y) % (10**9 + 7)
            x, y = w, z

        total_ways = (x + y) % (10**9 + 7)
        return (total_ways * total_ways) % (10**9 + 7)

# Example usage:
solution_instance = Solution()
result = solution_instance.TotalWays(5)
print(result)

      
