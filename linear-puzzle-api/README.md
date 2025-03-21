# Linear Puzzle API

This project provides a RESTful API for solving a linear puzzle with 4 elements using three different search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and Recursive Depth-First Search (DFS). Users can input the initial and final states of the puzzle, and the API will return the solution path.

## Project Structure

```
linear-puzzle-api
├── src
│   ├── app.py               # Entry point of the API
│   ├── bfs.py               # BFS algorithm implementation
│   ├── dfs.py               # DFS algorithm implementation
│   ├── recursive_dfs.py     # Recursive DFS algorithm implementation
│   └── utils
│       └── __init__.py      # Utility functions
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── tests
    ├── test_bfs.py          # Unit tests for BFS
    ├── test_dfs.py          # Unit tests for DFS
    └── test_recursive_dfs.py # Unit tests for Recursive DFS
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/linear-puzzle-api.git
   cd linear-puzzle-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```
   python src/app.py
   ```

2. Use the following endpoints to solve the puzzle:

   - **BFS Endpoint**
     ```
     POST /solve/bfs
     {
       "start_node": "initial_state",
       "end_node": "final_state"
     }
     ```

   - **DFS Endpoint**
     ```
     POST /solve/dfs
     {
       "start_node": "initial_state",
       "end_node": "final_state"
     }
     ```

   - **Recursive DFS Endpoint**
     ```
     POST /solve/recursive_dfs
     {
       "start_node": "initial_state",
       "end_node": "final_state"
     }
     ```

## Example

To solve a puzzle from state `1 2 3 4` to `4 3 2 1` using BFS, you would send a POST request to `/solve/bfs` with the appropriate JSON body.

## Running Tests

To run the unit tests for the algorithms, use the following command:
```
pytest tests/
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.