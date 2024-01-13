class Solution():
    def maxSumWithK(self, a, n, k):
        maxSum = [0] * n
        
        # Use Kadane's algorithm to calculate the maximum sum subarray ending at each index
        maxSum[0] = a[0]
        for i in range(1, n):
            maxSum[i] = max(a[i], maxSum[i - 1] + a[i])
        
        # Calculate the sum of the first k elements
        current_sum = sum(a[:k])
        ans = current_sum
        
        # Iterate through the array starting from the (k+1)-th element
        for i in range(k, n):
            # Update the current sum by adding the current element and subtracting the first element of the previous subarray
            current_sum = current_sum + a[i] - a[i - k]
            
            # Update the answer with the maximum of the current sum and the maximum sum subarray ending at the (i-k)-th index
            ans = max(ans, current_sum, current_sum + maxSum[i - k])
        
        return ans