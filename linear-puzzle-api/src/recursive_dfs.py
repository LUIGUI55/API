def recursive_dfs(start_node, end_node, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start_node)
    visited.add(start_node)

    if start_node == end_node:
        return path

    for neighbor in get_neighbors(start_node):
        if neighbor not in visited:
            result = recursive_dfs(neighbor, end_node, path, visited)
            if result is not None:
                return result

    path.pop()
    return None

def get_neighbors(node):
    # For a linear puzzle, neighbors are the adjacent nodes
    neighbors = []
    if node > 0:  # Can move left
        neighbors.append(node - 1)
    if node < 3:  # Can move right (assuming a 4-element puzzle)
        neighbors.append(node + 1)
    return neighbors