class Node:
    def __init__(self, number):
        self.number = number
        self.next = []
        self.previous = 0
        self.final_next = []


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
    d = []
    additional_d = []
    for i in range(len(nodes)):
        d.append(32768)
        additional_d.append(32768)
    d[0] = 0
    used = [nodes[0]]
    while len(used) != len(nodes):
        current = used[len(used)-1]
        for dist in current.next:
            if int(dist[1]) < d[dist[0].number] and dist[0] not in used:
                d[dist[0].number] = int(dist[1])
                additional_d[dist[0].number] = int(dist[1])
                dist[0].previous = current
        min = 32768
        appended_node = 0
        for i in range(len(additional_d)):
            if additional_d[i] < min:
                min = additional_d[i]
                appended_node = i
        used.append(nodes[appended_node])
        additional_d[appended_node] = 32768
    return sum(d)


def print_answer(nodes, t):
    for n in nodes:
        if n.previous != 0:
            n.final_next.append(n.previous.number)
            n.previous.final_next.append(n.number)
    with open("output.txt", "w") as file:
        for node in nodes:
            node.final_next.sort()
            node.final_next.append(-1)
            for n in node.final_next:
                file.write(str(n + 1) + " ")
            file.write("\n")
        file.write(str(t))


def main():
    read_data()


if __name__ == '__main__':
    main()
