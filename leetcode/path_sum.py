# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recursive_inorder(self,root,targetsum,cur):
        
        if root is None:
            return False
        cur += root.val
        if cur == targetsum and root.left is None and root.right is None:
            return True
        return (self.recursive_inorder(root.right,targetsum,cur) or self.recursive_inorder(root.left,targetsum,cur))
        
        
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.recursive_inorder(root,targetSum,0)