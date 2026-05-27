# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '[]'
        
        arr = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                arr.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                arr.append(None)
            
        return str(arr)



            



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = ast.literal_eval(data) 


        if not arr or arr[0] is None:
            return None


        root = TreeNode(arr[0])
        queue = [root]
        idx = 1

        while queue and idx < len(arr):
            node = queue.pop(0)

            if idx < len(arr):
                if arr[idx] is not None:
                    node.left = TreeNode(arr[idx])
                    queue.append(node.left)

                idx+=1
            
            if idx < len(arr):
                if arr[idx] is not None:
                    node.right = TreeNode(arr[idx])
                    queue.append(node.right)
                idx+=1
        return root




            
            



