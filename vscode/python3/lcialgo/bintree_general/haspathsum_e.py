from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val,self.left,self.right=val,left,right
    
class Solution:
    def hasPathSumRec(self, root: Optional[TreeNode], targetSum: int)->bool:
        def dfsSumCheck(root, tsum):
            if root:
                tsum-=root.val
                if tsum==0 and not root.left and not root.right:
                    return True

                return dfsSumCheck(root.left, tsum) or dfsSumCheck(root.right, tsum)
            return False
            
        return dfsSumCheck(root,targetSum)
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int)->bool:
        if not root:
            return False

        stack=[(root, targetSum-root.val)]
        while stack:
            curr,tsum=stack.pop()
            if tsum==0 and not curr.left and not curr.right:
                return True
            if curr.left:
                stack.append((curr.left,tsum-curr.left.val))
            if curr.right:
                stack.append((curr.right,tsum-curr.right.val))
        return False


def testCase():
    # Create nodes
    root = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    node3 = TreeNode(11)
    node4 = TreeNode(13)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(2)
    node8 = TreeNode(1)

    # Setup children
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.right = node8

    # Assuming your class is named Solution
    s = Solution()
    print(s.hasPathSum(root, 22))

testCase()