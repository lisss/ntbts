from typing import List
from collections import deque


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

    # https://leetcode.com/problems/course-schedule/
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        in_degree = {x: 0 for x in range(numCourses)}
        graph = {x: [] for x in range(numCourses)}

        for v, u in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        sources = deque()

        for k in in_degree:
            if in_degree[k] == 0:
                sources.append(k)

        ordered = []

        while sources:
            vertex = sources.popleft()
            ordered.append(vertex)

            for x in graph[vertex]:
                in_degree[x] -= 1
                if in_degree[x] == 0:
                    sources.append(x)

        return len(ordered) == numCourses

    # https://leetcode.com/problems/alien-dictionary/
    def alienOrder(self, words: List[str]):
        in_degree = {}
        graph = {}

        for word in words:
            for ch in word:
                graph[ch] = []
                in_degree[ch] = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            is_diff = False
            for i in range(min(len(w1), len(w2))):
                ch1, ch2 = w1[i], w2[i]
                if ch1 != ch2:
                    graph[ch1].append(ch2)
                    in_degree[ch2] += 1
                    is_diff = True
                    break
            if not is_diff and len(w1) > len(w2):
                return ''

        sources = deque()

        for k in in_degree:
            if in_degree[k] == 0:
                sources.append(k)

        ordered = []

        while sources:
            vertex = sources.popleft()
            ordered.append(vertex)

            for ch in graph[vertex]:
                in_degree[ch] -= 1
                if in_degree[ch] == 0:
                    sources.append(ch)

        if len(ordered) != len(in_degree):
            return ''

        return ''.join(ordered)

    # https://leetcode.com/problems/is-graph-bipartite/
    def isBipartite(self, graph: List[List[int]]):
        grouped = {}

        for i in range(len(graph)):
            if i not in grouped:
                queue = []
                queue.append((i, 0))

                while queue:
                    vert, group = queue.pop(0)
                    ch_group = 1 if not group else 0

                    for j in graph[vert]:
                        if j not in grouped:
                            grouped[j] = ch_group
                            queue.append((j, ch_group))
                        else:
                            if grouped[j] == group:
                                return False

        return True
