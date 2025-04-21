class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank
def find_root(subsets, i):
    if subsets[i].parent != i:
        subsets[i].parent = find_root(subsets, subsets[i].parent)
    return subsets[i].parent
def union(subsets, x, y):
    root_x = find_root(subsets, x)
    root_y = find_root(subsets, y)
    if subsets[root_x].rank < subsets[root_y].rank:
        subsets[root_x].parent = root_y
    elif subsets[root_x].rank > subsets[root_y].rank:
        subsets[root_y].parent = root_x
    else:
        subsets[root_y].parent = root_x
        subsets[root_x].rank += 1
def kruskals(V, edges):
    edges.sort(key=lambda e: e.weight)
    subsets = [Subset(i, 0) for i in range(V)]
    result = []
    i = 0  
    e = 0  
    while e < V - 1:
        next_edge = edges[i]
        i += 1
        x = find_root(subsets, next_edge.src)
        y = find_root(subsets, next_edge.dest)
        if x != y:
            result.append(next_edge)
            union(subsets, x, y)
            e += 1
    print("Following are the edges of the constructed MST:")
    min_cost = 0
    for edge in result:
        print(f"{edge.src} -- {edge.dest} == {edge.weight}")
        min_cost += edge.weight
    print(f"Total cost of Kruskals: {min_cost}")
V = 9
edges = [
    Edge(0, 1, 4),
    Edge(0, 7, 8),
    Edge(1, 7, 11),
    Edge(1, 2, 8),
    Edge(7, 8, 7),
    Edge(6, 7, 1),
    Edge(6, 8, 6),
    Edge(2, 8, 2),
    Edge(2, 5, 4),
    Edge(2, 3, 7),
    Edge(5, 3, 14),
    Edge(5, 4, 10),
    Edge(3, 4, 9)
]
kruskals(V, edges)
