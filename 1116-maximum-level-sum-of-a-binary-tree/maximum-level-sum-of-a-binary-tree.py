# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        d=deque([root])
        maxLevel=0
        level=0
        maxSum=float('-inf')
        while(d):
            sum=0
            level+=1
            for i in range(len(d)):
                k=d.popleft()
                sum+=k.val
                if(k.left):
                    d.append(k.left)
                if(k.right):
                    d.append(k.right)
            print(sum, maxSum,  level)
            if(sum > maxSum):
                maxSum=sum
                maxLevel=level
        return maxLevel
            
        











        