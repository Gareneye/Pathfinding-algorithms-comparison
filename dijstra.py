import math
import queue
import utility

def extractMin(V, Q):
    if not Q:
        return None

    minNode = Q[0]

    for v in Q:
        if V[v]['d'] < V[minNode]['d']:
            minNode = v

    Q.remove(minNode)
    return minNode

def resolve(start_node=(0,0), goal_node=(4,4), inactive=[], width=5, height=5):
    V, Adj = utility.createG(inactive, width, height)

    # Initialize Single Source
    for v in V:
        V[v]['d'] = math.inf
        V[v]['pi'] = None

    V[start_node]['d'] = 0

    # Funkcja wagi jest w utility
    # Relaksacja dla wagi 1
    def relax(V, u, v):
        #w = utility.weight(u, v)
        w = 1

        if V[v]['d'] > V[u]['d'] + w:
            V[v]['d'] = V[u]['d'] + w
            V[v]['pi'] = u

    S = []
    Q = [v for v in V]

    while Q:
        u = extractMin(V, Q)
        S.append(u)
        for v in Adj[u]:
            relax(V, u, v)

        if u == goal_node:
            break

    # Presentation
    presentation = {}
    for v in S:
        value = 200
        presentation[v] = (value, value, value)

    return presentation, utility.findShortestPath(V, start_node, goal_node)

resolve()