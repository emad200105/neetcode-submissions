# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0

        def sol(root):
            nonlocal maxi
            if not root:
                return 0
            
            left=sol(root.left)
            right=sol(root.right)

            maxi=max(maxi,left+right)

            return 1+max(left,right)

        sol(root)
        return maxi