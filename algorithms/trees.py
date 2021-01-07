import math
from collections import deque


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

    # https://leetcode.com/problems/binary-tree-paths/
    def binaryTreePaths(self, root: TreeNode):
        def _do(root, curr, res):
            if not root:
                return

            curr.append(str(root.val))

            if not root.left and not root.right:
                res.append('->'.join(curr))

            _do(root.left, curr, res)
            _do(root.right, curr, res)

            del curr[-1]

        res = []
        _do(root, [], res)
        return res

    # https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
    def subtreeWithAllDeepest(self, root: TreeNode):
        def _dfs(node):
            if not node:
                return (None, 0)

            (l_node, l_dist), (r_node, r_dist) = _dfs(
                node.left), _dfs(node.right)

            if l_dist > r_dist:
                return (l_node, l_dist + 1)
            if r_dist > l_dist:
                return (r_node, r_dist + 1)
            return (node, l_dist + 1)

        res_node, _ = _dfs(root)
        return res_node

    # https://leetcode.com/problems/binary-tree-maximum-path-sum/
    def maxPathSum(self, root: TreeNode):
        self.max_sum = -math.inf

        def _do(root):
            if not root:
                return 0

            left = _do(root.left)
            right = _do(root.right)

            max_left = max(left, 0)
            max_right = max(right, 0)

            curr_sum = max_left + max_right + root.val
            self.max_sum = max(self.max_sum, curr_sum)

            return max(max_left, max_right) + root.val

        _do(root)

        return self.max_sum

    # https://leetcode.com/problems/closest-binary-search-tree-value/
    def closestValue(self, root: TreeNode, target: float):
        if target < root.val:
            next_node = root.left
        else:
            next_node = root.right
        if not next_node:
            return root.val

        next_min = self.closestValue(next_node, target)

        return min(root.val, next_min, key=lambda x: abs(x - target))

    # https://leetcode.com/problems/binary-tree-level-order-traversal/
    def levelOrder(self, root: TreeNode):
        if not root:
            return
        res = []

        queue = deque()
        queue.append(root)

        while queue:
            level_len = len(queue)
            level_res = []

            for _ in range(level_len):
                curr_node = queue.popleft()
                level_res.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)
            res.append(level_res)

        return res
