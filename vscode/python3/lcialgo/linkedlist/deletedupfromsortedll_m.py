from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr,prev=head,dummy
        while curr:
            has_duplicate=False
            while curr.next and curr.val==curr.next.val:
                has_duplicate=True
                curr=curr.next
            if has_duplicate:
                prev.next=curr.next
            else:
                prev=curr

            curr=curr.next
        return dummy.next
    
    def printTraversell(self, head):
        while head:
            print(f'{head.val}', end=' ')
            head=head.next
        print('\n')

sol=Solution()
h4=ListNode(4,None)
h3=ListNode(3,None)
h33=ListNode(3,None)
h2=ListNode(2,None)
h22=ListNode(2,None)
h222=ListNode(2,None)
h1=ListNode(1,None)
h1.next=h2
h2.next=h22
h22.next=h222
h222.next=h3
h3.next=h33
h33.next=h4
sol.printTraversell(h1)
sol.printTraversell(sol.deleteDuplicates(h1))