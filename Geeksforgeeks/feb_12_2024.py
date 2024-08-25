#My code , Passed

class Solution:
    def sequence(self, n):
        k = 1
        sum = 0
        for i in range(1, n+1):
            result = 1
            j = 1
            while (j <= i):
                result = result * k
                k = k + 1
                j = j + 1
            sum = sum + result
        return sum % ((10 ** 9) + 7)


# other good code(take half time than me)

class Solution:
    mod=10**9+7
    def sequence(self, n):
        k=1
        total=0
        for i in range(1,n+1):
            curr=1
            for j in range(i):
                curr=(curr*k)%self.mod
                k+=1
            total=(total+curr)%self.mod
        return total