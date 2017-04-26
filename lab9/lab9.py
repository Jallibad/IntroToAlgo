from collections import deque
from heapdict import heapdict

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = heapdict()
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node,[]).append(to_node)
        self.edges.setdefault(to_node,[]).append(from_node)
        self.distances[(from_node, to_node)] = distance

g = Graph()
with open("example.txt") as file:
    for line in file:
        s,t,v = line.split(" ")
        g.add_node(s)
        g.add_node(t)
        g.add_edge(s,t,int(v))

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        u = None
        for node in nodes:
            if node in visited:
                if u is None:
                    u = node
                elif visited[node] < visited[u]:
                    u = node
        if u is None:
            break
        nodes.remove(u)
        current_weight = visited[u]

        for edge in graph.edges[u]:
            try:
                weight = current_weight + graph.distances[(u, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = u

    return visited, path

def shortest_path(graph, origin, destination):
    if origin == destination:
        return 0, list(origin)
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    if destination not in paths:
        return 0, origin
    new_destination = paths[destination]

    while new_destination != origin:
        full_path.appendleft(new_destination)
        new_destination = paths[new_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

def fordFulkerson(g, source, sink):
    max_flow = 0
    path = dijkstra(
    while 
