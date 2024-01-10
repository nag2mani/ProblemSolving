#User function Template for python3
class Solution:
    def longSubarrWthSumDivByK(self, arr, n, K):
        # Create a dictionary to store the remainder of cumulative sum
        # and its corresponding index
        remainder_dict = {0: -1}
        
        # Initialize variables to store cumulative sum and max length
        cum_sum = 0
        max_length = 0
        
        for i in range(n):
            cum_sum += arr[i]
            
            # Calculate the remainder when dividing cumulative sum by K
            remainder = cum_sum % K
            
            # If remainder is negative, convert it to positive
            if remainder < 0:
                remainder += K
            
            # If the remainder is already in the dictionary, update max length
            if remainder in remainder_dict:
                max_length = max(max_length, i - remainder_dict[remainder])
            
            # If remainder is not in the dictionary, add it with the current index
            if remainder not in remainder_dict:
                remainder_dict[remainder] = i
        
        return max_length