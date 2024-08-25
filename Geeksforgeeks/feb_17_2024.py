class Solution:
    def isMaxHeap(self,arr,n):
        # Check each parent node
        for i in range(n // 2):
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            # Check if left child exists and is greater than parent
            if left_child < n and arr[left_child] > arr[i]:
                return False

            # Check if right child exists and is greater than parent
            if right_child < n and arr[right_child] > arr[i]:
                return False

        return True