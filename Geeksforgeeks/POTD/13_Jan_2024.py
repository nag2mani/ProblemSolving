'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def insertionSort(self, head):
        # Base case: If the list is empty or has only one element, it is already sorted
        if head is None or head.next is None:
            return head

        # Initialize a sorted list with the first node
        sorted_head = head
        head = head.next
        sorted_head.next = None

        while head:
            current = head
            head = head.next

            # If the current node's data is smaller than the sorted list's head, update the head
            if current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                # Traverse the sorted list to find the correct position to insert the current node
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

        return sorted_head
