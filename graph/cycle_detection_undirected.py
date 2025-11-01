# following code detects the cycle in an undirected graph
# There are many ways, but we are going to use the dfs and bfs 


from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V 
        self.adj = [ [] for _ in range(self.V) ]
        
    def add_edges(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)


    # print the adj list of undirected graph
    def print_graph(self):
        for i in range(self.V):
            print(f"{i} -> {self.adj[i]}")


    def _is_cycle_helper_dfs(self, visited, node, parent):
        print(f"Check node {node}")
        visited[node] = True 

        for neighbour in self.adj[node]:
            if not visited[neighbour]:
                self._is_cycle_helper_dfs(visited, neighbour, node)
            elif neighbour != parent:
                return True

        return False 


    def is_cycle_dfs(self):
        visited = [False] * self.V
        
        for i in range(self.V):
            if not visited[i]:
                c = self._is_cycle_helper_dfs( visited, i, None)
                if c == True: 
                    return True
        
        return False 
            

    def _is_cycle_bfs_helper(self, visited, parent, i):
        q = deque()
        q.append(i)
        visited[i] = True
        parent[i] = None

        while q: 
            node = q.popleft()
            
            for neighbour in self.adj[node]:
                if not visited[neighbour]: 
                    q.append(neighbour)
                    visited[neighbour] = True
                    parent[neighbour] = node
                elif parent[neighbour] != node:
                    return True
        return False
                    

    def is_cycle_bfs(self):
        visited = [False] * self.V
        parent = [None] * self.V 

        for i in range(self.V):
            if not visited[i]: 
                c = self._is_cycle_bfs_helper(visited, parent, i)
                if c == True:
                    return True
        return False









if __name__ == "__main__":
    g = Graph(5)

    g.add_edges(0,1)
    g.add_edges(0,2)
    g.add_edges(0,3)
    g.add_edges(1,2)
    g.add_edges(3,4)

    print(g.is_cycle_dfs())
    print(g.is_cycle_bfs())

