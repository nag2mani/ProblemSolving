
class Solution:
    def subLinkedList(self, l1, l2):
        a=""
        b=""
        while l1:
            a=a+str(l1.data)
            l1=l1.next
        while l2:
            b=b+str(l2.data)
            l2=l2.next
        res1=int(a)
        res2=int(b)
        ans=abs(res1-res2)
        node=Node(ans)
        return node
