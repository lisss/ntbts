class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/binary-tree-inorder-traversal/
    def _do(self, root: TreeNode, res):
        if not root:
            return
        if root.left:
            self._do(root.left, res)

        res.append(root.val)

        if root.right:
            self._do(root.right, res)

        return res

    def inorderTraversal(self, root: TreeNode):
        res = []
        return self._do(root, res)
