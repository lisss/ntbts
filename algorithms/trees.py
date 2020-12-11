class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/binary-tree-inorder-traversal/
    def _do_in_order_traverse(self, root: TreeNode, res):
        if not root:
            return
        if root.left:
            self._do_in_order_traverse(root.left, res)

        res.append(root.val)

        if root.right:
            self._do_in_order_traverse(root.right, res)

        return res

    def inorderTraversal(self, root: TreeNode):
        res = []
        return self._do_in_order_traverse(root, res)

    # https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    # TODO: check their follow-up and try to optimize
    def kthSmallest(self, root: TreeNode, k: int):
        res = []
        self._do_in_order_traverse(root, res)

        return res[k - 1]

    # https://leetcode.com/problems/range-sum-of-bst/
    def rangeSumBST(self, root: TreeNode, low: int, high: int):
        if not root:
            return 0

        left = self.rangeSumBST(root.left, low, high) if root.val > low else 0
        right = self.rangeSumBST(
            root.right, low, high
        ) if root.val < high else 0

        if root.val <= high and root.val >= low:
            return left + right + root.val

        return left + right
