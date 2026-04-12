# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isSame(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if isSame(root, subRoot):
            return True
        if root:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        return False
        
