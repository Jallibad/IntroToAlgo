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


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        #deleteMin
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

if __name__ == '__main__':
    graph = Graph()
    
    with open("full.txt") as file:
        for line in file:
            currLine = line.strip().split(' ')
            graph.add_node(currLine[0])
            graph.add_node(currLine[1])
            graph.add_edge(str(currLine[0]),str(currLine[1]),int(currLine[2]))
    
    for i in sorted(list(graph.nodes),key = lambda x : int(x)):
        distance, path = shortest_path(graph, '1', str(i))
        print(str(i) + ': ' + str(distance) + ", [" +  ", ".join(path) + "]")
        
