# 01 March 2024


# 02 March 2024


# 03 March 2024


# 04 March 2024


# 05 March 2024


# 06 March 2024

class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        return False