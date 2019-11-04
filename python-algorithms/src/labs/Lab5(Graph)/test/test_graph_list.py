import unittest
from graph_list import Graph


class TestGraph(unittest.TestCase):

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex(5)
        graph.add_vertex(1)
        graph.add_vertex(2)
        self.assertSequenceEqual([], graph.adjacency_list[5])
        self.assertSequenceEqual([], graph.adjacency_list[1])
        self.assertSequenceEqual([], graph.adjacency_list[2])
        with self.assertRaises(Exception):
            graph.add_vertex(5)

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex(5)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_edge(5, 1)
        graph.add_edge(5, 2)
        graph.add_edge(3, 4)
        self.assertSequenceEqual([1, 2], graph.adjacency_list[5])
        self.assertSequenceEqual([5], graph.adjacency_list[1])
        self.assertSequenceEqual([5], graph.adjacency_list[2])
        self.assertSequenceEqual([3], graph.adjacency_list[4])
        self.assertSequenceEqual([4], graph.adjacency_list[3])

    def test_remove_edge(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 4)
        graph.add_edge(3, 4)
        graph.remove_edge(1, 2)
        self.assertSequenceEqual([3, 4], graph.adjacency_list[1])
        self.assertSequenceEqual([4], graph.adjacency_list[2])
        graph.remove_edge(2, 4)
        self.assertSequenceEqual([], graph.adjacency_list[2])
        self.assertSequenceEqual([1, 3], graph.adjacency_list[4])
        with self.assertRaises(Exception):
            graph.remove_edge(5, 10)
            graph.remove_edge(1, 2)

    def test_get_all_vertexes(self):
        graph = Graph()
        self.assertSequenceEqual([], graph.get_all_vertexes())
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_edge(4, 5)
        self.assertSetEqual(set([1, 2, 3, 4, 5]), set(graph.get_all_vertexes()))

    def test_get_vertex_environment(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 4)
        self.assertSequenceEqual([2, 3], graph.get_vertex_environment(1))
        self.assertSequenceEqual([1, 4], graph.get_vertex_environment(2))
        self.assertEqual(None, graph.get_vertex_environment(100))

    def test_is_adjacent_vertexes(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(3, 4)
        self.assertTrue(graph.is_adjacent_vertexes(1, 2))
        self.assertTrue(graph.is_adjacent_vertexes(3, 4))
        self.assertFalse(graph.is_adjacent_vertexes(1, 4))
        self.assertFalse(graph.is_adjacent_vertexes(5, 10))


if __name__ == 'main':
    unittest.main()
