from collections import deque, Counter
from typing import List


def topological_sort(vertices, edges):
    sorted_order = []
    if not vertices:
        return sorted_order

    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    sources = deque()

    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)

        for child in graph[vertex]:
            in_degree[child] -= 1

            if in_degree[child] == 0:
                sources.append(child)

    if len(sorted_order) != vertices:
        return []

    return sorted_order


def is_scheduling_possible(tasks, prerequisites):
    sorted_order = []

    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for u, v in prerequisites:
        graph[u].append(v)
        in_degree[v] += 1

    sources = deque()

    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)

    while sources:
        vert = sources.popleft()
        sorted_order.append(vert)

        for ch in graph[vert]:
            in_degree[ch] -= 1

            if in_degree[ch] == 0:
                sources.append(ch)

    return len(sorted_order) == tasks


def print_orders(tasks, prerequisites):
    sorted_order = []

    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for u, v in prerequisites:
        graph[u].append(v)
        in_degree[v] += 1

    sources = []

    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)

    def print_sorted_order(graph, sources, in_degree, sorted_order):
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = sources.copy()  # make a copy of sources
            # only remove the current source,
            # all other sources should remain in the queue for the next call
            sources_for_next_call.remove(vertex)

            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)

            # recursive call to print other orderings from the remaining (and new) sources
            print_sorted_order(graph, sources_for_next_call,
                               in_degree, sorted_order)

            # backtrack, remove the vertex from the sorted order
            # and put all of its children back to consider
            # the next source instead of the current vertex
            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1

        # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency
        # between tasks, or we have not processed all the tasks in this recursive call
        if len(sorted_order) == tasks:
            print(sorted_order)

    print_sorted_order(graph, sources, in_degree, sorted_order)

    print()


def find_order(words: List[str]):
    if not len(words):
        return ''

    in_degree = {}
    graph = {}

    for word in words:
        for char in word:
            in_degree[char] = 0
            graph[char] = []

    for i in range(0, len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(0, min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    sorted_order = []

    sources = deque()

    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)

    while sources:
        vert = sources.popleft()
        sorted_order.append(vert)

        for ch in graph[vert]:
            in_degree[ch] -= 1

            if in_degree[ch] == 0:
                sources.append(ch)

    if len(sorted_order) != len(in_degree):
        return ''

    return ''.join(sorted_order)


def can_construct(original_seq, sequences):
    if not len(original_seq):
        return False

    sorted_order = []

    in_degree = {i: 0 for i in original_seq}
    graph = {i: [] for i in original_seq}

    for seq in sequences:
        for i in range(len(seq) - 1):
            par, ch = seq[i], seq[i + 1]
            graph[par].append(ch)
            in_degree[ch] += 1

    if len(in_degree) != len(original_seq):
        return False

    sources = deque()

    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)

    while sources:
        if len(sources) > 1:
            return False
        vertex = sources.popleft()
        sorted_order.append(vertex)

        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return Counter(sorted_order) == Counter(original_seq)


def find_trees(nodes, edges):
    in_degree = {i: 0 for i in range(nodes)}
    graph = {i: [] for i in range(nodes)}

    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
        in_degree[n1] += 1
        in_degree[n2] += 1

    leaves = deque()

    for k in in_degree:
        if in_degree[k] == 1:
            leaves.append(k)

    total_nodes = nodes
    while total_nodes > 2:
        leaves_size = len(leaves)
        total_nodes -= leaves_size
        for _ in range(leaves_size):
            vertex = leaves.popleft()

            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 1:
                    leaves.append(child)

    return list(leaves)


print("Roots of MHTs: " +
      str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
