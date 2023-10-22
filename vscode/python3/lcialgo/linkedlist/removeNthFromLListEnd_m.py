from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
# The reason we take n+1 steps instead of n is to position the first pointer
# one step ahead of the node we want to remove. This is because in a singly linked list, 
# we don’t have a direct way to access the previous node, but we can access the next 
# node through the next pointer.
# So, if we want to remove the nth node from the end, we need to access the (n+1)th node 
# from the end (which is the node before the nth node from the end). This way, we can easily 
# skip over the nth node by setting (n+1)thNode.next = (n+1)thNode.next.next.
# That’s why we first move the first pointer n+1 steps from the start. Then, when we move both
# first and second pointers until first reaches the end, second will be at the (n+1)th node 
# from the end. Now, we can remove the nth node from the end by skipping it in the next pointer of the (n+1)th node.
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        first=second=dummy
        for _ in range(n+1):
            first=first.next
        while first:
            first,second=first.next,second.next
        second.next=second.next.next

        return dummy.next
    
    def removeNthFromEndUsing2Passes(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reversell(ptr):
            prev,curr=None,ptr
            while curr:
                next_temp=curr.next
                curr.next=prev
                prev=curr
                curr=next_temp
            return prev

        tail=reversell(head)      
        curr,prev=tail,None
        for _ in range(n-1):
            prev=curr
            curr=curr.next

        prev.next=curr.next

        return reversell(prev)
    
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
sol.printTraversell(sol.removeNthFromEnd(h1,2))

