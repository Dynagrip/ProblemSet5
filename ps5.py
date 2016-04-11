# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#as each node is read, add nodes and edges to graph

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here
# describing how you will model this problem as a graph.

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#as each node is read, add nodes and edges to graph
def edgeDist(digraph,start, end):
    
    for element in digraph.edges[start]:
        if element[0] == end:
            return (element[1],element[2])
            
    return None
            
            
            
            
            

def pathDist(digraph,path):
    totalDist = 0
    outDist = 0
    # return len(path)
           
    if type(path) != None:

        for i in range(1,len(path)):
            totalDist += edgeDist(digraph,path[i-1],path[i])[0]

            outDist += edgeDist(digraph,path[i-1],path[i])[1]
    #
    return (totalDist,outDist)
def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph
    Parameters:
        mapFilename : name of the map file
    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.
    Returns:
        a directed graph representing the map
    """
    # TODO
    g = WeightedDigraph()
    mitmap = open(mapFilename,"r")
    print "Loading map from file..."
    for line in mitmap:
        line = line.split()
        line[3].strip("\n")
        na = Node(line[0])
        nb = Node(line[1])

        try:
            g.addNode(na)
            g.addNode(nb)
        except:
            pass

        try:

            e = WeightedEdge(na,nb,line[2],line[3])
            g.addEdge(e)
        except:

            g.addNode(nb)
            g.addEdge(e)



    return g

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#Will first generate all possible paths, while generating will only append ones
#that do not exceed maxTotalDist and maxDistOutdoors to winnow down the list
#and improve performance. After that will go through the list

def DFS(digraph, start, end, maxTotalDist,maxDistOutdoors, path = [],shortest = None ):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph

    path = path + [start]
    if Node(start) == Node(end) and (pathDist(digraph,path)[0] <= maxTotalDist and pathDist(digraph,path)[1] <= maxDistOutdoors):
        if pathDist(digraph,path)[0] <= maxTotalDist and pathDist(digraph,path)[1] <= maxDistOutdoors:
        # print path
            return path
    for node in digraph.childrenOf(start):

        if node not in path:
            newPath = DFS(digraph,node,end,maxTotalDist,maxDistOutdoors,path,shortest)

            try:
                if newPath != None:
                    return newPath
                    
            except:
                raise ValueError


def DFSShortest(digraph, start, end, maxTotalDist,maxDistOutdoors,path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    answer = []

    if start == end and (pathDist(digraph,path)[0] <= maxTotalDist and pathDist(digraph,path)[1] <= maxDistOutdoors):
        for element in path:
            answer.append(element.getName())
       
        return path
#            return answer
#        else:
#            raise ValueError
    for node in digraph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or (pathDist(digraph,path)[0]<=pathDist(digraph,shortest)[0] and pathDist(digraph,path)[1]<=pathDist(digraph,shortest)[1] and pathDist(digraph,path)[0] <= maxTotalDist and pathDist(digraph,path)[1] <= maxDistOutdoors):
                newPath = DFSShortest(digraph,node,end,maxTotalDist,maxDistOutdoors,path,shortest)
                if newPath != None and (pathDist(digraph,newPath)[0] <= pathDist(digraph,newPath)[0] and (pathDist(digraph, newPath))[1] <= pathDist(digraph,newPath)[1]):
                    shortest = newPath
    return shortest


def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.
    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)
    Assumes:
        start and end are numbers for existing buildings in graph
    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.
        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
#path = []


def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.
    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)
    Assumes:
        start and end are numbers for existing buildings in graph
    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.
        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
#    global path
    path = path + [start]
    answer = []

    if start == end and (pathDist(digraph,path)[0] <= maxTotalDist and pathDist(digraph,path)[1] <= maxDistOutdoors):
#        global path   
#        return path
#        for element in path:
#            answer.append(element.getName())
            
#        global path
#        path = []
       
        return path
#            return answer
#        else:
#            raise ValueError
    for node in digraph.childrenOf(start):
        if node not in path:
#            global shortest#avoid cycles
#         if shortest == None or (pathDist(digraph,path)[0]<=pathDist(digraph,shortest)[0] and pathDist(digraph,path)[1]<=pathDist(digraph,shortest)[1] and pathDist(digraph,path)[0] <= maxTotalDist and pathDist(digraph,path)[1] <= maxDistOutdoors):
            if shortest == None or (pathDist(digraph,path)[0]<=pathDist(digraph,shortest)[0] and pathDist(digraph,path)[1]<=pathDist(digraph,shortest)[1] and pathDist(digraph,path)[0] <= maxTotalDist and pathDist(digraph,path)[1] <= maxDistOutdoors):
                newPath = directedDFS(digraph,node,end,maxTotalDist,maxDistOutdoors)
                if newPath != None and (pathDist(digraph,newPath)[0] <= pathDist(digraph,newPath)[0] and (pathDist(digraph, newPath))[1] <= pathDist(digraph,newPath)[1]):
#                    global shortest
                    shortest = newPath
#    global shortest
    return shortest

# mitMap = load_map("mit_map.txt")
#mitMap = load_map("mit_map.txt")
#LARGE_DIST = 1000000
#testDFS = directedDFS(mitMap, Node('32'), Node('56'), LARGE_DIST, 0)
#dfsPath1 = DFSShortest(mitMap,  Node('32'), Node('56'), LARGE_DIST, LARGE_DIST)
#dfsPath2 = DFSShortest(mitMap, Node('32'), Node('56'), LARGE_DIST, 0)
#dfsPath3 = DFSShortest(mitMap, Node('2'), Node('9'), LARGE_DIST, LARGE_DIST)
#dfsPath4 = DFSShortest(mitMap, Node('2'), Node('9'), LARGE_DIST, 0)

# Uncomment below when ready to test
### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    # Test cases
    mitMap = load_map("mit_map.txt")
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges


    LARGE_DIST = 1000000

    # Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = [Node('32'), Node('56')]
    brutePath1 = DFS(mitMap, Node('32'), Node('56'), LARGE_DIST, LARGE_DIST)
    dfsPath1 = DFSShortest(mitMap,  Node('32'), Node('56'), LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1)

#     Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 =  DFS(mitMap, Node('32'), Node('56'), LARGE_DIST, 0)
    dfsPath2 = DFSShortest(mitMap, Node('32'), Node('56'), LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = DFS(mitMap, Node('2'), Node('9'), LARGE_DIST, LARGE_DIST)
    dfsPath3 = DFSShortest(mitMap, Node('2'), Node('9'), LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    for element in expectedPath4:
        element = Node(element)
    brutePath4 = DFS(mitMap, Node('2'), Node('9'), LARGE_DIST, 0)
    dfsPath4 = DFSShortest(mitMap, Node('2'), Node('9'), LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

    # Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = DFS(mitMap, Node('1'), Node('32'), LARGE_DIST, LARGE_DIST)
    dfsPath5 = DFSShortest(mitMap, Node('1'), Node('32'), LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = DFS(mitMap, Node('1'), Node('32'), LARGE_DIST, 0)
    dfsPath6 = DFSShortest(mitMap, Node('1'), Node('32'), LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'

#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'

#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

##     Test case 8
#    print "---------------"
#    print "Test case 8:"
#    print "Find the shortest-path from Building 10 to 32 without walking"
#    print "more than 100 meters in total"
#    bruteRaisedErr = 'No'
#    dfsRaisedErr = 'No'
#    try:
#        DFS(mitMap, Node('10'), Node('32'), 100, LARGE_DIST)
#    except ValueError:
#        bruteRaisedErr = 'Yes'
#
#    try:
#        DFSShortest(mitMap, Node('10'), Node('32'), 100, LARGE_DIST)
#    except ValueError:
#        dfsRaisedErr = 'Yes'
#
#    print "Expected: No such path! Should throw a value error."
#    print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr
