# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        arr = []
        
        self.inorder(root, arr)
        
        for i in range(0, len(arr)-1, 1):
            if (arr[i+1] <= arr[i]):
                return False
            
        return True
            
    def inorder(self, root, accum):
        if root is not None:
            self.inorder(root.left, accum)
            
            accum.append(root.val)
            
            self.inorder(root.right, accum)