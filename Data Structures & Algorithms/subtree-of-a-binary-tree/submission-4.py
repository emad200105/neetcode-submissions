# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sol(r,s):
            if not r and not s:
                return True
            elif not r:
                return False
            elif not s:
                return False
            elif r.val!=s.val:
                return False
            else:
                return sol(r.left,s.left) and sol(r.right,s.right)

        if not subRoot:
            return True
        if not root:
            return False
        if root.val==subRoot.val and sol(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
