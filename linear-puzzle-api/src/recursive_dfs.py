def recursive_dfs(start_node, end_node, path=None):
    if path is None:
        path = []

    path.append(start_node)

    if start_node == end_node:
        return path

    for neighbor in get_neighbors(start_node):
        if neighbor not in path:
            result = recursive_dfs(neighbor, end_node, path)
            if result is not None:
                return result

    path.pop()
    return None

def get_neighbors(node):
    # This function should return the valid neighbors of the node
    # For a linear puzzle, neighbors can be defined based on the puzzle's rules
    neighbors = []
    if node > 0:  # Assuming nodes are indexed from 0
        neighbors.append(node - 1)  # Move left
    if node < 3:  # Assuming a linear puzzle of 4 elements (0 to 3)
        neighbors.append(node + 1)  # Move right
    return neighbors