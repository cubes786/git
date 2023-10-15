from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False 
        slow=head
        fast=head.next.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next

        return True

    def hasCycleAlt(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False 
        slow=head
        fast=head.next.next
        while slow and fast:
            if slow==fast:
                return True
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                fast=fast.next
        return False

sol=Solution()

# Test case 1: A list with a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle
print(sol.hasCycle(node1))
print(sol.hasCycleAlt(node1))

# Test case 2: A list without a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
print(sol.hasCycle(node1))
print(sol.hasCycleAlt(node1))

# Test case 3: An empty list
print(sol.hasCycle(None))
print(sol.hasCycleAlt(None))
