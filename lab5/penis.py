def reverseGraph(g):
    ans = {}
    for a, b in g.items():
        for i in b:
            if i in ans:
                ans[i].append(a)
            else:
                ans[i] = [a]
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

def main():
    #sys.setrecursionlimit(1000) #increase recursion limit from 400 to 1000
    
    graph = buildGraph("example.txt")
    reverse = reverseGraph(graph)
    print(graph)
    
    #test 2: operate on test.txt
    
    
if __name__ == "__main__":
    main()
