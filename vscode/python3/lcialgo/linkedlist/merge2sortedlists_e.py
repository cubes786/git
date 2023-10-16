from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode=ListNode(0)
        curr=dummyNode
        while list1 and list2:
            if list1.val<list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        curr.next=list1 if list1 else list2
        return dummyNode.next
    
sol=Solution()

# Creating nodes for list1
node1 = ListNode(5)
node2 = ListNode(10)
node3 = ListNode(15)

# Linking nodes for list1
node1.next = node2
node2.next = node3

# Creating nodes for list2
node4 = ListNode(2)
node5 = ListNode(3)
node6 = ListNode(20)

# Linking nodes for list2
node4.next = node5
node5.next = node6

# Merging the two lists
merged_list = sol.mergeTwoLists(node1, node4)

# Printing the merged list
while merged_list is not None:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next