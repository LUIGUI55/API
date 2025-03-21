def bfs(start_node, end_node):
    from collections import deque

    # Queue for BFS
    queue = deque([start_node])
    # To keep track of visited nodes
    visited = set()
    # To store the path
    parent = {start_node: None}

    while queue:
        current_node = queue.popleft()

        # Check if we reached the end node
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]  # Return reversed path

        # Mark the current node as visited
        visited.add(current_node)

        # Generate possible moves (assuming a linear puzzle)
        for move in generate_moves(current_node):
            if move not in visited and move not in queue:
                queue.append(move)
                parent[move] = current_node

    return None  # Return None if no path is found

def generate_moves(node):
    # Assuming a linear puzzle with nodes represented as integers
    moves = []
    if node > 0:  # Can move left
        moves.append(node - 1)
    if node < 3:  # Can move right (for a 4-element puzzle)
        moves.append(node + 1)
    return moves