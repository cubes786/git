from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], preorder: List[int]) -> Optional[TreeNode]:
        def constructBinTree(postorder, postStart, postEnd,inorder, inStart, inEnd):
                if postStart > postEnd or inStart > inEnd:
                    return None
                value = postorder[postEnd]
                root = TreeNode(value)
                k = inorder.index(value)
                root.left = constructBinTree(postorder, postStart, postStart + (k - inStart) - 1,
                                            inorder, inStart, k - 1) 
                #k-inStart give the num of elems on left tree, the -1 is due to fact that 
                #in postorder the right tree is immediately after leftree
                root.right = constructBinTree(postorder, postStart + (k - inStart), postEnd - 1,
                                            inorder, k + 1, inEnd)
                return root
        return constructBinTree(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)

#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

# Test case
#preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]
sol=Solution()
root = sol.buildTree(inorder, postorder)

# Function to print inorder traversal for testing
def printInorder(node):
    if node is not None:
        printInorder(node.left)
        print(node.val, end=' ')
        printInorder(node.right)

printInorder(root)  # Should print: 4 2 5 1 6 3 7