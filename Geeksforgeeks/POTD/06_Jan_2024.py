
from typing import List


class Solution:

    def sumOfPowers(self, a: int, b: int) -> int:
        def prime_factors_sum(num, memo = {}):
            if num in memo:
                return memo[num]
        
            result = 0
        
            # Handle the case of 2 separately to simplify the loop
            temp = num
            while temp % 2 == 0:
                result += 1
                temp //= 2
        
            # Iterate only for odd numbers starting from 3
            for i in range(3, int(temp**0.5) + 1, 2):
                while temp % i == 0:
                    result += 1
                    temp //= i
        
            # If temp is still greater than 1, it's a prime factor
            if temp > 1:
                result += 1
        
            memo[num] = result
            return result

        total_points = 0
        for num in range(a, b + 1):
            total_points += prime_factors_sum(num)

        return total_points