from typing import List, Optional

class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def invertTreeRec(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
           root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)

        return root
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            stack=[root]
            while stack:
                curr=stack.pop()
                if curr:
                    curr.left,curr.right=curr.right,curr.left
                    stack += curr.right,curr.left
        return root
            

def preTravelBinTree(node):
    if node:
        print(f'{node.val}', end=' ')
        preTravelBinTree(node.left)        
        preTravelBinTree(node.right)

def bfsTravelBinTree(node):
    from collections import deque
    q=deque([node])
    while q:
        curr=q.popleft()
        print(f'{curr.val}', end=' ')
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

def dfsTravelBinTree(node):
    if not node:
        return
    stack=[node]
    while stack:
        curr=stack.pop()
        print(f'{curr.val}', end=' ')
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        


def testCase():
    one=TreeNode(1)
    three=TreeNode(3)
    two=TreeNode(2,one,three)

    six=TreeNode(6)
    nine=TreeNode(9)
    seven=TreeNode(7,six,nine)

    four=TreeNode(4,two,seven)
    
    
    print('Prior Inversion tree is:')
    bfsTravelBinTree(four)
    print()
    
    sol=Solution()
    four=sol.invertTree(four)
    
    print('\nPost Inversion tree is:')
    bfsTravelBinTree(four)

testCase()    