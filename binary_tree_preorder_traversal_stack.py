# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        s = []
        res = []
        
        while (root != None) or (len (s) != 0):
            if root != None:
                res.append(root.val)         
                if root.right != None: 
                    s.append(root.right)
                root = root.left
            else:
                root = s.pop()
                
        return res
