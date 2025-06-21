# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def it(node):
            if node is None:
                return
           
            it(node.left)
            arr.append(node.val)
            it(node.right)
   
        arr=[]
        it(root)
        return arr
