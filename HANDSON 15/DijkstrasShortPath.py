import heapq
class Node:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost
class DijkstrasShortPath:
    def __init__(self, V):
        self.V = V
        self.dist = [float('inf')] * V
        self.settled = set()
        self.pqueue = []
        self.adj = []
    def dijkstra(self, adj, src):
        self.adj = adj
        self.dist[src] = 0
        heapq.heappush(self.pqueue, Node(src, 0))
        while len(self.settled) != self.V:
            if not self.pqueue:
                return
            u = heapq.heappop(self.pqueue).node
            if u in self.settled:
                continue
            self.settled.add(u)
            self.neighbours(u)
    def neighbours(self, u):
        for v in self.adj[u]:
            if v.node not in self.settled:
                new_distance = self.dist[u] + v.cost
                if new_distance < self.dist[v.node]:
                    self.dist[v.node] = new_distance
                    heapq.heappush(self.pqueue, Node(v.node, self.dist[v.node]))
if __name__ == "__main__":
    V = 4
    source = 0
    adj = [[] for _ in range(V)]
    adj[0].append(Node(1, 6))
    adj[0].append(Node(2, 2))
    adj[1].append(Node(3, 1))
    adj[2].append(Node(1, 3))
    adj[2].append(Node(3, 5))
    dpq = DijkstrasShortPath(V)
    dpq.dijkstra(adj, source)
    print("The shorted path from node :")
    for i in range(V):
        print(f"{source} to {i} is {dpq.dist[i]}")
