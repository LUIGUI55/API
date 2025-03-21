import unittest
from src.bfs import bfs

class TestBFS(unittest.TestCase):

    def test_bfs_solution(self):
        # Test case 1: Simple case
        start_node = 0
        end_node = 3
        expected_solution = [0, 1, 2, 3]  # Example expected path
        self.assertEqual(bfs(start_node, end_node), expected_solution)

    def test_bfs_no_solution(self):
        # Test case 2: No possible path
        start_node = 0
        end_node = 5
        expected_solution = []  # No path exists
        self.assertEqual(bfs(start_node, end_node), expected_solution)

    def test_bfs_same_node(self):
        # Test case 3: Start and end node are the same
        start_node = 2
        end_node = 2
        expected_solution = [2]  # Path is just the starting node
        self.assertEqual(bfs(start_node, end_node), expected_solution)

    def test_bfs_large_case(self):
        # Test case 4: Larger puzzle
        start_node = 0
        end_node = 15
        expected_solution = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Example expected path
        self.assertEqual(bfs(start_node, end_node), expected_solution)

if __name__ == '__main__':
    unittest.main()