import math

MAX_DISTANCE = 40075017 #meters
def aStar(jsonNodes, start, dest, hash):

    # hash stores a constant lookup between guid and the node itself
    # hash = genHash(jsonNodes)

    heuristic = genHeuristic(jsonNodes, hash[dest])

    # a star search

    # IT IS ASSUMED START IS A GUID, NOT A NODE OBJECT
    curr = hash[start]
    openList = []
    currCost = 0
    currPath = [start]

    while(curr['guid'] != dest):
        
        # add all nodes adjacent to current node to list with each nodes' cost, heuristic, and path
        for guid in curr['adjacencyList']:
            openList.append({
                'cost' : currCost + dist(curr, hash[guid]),
                'heuristic' : heuristic[guid],
                'path' : currPath + [guid],
                'guid' : guid,
            })
        # find node in list with lowest cost + heuristic
        minTotalCost = MAX_DISTANCE

        for index, openListNode in enumerate(openList):
            if(openListNode['cost'] + openListNode['heuristic'] < minTotalCost):
                minTotalCost = openListNode['cost'] + openListNode['heuristic']
                minElement = openListNode
                minElementIndex = index
            
        # remove lowest cost + heuristic element from list
        openList.pop(minElementIndex)

        # update curr with the new min element
        curr = hash[minElement['guid']]
        currPath = minElement['path']
        currCost = minElement['cost']

    # currPath should now hold list of guids to follow to get from start to dest
    return currPath, currCost
    
def genHash(jsonNodes):
    hash = {}
    for node in jsonNodes:
        hash[node['guid']] = node
        
    return hash


def genHeuristic(nodes, dest):
    heuristic = {}
    for node in nodes:
        heuristic[node['guid']] = dist(node, dest)
    return heuristic

def dist(node1, node2):
    return math.sqrt( (node1['lat'] - node2['lat'])**2 + (node1['long'] - node2['long'])**2 )