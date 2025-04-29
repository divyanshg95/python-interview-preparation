
class DiGraph:
    def __init__(self, vertices: int) -> None:
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    
    def add_edge(self, u: int, v:int) -> None:
        self.adj[u].append(v)


    
    # interesting part of the code
    # the function have the inner function dfs_utils 

    def dfs_utils(self, node: int, visited: list) -> None:
        visited[node] = True
        print(f"{node}", sep=" ,", end=" ")
        for neighbour in self.adj[node]:
            if not visited[neighbour]:
                self.dfs_utils(neighbour, visited)
    

    def DFS(self) -> None:
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.dfs_utils(i, visited)
        print()

                





    def print_graph(self) -> None:
        """
        Prints the adjacency list representation of the graph.
        Each vertex and its corresponding edges are displayed in the format:
        vertex -> edge1 edge2 ...
        """
        for r in range(self.V):
            print(f"{r} -> ",end = "")    
            for c in self.adj[r]:
                print(f"{c},", end="")
            print()
        print()
def graph():
    """
    Creates a sample directed graph, adds edges, prints the graph structure,
    and performs a Depth First Search (DFS) traversal.
    """




def graph():
    G = DiGraph(6)
    
    G.add_edge(0,1)
    G.add_edge(0,3)
    G.add_edge(1,4)
    G.add_edge(3,1)
    G.add_edge(2,4)
    G.add_edge(2,5)
    G.add_edge(5,5)
    G.print_graph()
    G.DFS()
    
if __name__ == "__main__":
    graph()







