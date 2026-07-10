# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res=[]

        def trav(root):
            if root:
                trav(root.left)
                res.append(root.val)
                trav(root.right)
        trav(root)
        for j in range(1,len(res)):
            if res[j]<=res[j-1]:
                return False
        return True