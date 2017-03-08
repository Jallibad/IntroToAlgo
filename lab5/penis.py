def reverseGraph(g):
    ans = {}
    for a, b in g.items():
        for i in b:
            ans.setdefault(i, []).append(a)
    return ans

def buildGraph(file):
    graph = {}
    with open(file) as f:
        for line in f:
            curLine = line.strip().split(' ')
            if (not graph.__contains__(curLine[0])):
                graph[curLine[0]] = []
            graph[curLine[0]].append(curLine[1])
    return graph

def explore(a, graph, visited, post, p=False):
    visited[a] = True
    for u in graph.get(a, []):
        if not visited.get(u):
            if p:
                print(u, end=' ')
            explore(u, graph, visited, post, p)
    post.insert(0, a)

def main():
    #sys.setrecursionlimit(1000) #increase recursion limit from 400 to 1000
    
    graph = buildGraph("example.txt")
    reverse = reverseGraph(graph)
    #print(graph)
    #print(reverse)
    
    visited = {}
    for a in graph:
        visited[a] = False

    post = []
    for a in reverse:
        if not visited.get(a):
            explore(a, reverse, visited, post)
    #print(post)

    visited = {}
    for u in post:
        if not visited.get(u):
            print(u, end=' ')
            explore(u, graph, visited, [], True)
            print()

if __name__ == "__main__":
    main()
