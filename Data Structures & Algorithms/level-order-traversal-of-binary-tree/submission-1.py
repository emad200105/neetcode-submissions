# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res=[]
        que=collections.deque()
        que.append(root)

        while que:
            qlen=len(que)
            cur=[]

            for i in range(qlen):
                node=que.popleft()
                cur.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            res.append(cur)
        return res