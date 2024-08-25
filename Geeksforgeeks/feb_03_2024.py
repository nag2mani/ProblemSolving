'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        x = 0
        i = 0
        while head:
            x = (x*2 + head.data)%MOD
            head = head.next
            i+=1
        return x
