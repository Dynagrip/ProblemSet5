 from graph import *

def DFS(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    # print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph,node,end,path,shortest)
            if newPath != None:
                return newPath

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest



def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))

    h = Digraph()
    for n in nodes:
        h.addNode(n)
    h.addEdge(Edge(nodes[0],nodes[1]))
    h.addEdge(Edge(nodes[1],nodes[2]))
    h.addEdge(Edge(nodes[2],nodes[3]))
    h.addEdge(Edge(nodes[2],nodes[4]))
    h.addEdge(Edge(nodes[3],nodes[4]))
    h.addEdge(Edge(nodes[3],nodes[5]))
    h.addEdge(Edge(nodes[0],nodes[2]))
    h.addEdge(Edge(nodes[1],nodes[0]))
    h.addEdge(Edge(nodes[3],nodes[1]))
    h.addEdge(Edge(nodes[4],nodes[0]))
    sp = DFS(h, nodes[0], nodes[5])
    # print 'Shortest path found by DFS:', printPath(sp)

