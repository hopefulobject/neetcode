# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertCurr(node):
            if node.right or node.left:
                temp = node.right
                node.right = node.left
                node.left = temp

                if node.right:
                    invertCurr(node.right)
                if node.left:
                    invertCurr(node.left)
            return node


            
        if root:
            return invertCurr(root)


            

        