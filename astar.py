import math
import queue
import utility

def extractMin(V, Q):
    if not Q:
        return None

    minNode = Q[0]

    for v in Q:
        if V[v]['f'] < V[minNode]['f']:
            minNode = v

    Q.remove(minNode)
    return minNode

def resolve(start_node=(0,0), goal_node=(4,4), inactive=[], width=5, height=5):
    V, Adj = utility.createG(inactive, width, height)

    for v in V:
        V[v]['g'] = math.inf
        V[v]['f'] = math.inf

    V[start_node]['g'] = 0
    V[start_node]['f'] = utility.weight(start_node, goal_node)

    S = []
    Q = [start_node]

    while Q:
        u = extractMin(V, Q)

        if u == goal_node:
            break

        S.append(u)

        for v in Adj[u]:
            if v in S:
                continue

            if v not in Q:
                Q.append(v)

            test_g = V[u]['g'] + 1

            if test_g >= V[v]['g']:
                continue

            V[v]['pi'] = u
            V[v]['g'] = test_g
            V[v]['f'] = V[v]['g'] + utility.weight(v, goal_node)

    # Presentation
    presentation = {}
    for v in S:
        value = 200
        presentation[v] = (value, value, value)

    return presentation, utility.findShortestPath(V, start_node, goal_node)

resolve()