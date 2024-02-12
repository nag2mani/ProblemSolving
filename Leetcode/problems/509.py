#1
class Solution1:
    def fib1(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib1(n-1) + self.fib1(n-2)




#2
class Solution2:
    def fib2(self, n: int) -> int:
        if n == 0:
            return(0)
        if n == 1:
            return(1)

        # create empty dp array
        dp = [0] * (n + 1)

        # find patterns
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp




#3
class Solution3:
    def fib3(self, n: int) -> int:

        a = 0
        b = 1
        if n <= 1:
            return n
        for _ in range(2, n+1):
            a, b = b, a + b, 
        return b

o = Solution1()
print(o.fib1(40))