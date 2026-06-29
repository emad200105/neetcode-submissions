# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checker(r1,r2):
            if not r1 and not r2:
                return True
            elif not r1:
                return False
            elif not r2:
                return False
            elif r1.val!=r2.val:
                return False
            else:
                return checker(r1.left,r2.left) and checker(r1.right,r2.right)


        if not root and not subRoot:
            return True
        elif root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root.val!=subRoot.val:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else: 
            return checker(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
