class Solution:

    def removeKdigits(self, S, K):
        stack = []

        for digit in S:
            while K > 0 and stack and stack[-1] > digit:
                stack.pop()
                K -= 1
            stack.append(digit)

        # If K is still greater than 0, remove remaining digits from the end of the stack
        while K > 0:
            stack.pop()
            K -= 1

        # Join the elements of the stack to form the result
        result = ''.join(stack).lstrip('0')

        # If the result is empty, return '0'
        return result if result else '0'
    

