from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodesON(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack,count=[root],0
        while stack:
            curr=stack.pop()
            count+=1
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return count
    
    def countNodesBinSearch(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def depth(root): #depth is defined as distance of a node to root node - so a tree with 1 node is depth 0
            d=0
            while root.left:
                d+=1
                root=root.left
            return d
        def exists(node, d, idx): # this checks if a node exists at index in last level of tree depth d 
            l,r=0,2**d-1
            for _ in range(d):
                pivot=l+(r-l)//2
                if idx<=pivot:
                    node=node.left
                    r=pivot
                else:
                    node=node.right
                    l=pivot+1
            return node is not None

        d=depth(root)
        if d==0:
            return 1
        l,r=0,2**d-1
        node=root   #the below algo finds the first pos of node (l) which doesnt exists in last level and 
        #since it is indexs are 0 based l represent the count of nodes on last level
        #so if you just add this count l on last level l to the nodes in all upper levels we get final answer
        while l<=r:
            pivot=l+(r-l)//2 #this is done to avoid num overflow when l and r large ints
            if exists(node,d,pivot):
                l=pivot+1
            else:
                r=pivot-1
        return 2**d-1+l        

    def countNodes(self,root):
        if not root:
            return 0
        def depth(node):
            # Compute the depth (height) of a tree.
            d = 0
            while node.left:
                node = node.left
                d += 1
            return d

        d = depth(root)
        if d==0:
            return 1
        
        # If the tree has 2^d - 1 nodes, then we return the result
        if root.right and depth(root.right) == d - 1:
            return (2 ** d)  + self.countNodes(root.right)
        else:
            return (2 ** (d - 1)) + self.countNodes(root.left)


    
def testCase():
    # Create nodes
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)

    # Setup children
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node5
    node1.right = node4

    # Assuming your class is named Solution
    s = Solution()
    print(s.countNodes(root))

testCase()