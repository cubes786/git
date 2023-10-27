from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before=before_head=ListNode(0)
        after=after_head=ListNode(0)

        while head:
            if head.val<x:
                before.next=head
                before=before.next
            else:
                after.next=head
                after=after.next
            head=head.next
        
        before.next=after_head.next
        after.next=None
        return before_head.next
    
    def printTraversell(self, head):
        while head:
            print(f'{head.val}', end=' ')
            head=head.next
        print('\n')
        
sol=Solution()
# Create a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
sol.printTraversell(head)
sol.printTraversell(sol.partition(head,3))