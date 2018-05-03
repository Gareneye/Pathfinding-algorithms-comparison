import math
import queue
import utility


def resolve(start_node=(0,0), goal_node=(4,4), inactive=[], width=5, height=5):
    V, Adj = utility.createG(inactive, width, height)

