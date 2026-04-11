# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth(node):
            depth1 = 0
            depth2 = 0
            if node:
                if node.left:
                    depth1 = get_depth(node.left)
                if node.right:
                    depth2 = get_depth(node.right)
                return 1 + max(depth1, depth2)
            return 0

        return(get_depth(root))



                
        