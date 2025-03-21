import unittest
from src.dfs import dfs

class TestDFS(unittest.TestCase):

    def test_dfs_solution(self):
        # Test case where the path exists
        start_node = 1
        end_node = 4
        expected_path = [1, 2, 3, 4]  # Example expected path
        self.assertEqual(dfs(start_node, end_node), expected_path)

    def test_dfs_no_solution(self):
        # Test case where the path does not exist
        start_node = 1
        end_node = 5  # Assuming 5 is not reachable
        expected_path = []  # No path should be found
        self.assertEqual(dfs(start_node, end_node), expected_path)

    def test_dfs_same_node(self):
        # Test case where start and end nodes are the same
        start_node = 2
        end_node = 2
        expected_path = [2]  # Path should just be the start node
        self.assertEqual(dfs(start_node, end_node), expected_path)

if __name__ == '__main__':
    unittest.main()