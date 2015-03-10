nodes = {}


def decompose(node_name, calling_node_name=None):
    total = 1
    num_edges_removed = 0

    for child_name in nodes[node_name]:
        if child_name != calling_node_name:
            result = decompose(child_name, node_name)
            num_child_nodes = result[0]
            num_edges_removed += result[1]
            total += num_child_nodes

            if num_child_nodes % 2 == 0:
                num_edges_removed += 1

    return total, num_edges_removed

if __name__ == '__main__':
    num_verticies, num_edges = map(int, raw_input().split(' '))

    for i in xrange(num_edges):
        u, v = map(str, raw_input().split(' '))

        nodes.setdefault(u, [])
        nodes.setdefault(v, [])

        nodes[v].append(u)
        nodes[u].append(v)

    # Decompose the last node (last node not significant)
    print decompose(u)[1]

