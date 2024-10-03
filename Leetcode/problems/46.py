#Python Inbuilt Function.
import itertools
nums=[3,4,5,6]
def permute(nums):
    return list(itertools.permutations(nums))
# print("Method 1 : ",permute(nums))


#Using Heap Method
def heap_permute(n, nums, result):
    if n == 1:
        result.append(nums[:])  # Append a copy of the current permutation
    else:
        for i in range(n):
            heap_permute(n - 1, nums, result)
            if n % 2 == 0:  # If n is even, swap i and n-1
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
            else:  # If n is odd, swap 0 and n-1
                nums[0], nums[n - 1] = nums[n - 1], nums[0]
result = []
heap_permute(len(nums), nums, result)
print("Method 2 : ", result)
print("Length : ", len(result))


#Using Backtrack(this takes more time than method 2)
def backtrack(path, nums, result):
    if len(path) == len(nums):
        result.append(path[:]) # Append a copy of the current path
        return

    for num in nums:
        if num not in path:
            path.append(num)        # Choose the element
            backtrack(path, nums, result)  # Explore further
            path.pop()              # Backtrack by removing the last element
result = []
backtrack([], nums, result)
# print("Method 3 : ", result)
# print("Length : ", len(result))


