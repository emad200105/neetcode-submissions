# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def sol(cur,maxi):
            if not cur:
                return 0
            if cur.val>=maxi:
                return 1+sol(cur.left,cur.val)+sol(cur.right,cur.val)

            return sol(cur.left,maxi)+sol(cur.right,maxi)
        
        return 1+sol(root.left,root.val)+sol(root.right,root.val)