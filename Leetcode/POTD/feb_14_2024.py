#my code

class Solution:
    def rearrangeArray(self, nums):
        result = []
        positive_stack = []
        negative_stack = []
        for i in nums:
            if i>0:
                positive_stack.append(i)
            else:
                negative_stack.append(i)
        for j, k in zip(positive_stack, negative_stack):
            result.append(j)
            result.append(k)
        return result




#good way
class Solution:
    def rearrangeArray(self, nums):
        
        pos, neg = [], []

        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        nums[0 : len(pos) * 2 : 2] = pos
        nums[1 : len(neg) * 2 : 2] = neg

        return nums