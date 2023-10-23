from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        
        n,tail=1,head
        while tail.next:
            tail=tail.next
            n+=1
        
        nmodk=k%n
        if nmodk==0:
            return head
        
        first=second=head
        for i in range(nmodk+1):
            first=first.next
        while first:
            first=first.next
            second=second.next

        newhead=second.next
        second.next=None
        tail.next=head
        
        return newhead
    
    def rotateRightBylooping(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head

        # Find the length of the list and the tail node
        tail, length = head, 1
        while tail.next:
            tail = tail.next
            length += 1

        # Connect the tail to the head to form a circular list
        tail.next = head

        # Find the new tail, which is (length - k % length) nodes ahead of the head
        new_tail = head
        for _ in range(length - k % length - 1):
            new_tail = new_tail.next

        # The new head is next of the new tail
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head
    
    def printTraversell(self, head):
        while head:
            print(f'{head.val}', end=' ')
            head=head.next
        print('\n')

sol=Solution()
h4=ListNode(4,None)
h3=ListNode(3,None)
h2=ListNode(2,None)
h1=ListNode(1,None)
h1.next=h2
h2.next=h3
h3.next=h4

sol.printTraversell(h1)
sol.printTraversell(sol.rotateRight(h1,2))