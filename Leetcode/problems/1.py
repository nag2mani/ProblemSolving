#my solution;

class Solution:
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i] + nums[j]) == target:
                    return (i,j)



#Good solution;
                
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            # check if the compliment of our current number is in the map
            s = target - nums[i]
            # if it is, return the index (stored number in the hash) for that complimnetary number
            if s in seen:
                return [seen[s], i]
            # store the current number on its compliment
            seen[nums[i]] = i