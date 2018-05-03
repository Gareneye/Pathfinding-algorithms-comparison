def createG(inactive=[], width=5, height=5):
    Adj = {}
    V = {}

    # Tworze liste sasiedztwa
    for x in range(0, width):
        for y in range(0, height):
            node = (x, y)
            list = []

            if node in inactive:
                continue

            V[node] = {}

            if x-1 >= 0 and (x-1, y) not in inactive:
                list.append((x-1, y))

            if x+1 < width and (x+1, y) not in inactive:
                list.append((x+1, y))

            if y-1 >= 0 and (x, y-1) not in inactive:
                list.append((x, y-1))

            if y+1 < width and (x, y+1) not in inactive:
                list.append((x, y+1))

            Adj[node] = list

    return V, Adj