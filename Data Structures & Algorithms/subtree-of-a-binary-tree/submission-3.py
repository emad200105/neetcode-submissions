class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sol(l1, l2):
            if not l1 and not l2:
                return True
            if not l1 or not l2:
                return False
            if l1.val != l2.val:
                return False

            return sol(l1.left, l2.left) and sol(l1.right, l2.right)

        if not subRoot:
            return True
        if not root:
            return False

        if root.val == subRoot.val and sol(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)