import math
import queue
import utility


def resolve(start_node=(0,0), goal_node=(4,4), inactive=[], width=5, height=5):
    V, Adj = utility.createG(inactive, width, height)

    for node in V:
        V[node]['color'] = "white"
        V[node]['d'] = math.inf
        V[node]['pi'] = None

    V[start_node]['color'] = "gray"
    V[start_node]['d'] = 0
    V[start_node]['pi'] = None

    Q = []
    Q.append(start_node)

    while Q:
        u = Q.pop()
        for v in Adj[u]:
            if V[v]['color'] == "white":
                V[v]['color'] = "gray"
                V[v]['d'] = V[u]['d'] + 1
                V[v]['pi'] = u
                Q.append(v)
        V[u]['color'] = "black"

    #shortest path
    def findShortestPath(V, s, v):
        if s is v:
            return [s]

        if not V[v]['pi']:
            return []

        list = findShortestPath(V, s, V[v]['pi'])
        list.append(v)

        return list

    return findShortestPath(V, start_node, goal_node)