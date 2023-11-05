from typing import List, Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[Node]) -> bool:
        from collections import deque
        if not root:
            return True
        
        q=deque([root])
        compTreeFlag=False
        while q:
            level_count=len(q)
            for _ in range(level_count):
                curr=q.popleft()
                if curr.left:
                    if compTreeFlag:
                        return False
                    else:
                        q.append(curr.left)
                else:
                    compTreeFlag=True
                
                if curr.right:
                    if compTreeFlag:
                        return False
                    else:
                        q.append(curr.right)
                else:
                    compTreeFlag=True
        return True

    def isComplete(self,root):
        if root is None:
            return False

        from collections import deque
        queue = deque()
        hasNull = False

        queue.append(root)
        while queue:
            curr = queue.popleft()
            if curr is None:
                hasNull = True
            else:
                if hasNull:
                    return False
                queue.append(curr.left)
                queue.append(curr.right)

        return True

# Function to add a new node to the tree
def addNode(data):
    return Node(data)

sol=Solution()
# Test Case 1: Complete Binary Tree
root1 = addNode(1)
root1.left = addNode(2)
root1.right = addNode(3)
root1.left.left = addNode(4)
root1.left.right = addNode(5)
root1.right.left = addNode(6)
print(sol.isCompleteTree(root1))  # Should print True
print(sol.isComplete(root1))  # Should print True    

# Test Case 2: Not a Complete Binary Tree
root2 = addNode(1)
root2.left = addNode(2)
root2.right = addNode(3)
root2.left.left = addNode(4)
root2.left.right = addNode(5)
root2.right.right = addNode(6)  # This node makes the tree incomplete
print(sol.isCompleteTree(root2))  # Should print False      
print(sol.isComplete(root2))  # Should print False    