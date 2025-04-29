
class DiGraph:
    def __init__(self, vertices) -> None: 
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v:int) -> None: 
        self.adj[u].append(v)
    
    def topological_utils(self, node: int, visited: list, sorted: list) -> None: 
        if not visited[node]:
            visited[node] = True
            for neighbour in self.adj[node]:
                self.topological_utils(neighbour,visited, sorted)
            sorted.append(node)  
        
    # following method performs the dfs sort 
    # and add the node in sorted list at time of finish 
    def topological_sort(self):
        visited = [False] * self.V
        sorted = []
        for node in range(self.V):
            self.topological_utils(node, visited, sorted)
        print(list(reversed(sorted)))

    def print(self):
        for u in range(self.V):
            for v in self.adj[u]:
                print(f"{u} -> {v}") 
    

if __name__ == "__main__":
    graph = DiGraph(9)
    graph.add_edge(0,1)
    graph.add_edge(0,7)
    graph.add_edge(1,2)
    graph.add_edge(1,7)
    graph.add_edge(2,5)
    graph.add_edge(3,2)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(6,7)
    graph.print()
    graph.topological_sort()



        
     
