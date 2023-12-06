from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self, directed): 
   
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
      
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        """It takes starting node and 
        goal node as parameters then it returns 
        a path using Uniform Cost Search Algorithm"""
        visited = []  
        queue = PriorityQueue()
        queue.put((0, current_node))
        
        while not queue.empty():
            item = queue.get()
            current_node =  item[1]
            
            if current_node == goal_node:
                print(current_node, end = " ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue
                    
                #print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                        queue.put((neighbour[0], neighbour[1]))




g = Graph(False)


g.graph =  defaultdict(list)

edges= int (input("\nEnter No. of Edges : "))
for i in range(edges):
    src=input("\nEnter Starting Vertex = ")
    dest=input("\nEnter Destination Vertex = ")
    wt=int(input("\nEnter Weight of Cost = "))
    g.add_edge(src,dest,wt)


g.graph
S=input("\n enter starting index=")
G=input("\n enter goal  index=")

g.ucs(S,G)
print("A  K L G")