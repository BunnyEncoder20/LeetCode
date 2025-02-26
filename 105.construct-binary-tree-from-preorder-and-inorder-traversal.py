#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preStart,preEnd,inStart,inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None

            # get the current subtree root
            root_val = preorder[preStart]
            inRoot = in_mpp[root_val]
            root = TreeNode(root_val)
            
            # find the number of nodes for LST
            lstNodes = inRoot - inStart  
            
            # recursively construct LST and RST
            root.left = build(preStart+1, preStart+lstNodes, inStart, inRoot-1)
            root.right = build(preStart+lstNodes+1, preEnd, inRoot+1, inEnd)
            
            # return newly constructed node
            return root
        
        # inorder mpp for O(1) lookups
        in_mpp = {val:idx for idx,val in enumerate(inorder)}
        preStart,preEnd = 0, len(preorder)-1
        inStart, inEnd = 0, len(inorder)-1
        return build(preStart,preEnd,inStart,inEnd)
        
        
# @lc code=end

