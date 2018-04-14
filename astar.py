import math

class AStar:
    closed_set = []
    open_set = []
    inactive = []
    current_node = (0,0)
    destination_node = (5, 5)
    width = 0
    height = 0

    def __init__(self, current_node=(0,0), destination_node=(5,5), inactive=[], width=6, height=6):
        self.current_node = current_node
        self.destination_node = destination_node
        self.inactive = inactive
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.closed_set = []                     # przjrzane
        self.open_set = [self.current_node]      # nie odwiedzone

    def resolve(self):
        while len(self.open_set):
            node = self.getClosest(self.destination_node)   # f

            self.open_set.remove(node)
            self.closed_set.append(node)

            if node == self.destination_node:
                return True, self.closed_set

            for neighbor in self.getNeighbors(node):
                if neighbor in self.closed_set or neighbor in self.open_set:
                    continue
                self.open_set.append(neighbor)

        return False, self.closed_set

    # The Euclidean Distance Heuristic
    # f, but its only h because each neighbor is in the same distance from current node
    def getClosest(self, node_start):
        min = math.inf
        node = None

        for node_dest in self.open_set:
            l = self.getDistance(node_start, node_dest)
            if (l < min):
                min = l
                node = node_dest

        return node

    def getDistance(self, node_start, node_dest):
        x = node_start[0] - node_dest[0]
        y = node_start[1] - node_dest[1]
        return math.sqrt(x * x + y * y)

    def getNeighbors(self, node):
        def isValid(node):
            return 0 <= node[0] < self.width and \
                   0 <= node[1] < self.height and \
                   node not in self.inactive

        neighbors = []
        if isValid((node[0]-1, node[1])):
            neighbors.append((node[0]-1, node[1]))

        if isValid((node[0]+1, node[1])):
            neighbors.append((node[0]+1, node[1]))

        if isValid((node[0], node[1]-1)):
            neighbors.append((node[0], node[1]-1))

        if isValid((node[0], node[1]+1)):
            neighbors.append((node[0], node[1]+1))

        return neighbors


test = AStar()
print(test.resolve())