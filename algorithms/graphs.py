class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # https://leetcode.com/problems/clone-graph/
    def cloneGraph(self, node: Node):
        if not node:
            return
        if not node.neighbors:
            return Node(node.val)

        visited = {}

        def _do(node: Node):
            new_node = Node(node.val)
            visited[node.val] = new_node
            for x in node.neighbors:
                if x.val not in visited:
                    cloned = _do(x)
                    new_node.neighbors.append(cloned)
                else:
                    new_node.neighbors.append(visited[x.val])
            return new_node

        return _do(node)
