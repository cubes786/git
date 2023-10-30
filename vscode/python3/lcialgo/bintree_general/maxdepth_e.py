from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthRec(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack,maxd=[(root,1)],1
        while stack:
            curr,d=stack.pop()
            if curr.left:
                stack.append((curr.left,1+d))
            if curr.right:
                stack.append((curr.right,1+d))
            maxd=max(maxd,d)
        return maxd


def test_maxDepth():
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance of Solution
    solution = Solution()

    # Call maxDepth method
    depth = solution.maxDepth(root)

    print(depth)
    # Assert that the maximum depth is correct
    #assert depth == 3, f"Expected 3, but got {depth}"

# Run the test
test_maxDepth()