
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        ptr=head
        while ptr:
            newnode=Node(ptr.val,None,None)
            newnode.next=ptr.next
            ptr.next=newnode
            ptr=newnode.next
        
        ptr=head
        while ptr:
            ptr.next.random=ptr.random.next if ptr.random else None
            ptr=ptr.next.next
        
        ptr=head
        newptr=head.next
        newhead=newptr
        while ptr:
            ptr.next=ptr.next.next
            newptr.next=newptr.next.next if newptr.next else None
            ptr=ptr.next
            newptr=newptr.next
            
        return newhead
    
# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Setting up next pointers
node1.next = node2
node2.next = node3

# Setting up random pointers
node1.random = node3  # 1st node points to 3rd node
node2.random = node1  # 2nd node points to 1st node
node3.random = node2  # 3rd node points to 2nd node

# Creating a solution object
sol = Solution()

# Creating a deep copy of the list
copy_head = sol.copyRandomList(node1)

def traverse_and_verify(original_head, cloned_head):
    # Traverse both lists and compare nodes one by one
    while original_head and cloned_head:
        # Check if the value in both nodes is the same
        assert original_head.val == cloned_head.val

        # Check if the next node is the same (None in both or not None in both)
        assert (original_head.next is None) == (cloned_head.next is None)

        # Check if the random node is the same (None in both or not None in both)
        assert (original_head.random is None) == (cloned_head.random is None)

        # If random is not None, check if the value of the random node is the same
        if original_head.random:
            assert original_head.random.val == cloned_head.random.val

        # Move to the next node in both lists
        original_head = original_head.next
        cloned_head = cloned_head.next

    # Check if we have reached the end of both lists (they have the same length)
    assert (original_head is None) and (cloned_head is None)

# Call this function with your original and cloned heads
traverse_and_verify(node1, copy_head)