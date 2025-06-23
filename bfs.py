from collections import deque

def bfs(n, adj, start):
    """Return the BFS traversal order starting at `start`."""
    visited = [False] * n
    order   = []
    q = deque([start])
    visited[start] = True

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return order


def main():
    print("=== Breadth-First Search (BFS) ===")
    
    n = int(input("Number of vertices (n): "))
    m = int(input("Number of edges (m): "))
    
    adj = [[] for _ in range(n)]
    print("\nEnter each edge as two space-separated vertex IDs (0-based).")
    for i in range(m):
        u, v = map(int, input(f"  Edge {i+1}/{m}: ").split())
        # For an undirected graph add both directions
        adj[u].append(v)
        adj[v].append(u) 
    
    start = int(input("\nStart vertex for BFS: "))

    order = bfs(n, adj, start)
    print("\nBFS visitation order:", *order)


if __name__ == "__main__":
    main()
