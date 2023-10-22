from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #1->2->3->4->5->6
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for _ in range(left-1):
            pre=pre.next
        
        curr=pre.next
        for _ in range(right-left):
            next=curr.next
            curr.next=next.next
            next.next=pre.next
            pre.next=curr
        return dummy.next


    def reverseBetweenOnValues(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ptr=head
        while ptr.next and ptr.next.val!=left:
            ptr=ptr.next
        
        lefthalfend=ptr        
        lptr=ptr.next
        if not lptr:
            return head

        lptrEnd=lptr
        lefthalfend.next=None

        prev=None
        curr=lptr
        while curr.val!=right:
            next_temp = curr.next
            curr.next=prev
            prev=curr            
            curr=next_temp
        
        righthalfend=curr.next
        curr.next=prev
        lefthalfend.next=curr
        lptrEnd.next=righthalfend

        return head


        

sol=Solution()

# Creating a linked list 1->2->3->4->5->6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
#head.next.next.next.next.next = ListNode(6)
newhead=sol.reverseBetween(head,2,4)
while newhead:
    print(f'{newhead.val}', end=' ')
    newhead=newhead.next

# def reverse(ptr):    
#     prev=None
#     curr=ptr
#     while curr:
#         next_temp = curr.next
#         curr.next=prev
#         prev=curr            
#         curr=next_temp
#     return prev

