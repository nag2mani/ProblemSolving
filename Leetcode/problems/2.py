#My solution;
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2:
            # Get the values of the current nodes or 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the current digits and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update the carry
            
            # Create a new node with the digit at the current place value
            current.next = ListNode(total % 10)
            current = current.next  # Move to the next node
            
            # Move to the next nodes in both lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Check if there's any remaining carry
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy_head.next




#Good solution;

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur=dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit 
            val = v1 +v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            #update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next