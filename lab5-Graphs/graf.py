import sys


class Node:
    def __init__(self, index, cost, neighbors):
        self.index = index
        self.cost = cost
        self.distance = sys.maxsize
        self.neighbors = neighbors

    def new_distance(self, distance, previous_node):
        self.distance = distance
        self.previous_node = previous_node

    def __lt__(self, other):
        return self.distance < other.distance


def dijkstra(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    data = data.split("\n")
    width = len(data[0])
    height = len(data)
    nodes = []
    start_end = []
    for y in range(height):
        for x in range(width):
            neighbors = []
            if data[y][x] == "0":
                start_end.append(y * width + x)
            if y != 0:
                neighbors.append((y - 1) * width + x)
            if y != height - 1:
                neighbors.append((y + 1) * width + x)
            if x != 0:
                neighbors.append(y * width + x - 1)
            if x != width - 1:
                neighbors.append(y * width + x + 1)
            nodes.append(Node(y*width + x, int(data[y][x]), neighbors))
    unvisited = set(nodes)
    nodes[start_end[0]].new_distance(0, None)
    while len(unvisited) != 0:
        index = min(unvisited).index
        for neighbor in nodes[index].neighbors:
            neighbor = nodes[neighbor]
            distance = neighbor.cost + nodes[index].distance
            if distance < neighbor.distance:
                neighbor.new_distance(distance, index)
        unvisited.remove(nodes[index])
    output = [" "] * len(nodes)
    previous_node = start_end[1]
    while previous_node is not None:
        output[previous_node] = str(nodes[previous_node].cost)
        previous_node = nodes[previous_node].previous_node
    print(" ", "#" * width, " ")
    for y in range(height):
        print("#", "".join(output[y * width: (y + 1) * width]), "#")
    print(" ", "#" * width, " ")
