# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #to validate bst, we should not just check left and right nodes
    # because there might be a tree where left and right nodes 
    # are properly maintained but it might not be a bst , a value less than 
    # root might be there on the right sub tree. so, we need to check all the
    # nodes of right tree and left sub tree to determine the current node
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, leftLimit, rightLimit):
            if root is None:
                return True
            if(root.val <= leftLimit or root.val >= rightLimit):
                return False
            return valid(root.left, leftLimit, root.val) and valid(root.right, root.val, rightLimit)
        return valid(root, float('-inf'), float('inf'))

        