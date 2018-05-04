import math
import queue
import utility


def resolve(start_node=(0,0), goal_node=(4,4), inactive=[], width=5, height=5):
    V, Adj = utility.createG(inactive, width, height)

    def DFSVisit(V, Adj, time, u):
        time += 1
        V[u]['color'] = "gray"
        for v in Adj[u]:
            if V[v]['color'] is "white":
                V[v]['pi'] = u
                DFSVisit(V, Adj, time, v)
        V[u]['color'] = "black"
        time += 1
        V[u]['f'] = time

    for node in V:
        V[node]['color'] = "white"
        V[node]['pi'] = None

    time = 0

    for node in V:
        if V[node]['color'] is "white":
           DFSVisit(V, Adj, time, node)

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
