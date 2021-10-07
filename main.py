class Node:
    def __init__(self, number):
        self.number = number
        self.color = 0
        self.next = []
        self.visited = False
        self.min_next = []


def read_data():
    nodes = []
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line)
            count_nodes = int(data[0])
    data = data[1:]
    for i in range(count_nodes):
        nodes.append(Node(i))
    for i in range(count_nodes):
        count = -1
        nodes_numbers = data[i][:-1].split(" ")
        if i == count_nodes - 1:
            nodes_numbers = data[i].split(" ")
        for j in nodes_numbers:
            count += 1
            nodes[i].next.append((nodes[count], int(j)))
    t = min_ost(nodes)
    print_answer(nodes, t)


def min_ost(nodes):
    t = 0
    used = [nodes[0].number]
    while len(used) != len(nodes):
        m = 32768
        n = 0
        current = 0
        for node in used:
            for dist in nodes[node].next:
                if int(dist[1]) < m and dist[0].number not in used:
                    m = int(dist[1])
                    n = dist[0]
                    current = node
        n.min_next.append(current)
        nodes[current].min_next.append(n.number)
        t += m
        used.append(n.number)
    return t


def print_answer(nodes, t):
    with open("output.txt", "w") as file:
        for node in nodes:
            node.min_next.sort()
            node.min_next.append(-1)
            for n in node.min_next:
                file.write(str(n + 1) + " ")
            file.write("\n")
        file.write(str(t))


def main():
    read_data()


if __name__ == '__main__':
    main()
