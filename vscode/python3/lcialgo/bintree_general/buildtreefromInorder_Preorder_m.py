from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def constructBinTree(preorder,prestart,preend,inorder,instart,inend):
            if prestart>preend or instart>inend:
                return None
            
            rootval=preorder[prestart]
            node=TreeNode(rootval)
            k=inorder.index(rootval)
            node.left=constructBinTree(preorder,prestart+1,prestart+(k-instart),
                                       inorder,instart,k-1)
            #k-inStart give the num of elems on left tree
            node.right=constructBinTree(preorder,prestart+(k-instart)+1,preend,
                                        inorder,k+1,inend)
            return node
        
        return constructBinTree(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)

#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

# Test case
preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
sol=Solution()
root = sol.buildTree(preorder, inorder)

# Function to print inorder traversal for testing
def printInorder(node):
    if node is not None:
        printInorder(node.left)
        print(node.val, end=' ')
        printInorder(node.right)

printInorder(root)  # Should print: 4 2 5 1 6 3 7