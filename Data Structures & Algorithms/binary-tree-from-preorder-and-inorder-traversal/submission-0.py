# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
hash_map = {}
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ran = False
        if not ran:
            for i,k in enumerate(inorder):
                hash_map[k] = i
            ran = True

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = hash_map[preorder[0]]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root



            
        