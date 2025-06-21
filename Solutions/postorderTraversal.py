#Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def it(node):
            if not node:
                return
           
            it(node.left)
            it(node.right)
            arr.append(node.val)


        arr = []
        it(root)
        return arr