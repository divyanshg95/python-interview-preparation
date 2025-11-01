
from collections import deque

class DiGraph:
    def __init__(self, V):
        self.V = V
        self.adj = [ [] for _ in range(V) ]

    def add_edge(self, e, v):
        self.adj[e].append(v) 
    

    # prints the graph's adjuncy matrix 
    def print_graph(self):
        for i in range(self.V):
            print(f"{i} -> {self.adj[i]}")



    def dfs_helper(self, visited, node):
        print(f"{node}, ", sep= "", end="")
        visited[node] = True

        for neighbour in self.adj[node]:
            if not visited[neighbour]:
                self.dfs_helper(visited, neighbour)
                



    def dfs(self):

        visited = [False] * self.V
        print(f"DFS Traversal")
        for n in range(self.V):
            if not visited[n]:
                self.dfs_helper(visited, n)
        print()
        print(f"End DFS Traversal")

    
    def bfs_helper(self, visited, source):
        q =  deque()
        q.append(source)
        visited[source] = True

        while q: 
            node = q.popleft()
            print(f"{node}, ", sep="", end="")
            

            for neighbour in self.adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)



    def bfs(self):
        visited = [False] * self.V

        print(f"BFS Traversal")
        for n in range(self.V):
            if not visited[n]:
                self.bfs_helper(visited, n)
        print()
        print(f"End BFS Traversal")






if __name__ == "__main__":

    G = DiGraph(6)
    
    G.add_edge(0,1)
    G.add_edge(0,3)
    G.add_edge(1,4)
    G.add_edge(3,1)
    G.add_edge(2,4)
    G.add_edge(2,5)
    G.add_edge(5,5)
    G.print_graph()
    
    G.dfs()
    G.bfs()



    



        



