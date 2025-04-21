from collections import defaultdict
class TopologicalSort:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)
    def add_edge(self, u, v):
        self.adj[u].append(v)
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)
    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        print("Topological sorting of the graph:", end=" ")
        while stack:
            print(stack.pop(), end=" ")
ts = TopologicalSort(6)
edges = [
    (5, 2),
    (5, 1),
    (4, 3),
    (4, 1),
    (2, 3),
    (3, 1)
]
for u, v in edges:
    ts.add_edge(u, v)
ts.topological_sort()
