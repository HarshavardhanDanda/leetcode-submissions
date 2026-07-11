# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res=[[root.val]]
        d=deque([root])
        while(d):
            level=[]
            for i in range(len(d)):
                k=d.popleft()
                if(k.left):
                    d.append(k.left)
                    level.append(k.left.val)
                if(k.right):
                    d.append(k.right)
                    level.append(k.right.val)
            if(len(level)):
                res.append(level)
        return res


        