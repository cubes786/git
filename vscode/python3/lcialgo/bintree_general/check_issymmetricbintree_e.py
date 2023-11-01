from typing import List, Optional

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val,self.left,self.right=val,left,right

class Solution:
    def isSymmetricRec(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetry(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val==right.val and checkSymmetry(left.left,right.right) and checkSymmetry(left.right,right.left)
        
        if not root:
            return True
        else:
            return checkSymmetry(root.left,root.right)
        

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        if not root:
            return True
        q=deque([(root.left,root.right)])
        while q:
            first,second=q.popleft()
            if not first and not second:
                continue
            if not first or not second or first.val!=second.val:
                return False
            q.append((first.left,second.right))
            q.append((first.right,second.left))
        return True
    
def testcase():
    # Create a symmetric binary tree for testing
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    sol=Solution()

    assert sol.isSymmetric(root) == True, "Test case 1 failed"

    # Create an asymmetric binary tree for testing
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)

    assert sol.isSymmetric(root) == False, "Test case 2 failed"

    print("All test cases passed")

testcase()    