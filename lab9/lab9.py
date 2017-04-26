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
        self.distances[(to_node, from_node)] = 0

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

        if u not in graph.edges:
            continue
        for edge in graph.edges[u]:
            try:
                weight = current_weight + graph.distances[(u, edge)]
            except:
                continue
            if (edge not in visited or weight < visited[edge]) and graph.distances[(u,edge)]>0:
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

def explore(s, g, visited=set()):
    visited.add(s)
    for u in g.edges[s]:
        if u not in visited and g.distances[(s,u)]>0:
            explore(u, g, visited)
    return visited

def fordFulkerson(g, source, sink):
    max_flow = 0
    a, path = shortest_path(g, source, sink)
    while a != 0:
        flow = g.distances[(path[0],path[1])]
        for i in range(1,len(path)):
            flow = min(flow, g.distances[(path[i-1],path[i])])
        max_flow += flow
        for i in range(1,len(path)):
            g.distances[(path[i-1],path[i])] -= flow
            g.distances[(path[i],path[i-1])] += flow
            
        a, path = shortest_path(g, source, sink)
    visited = explore(source,g)
    print("max flow =", max_flow)
    print("minimum cut =",max_flow, sorted(visited), sorted(g.nodes - visited))

g = Graph()
with open("example.txt") as file:
    for line in file:
        s,t,v = line.split(" ")
        g.add_node(int(s))
        g.add_node(int(t))
        g.add_edge(int(s),int(t),int(v))
fordFulkerson(g,min(g.nodes),max(g.nodes))
