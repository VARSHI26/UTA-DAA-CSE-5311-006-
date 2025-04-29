INF = 99999
V = 4

def floyd_warshall(dist):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print_solution(dist)

def print_solution(dist):
    print("The following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(f"{dist[i][j]}", end="   ")
        print()

if __name__ == "__main__":
    graph = [
        [0, 8, INF, 56],
        [INF, 0, 2, INF],
        [INF, INF, 0, 3],
        [INF, INF, INF, 0]
    ]
    floyd_warshall(graph)
