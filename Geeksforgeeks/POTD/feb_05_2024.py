
# class Node: 
#     # Constructor to initialize the node object 
#     def __init__(self, data): 
#         self.data = data 
#         self.next = None


class Solution:
    def sortedInsert(self, head, data):
        
        new_node = Node(data)
        
        # If the linked list is empty, insert the new node and return it as the head.
        if not head:
            new_node.next = new_node
            return new_node

        # If the data to be inserted is smaller than or equal to the head, insert at the beginning.
        if head.data >= data:
            curr = head
            while curr.next != head:
                curr = curr.next
            new_node.next, curr.next = head, new_node
            return new_node
        else:
            # Traverse the linked list to find the correct position for insertion.
            curr = head
            while True:
                # Insert the new node when the next node has greater or equal data, or we reach the end.
                if curr.next.data >= data or curr.next == head:
                    new_node.next, curr.next = curr.next, new_node
                    return head
                curr = curr.next