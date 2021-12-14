def visit(node, nodes, path, paths):
    # Make a copy of the path and add the current node to it
    path = path.copy()
    path.append(node)

    # Determine the states of the base cases
    multiple_visited_small_nodes = len(set([i for i in path if path.count(i) > 1 and i.islower()]))
    is_small_third_visit = nodes[node]["size"] == "small" and path.count(node) == 3
    is_start_second_visit = path.count("start") == 2
    is_end = node == "end"

    # Continue travelling if none of the base cases are met
    if multiple_visited_small_nodes < 2 and not is_small_third_visit and not is_start_second_visit and not is_end:
        for conn in nodes[node]["conn"]:
            paths = visit(conn, nodes, path, paths)

    # If the current node is the end, save the path
    elif is_end:
        paths.append(path)

    return paths


if __name__ == "__main__":

    nodes = {}

    # Read input
    with open("input.txt", "r") as f:
        for line in f.readlines():
            # Take both nodes from the line, ensure they are stored as nodes with their size, and add the connection
            a, b = line.strip().split("-")

            size = "big" if a.isupper() else "small"
            nodes.setdefault(a, {"size": size, "conn": []})

            size = "big" if b.isupper() else "small"
            nodes.setdefault(b, {"size": size, "conn": []})

            nodes[a]["conn"].append(b)
            nodes[b]["conn"].append(a)

    # Travel through the nodes recursively, starting at "start"
    paths = visit("start", nodes, [], [])

    print(len(paths))
