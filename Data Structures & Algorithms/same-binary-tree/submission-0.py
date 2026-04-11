# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def areSame(node1, node2):
            if not node1 and node2:
                return False
            elif not node2 and node1:
                return False
            elif node1 is None and node2 is None:
                return True
            elif node1.val == node2.val:
                children1 = True
                children2 = True
                if node1:
                    children1 = areSame(node1.left, node2.left)
                    children2 = areSame(node1.right, node2.right)

                return children1 and children2
            return False
        
        return areSame(p, q)

                    
                



        