from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def revLlist(self, l1: Optional[ListNode]):
        curr,prev=l1,None
        while l1:
            l1=l1.next
            curr.next=prev
            prev=curr
            curr=l1
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:     
        carry=0
        dummyhead=ListNode(0)
        l3=dummyhead
        while l1 or l2 or carry:
            val1,val2 = l1.val if l1 else 0,l2.val if l2 else 0
            carry,rem=divmod(val1+val2+carry,10)
            l3.next=ListNode(rem)            
            l3=l3.next
            l1,l2=l1.next if l1 else None, l2.next if l2 else None
        return dummyhead.next

sol=Solution()

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next=node6

newcurr=sol.addTwoNumbers(node1,node4)
while newcurr:
    print(newcurr.val,end=' ')
    newcurr=newcurr.next