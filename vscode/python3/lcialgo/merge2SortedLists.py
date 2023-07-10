# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        elif list2:
            curr.next=list2
        return dummy.next
    
# Create the first linked list: 1 -> 3 -> 5
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

# Create the second linked list: 2 -> 4 -> 6
list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

# Merge the two lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
current = merged_list
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next    