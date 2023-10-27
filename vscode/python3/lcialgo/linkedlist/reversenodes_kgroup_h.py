from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while True:
            curr,stack=prev,[]
            for _ in range(k):
                curr=curr.next
                if not curr:
                    return dummy.next
                stack.append(curr)
            
            nextPtr=curr.next
            while stack:
                next=stack.pop()
                prev.next=next
                prev=next
            prev.next=nextPtr

            
def list_to_nodes(values):
    dummy = ListNode()
    ptr = dummy
    for value in values:
        ptr.next = ListNode(value)
        ptr = ptr.next
    return dummy.next

def nodes_to_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values

def test_reverseKGroup():
    # Assuming the reverseKGroup function has been implemented in a class named Solution
    solution = Solution()

    head = list_to_nodes([1, 2])
    k = 2
    expected_output = [2, 1]
    print(nodes_to_list(solution.reverseKGroup(head, k)))

    head = list_to_nodes([1, 2, 3, 4, 5])
    k = 2
    expected_output = [2, 1, 4, 3, 5]
    print(nodes_to_list(solution.reverseKGroup(head, k)))
    #assert nodes_to_list(solution.reverseKGroup(head, k)) == expected_output

    head = list_to_nodes([1, 2, 3, 4, 5])
    k = 3
    expected_output = [3, 2, 1, 4, 5]
    print(nodes_to_list(solution.reverseKGroup(head, k)))
    # assert nodes_to_list(solution.reverseKGroup(head, k)) == expected_output

test_reverseKGroup()            