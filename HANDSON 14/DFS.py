from collections import defaultdict
class DFS:
    def __init__(self, v):
        self.V = v
        self.adj = defaultdict(list)

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for n in self.adj[v]:
            if not visited[n]:
                self.dfs_util(n, visited)

    def dfs(self, v):
        visited = [False] * self.V
        self.dfs_util(v, visited)
graph = DFS(8)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.add_edge(3, 6)
graph.add_edge(4, 7)
graph.add_edge(4, 5)
graph.add_edge(5, 2)
print("Following is Depth First Traversal (starting from vertex 0)")
graph.dfs(0)
