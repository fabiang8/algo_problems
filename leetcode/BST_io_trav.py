# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.reslist = []
        
        self.collect_vals(root)
        
        return self.reslist
    
    def collect_vals(self,root):
        
        if root is None:
            return None
        
        self.collect_vals(root.left)
        
        self.reslist.append(root.val)
        
        self.collect_vals(root.right)
        