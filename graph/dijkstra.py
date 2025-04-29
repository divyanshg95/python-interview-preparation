import heapq 

class DiGraph: 
    def __init__(self, graph: dict = {}):
        self.graph = graph # A dictionary of adjacency list 

    def add_edge(self, source: str, target: str, weight: float):
        if not source in self.graph.keys():
            self.graph[source] = {}
        #self.graph[source][target] = weight
        self.graph[source] = {target:weight}

    def print(self): 
        for node, edges in self.graph.items():
            print(f"{node} -> ", end="")
            for (node, weight) in edges.items():
                print(f"{node}: {weight}, ", end="")
            print()
        print()

    def dijkstra(self, graph : dict, start:str) -> list:
        distances = {node: float('inf') for node in graph.keys()}
        distances[start] = 0 
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)

        while priority_queue:
            (distance, source) = heapq.heappop(priority_queue) 
            
            # if distance present in heap is higher means this 
            # is stale entry and it can be ignored  
            if distance > distances[source]:
                continue
        
            for (target, weight) in graph[source].items():
                if distance + weight < distances[target]:
                    distances[target] = distance + weight
                    heapq.heappush(priority_queue, (distance + weight, target))
                
        return distances    

    
if __name__ == "__main__":
    graph = {
        "A": {"B": 3, "C": 3},
        "B": {"A": 3, "D": 3.5, "E": 2.8},
        "C": {"A": 3, "E": 2.8, "F": 3.5},
        "D": {"B": 3.5, "E": 3.1, "G": 10},
        "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
        "F": {"G": 2.5, "C": 3.5},
        "G": {"F": 2.5, "E": 7, "D": 10},
    }
    g = DiGraph(graph)
    g.print()

    distances = g.dijkstra(graph, "B")
    print(distances)

    ## test adding edges 

    # gt = DiGraph()
   

    # # Add A and its neighbors
    # gt.add_edge("A", "B", 3)
    # gt.add_edge("A", "C", 3)

    # # Add B and its neighbors
    # gt.add_edge("B", "A", 3)
    # gt.add_edge("B", "D", 3.5)
    # gt.add_edge("B", "E", 2.8)
    # gt.print()






