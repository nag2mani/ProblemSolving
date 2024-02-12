#my solution
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


# other solution
class Solution:
    def majorityElement(self, nums):
        counter = 1
        value = nums[0]
        
        for i in range(len(nums)):
            if i == 0:
                continue
            
            if counter == 0:
                value = nums[i]
            
            if nums[i] == value:
                counter += 1
            else:
                counter -= 1
        
        return value