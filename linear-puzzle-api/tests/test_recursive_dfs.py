import unittest
from src.recursive_dfs import recursive_dfs

class TestRecursiveDFS(unittest.TestCase):

    def test_solution_found(self):
        start_node = [1, 2, 3, 0]
        end_node = [0, 1, 2, 3]
        expected_solution = [[1, 2, 3, 0], [0, 1, 2, 3]]  # Example expected path
        self.assertEqual(recursive_dfs(start_node, end_node), expected_solution)

    def test_no_solution(self):
        start_node = [1, 2, 3, 0]
        end_node = [1, 0, 2, 3]
        expected_solution = None  # Example expected result when no solution exists
        self.assertEqual(recursive_dfs(start_node, end_node), expected_solution)

    def test_edge_case(self):
        start_node = [0, 1, 2, 3]
        end_node = [0, 1, 2, 3]
        expected_solution = [[0, 1, 2, 3]]  # Starting and ending at the same node
        self.assertEqual(recursive_dfs(start_node, end_node), expected_solution)

if __name__ == '__main__':
    unittest.main()