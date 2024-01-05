class Solution:
    def singleElement(self, arr, N):
        ones = 0
        twos = 0
         
        for i in range(N):
            twos = twos ^ (ones & arr[i])
            ones = ones ^ arr[i]
            common_bit_mask = ~(ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask
        return ones