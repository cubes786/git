from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTreeRec(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False

        if p and q:
            if p.val!=q.val:
                return False
            
            lres= self.isSameTree(p.left, q.left)
            if not lres:
                return False
            rres= self.isSameTree(p.right, q.right)
            if not rres:
                return False
        return True
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True        
            if not p or not q:
                return False            
            if p.val!=q.val:
                return False
            
            return True
        
        stack=[(p,q)]
        while stack:
            currp,currq=stack.pop()
            if not check(currp,currq):
                return False
            if currp and currq:
                stack.append((currp.left,currq.left))
                stack.append((currp.right,currq.right))
            
        return True


def test_isSameTree():
    # Create two binary trees
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    # Create an instance of Solution
    solution = Solution()

    # Call isSameTree method
    is_same = solution.isSameTree(p, q)

    print(is_same)
    # Assert that the trees are the same
    #assert is_same, "Expected True, but got False"

# Run the test
test_isSameTree()