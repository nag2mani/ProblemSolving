# 162. Find Peak Element


#In O(n) time
def findPeakElement(nums) -> int:
    if len(nums)==1:
        return 0
    if len(nums)==2:
        if nums[0] > nums[1]:
            return 0
        else:
            return 1
    else:
        for i in range(1, len(nums)-1):
            if nums[i-1] > nums[i]:
                return 0
            else:
                if ((nums[i-1] < nums[i]) and (nums[i+1] < nums[i])):
                    return i
        return len(nums)-1


#In log(n) time
def findPeakElement(nums) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    while(low < high):
        mid = low + (high - low) // 2
        if nums[mid] < nums[mid + 1]:
            # Although it is not sorted but we have assumed.
            low = mid + 1
        else:
            high = mid
    return low
