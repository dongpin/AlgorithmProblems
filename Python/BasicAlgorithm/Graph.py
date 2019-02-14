# Graph representations
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    def add_vertex(self, u):
        if u not in self.graph:
            self.graph[u] = []

# Graph Traverse
def dfs(graph):
    def dfs_helper(graph, u, visited, res):
        res.append(u)
        visited.add(u)
        if u in graph:
            for v in graph[u]:
                if v not in visited:
                    dfs_helper(graph, v, visited, res)

    visited = set()
    res = []
    for u in graph.keys():
        if u not in visited:
            dfs_helper(graph, u, visited, res)
    return res

def dfs_iterative(graph):
    visited = set()
    stack = []
    res = []
    for u in graph:
        if u not in visited:
            stack.append(u)
            while stack:
                cur = stack.pop()
                if cur not in visited:
                    visited.add(cur)
                    res.append(cur)
                if cur in graph:
                    # add adjacent vertex in reverse order 
                    # to maintain the same sequence as recursive approach
                    for v in graph[cur][::-1]:
                        if v not in visited:
                            stack.append(v)
    return res

def bfs(graph):
    visited = set()
    queue = []
    res = []
    for u in graph:
        if u not in visited:
            queue.append(u)
            while queue:
                cur = queue.pop(0)
                if cur not in visited:
                    visited.add(cur)
                    res.append(cur)
                if cur in graph:
                    for v in graph[cur]:
                        if v not in visited:
                            queue.append(v)
    return res

# Directed graph: Detect cycle, Topological sort, SCC, Kosaraju-Sharir algorithm

# MST: Prim's algorithm, Kruskal's algorithm

# Shortest paths: Dijkstra's algorithm, Bellman-Ford algorithm, Negative cycle detection

# Netword flow: max flow, min cut

# Cycle detection

# Topological sort

# Minimum spanning tree

# Shortest path algorithm

# Flood-fill algorithm

# Articulation point and bridges

# Biconnected components

# Strongly connected components

# Hamiltonian path

# Maximum path

# Minimum cost maximum flow

# Min-cut
