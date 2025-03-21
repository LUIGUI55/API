def dfs(start_node, end_node):
    stack = [start_node]
    visited = set()
    parent = {start_node: None}

    while stack:
        current_node = stack.pop()

        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]  # Return reversed path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in get_neighbors(current_node):
                if neighbor not in visited:
                    stack.append(neighbor)
                    parent[neighbor] = current_node

    return None  # Return None if no path is found

def get_neighbors(node):
    # For a linear puzzle, neighbors are the adjacent nodes
    neighbors = []
    if node > 0:  # Can move left
        neighbors.append(node - 1)
    if node < 3:  # Can move right (assuming a 4-element puzzle)
        neighbors.append(node + 1)
    return neighbors