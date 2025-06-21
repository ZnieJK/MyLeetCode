#Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stacky = root, []
        res = []

        while cur or stacky:
            if cur:
                res.append(cur.val)
                stacky.append(cur.right)
                cur = cur.left
            else:
                cur = stacky.pop()

        return res      