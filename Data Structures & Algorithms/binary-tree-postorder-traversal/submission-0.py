# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def sol(root):
            if root:
                sol(root.left)
                sol(root.right)
                res.append(root.val)

        sol(root)
        return res
