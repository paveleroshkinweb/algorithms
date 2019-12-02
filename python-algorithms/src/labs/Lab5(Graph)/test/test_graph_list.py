import unittest
from graph_list import Graph
import utils


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

    def test_get_all_vertices(self):
        graph = Graph()
        self.assertSequenceEqual([], graph.get_all_vertices())
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_edge(4, 5)
        self.assertSetEqual(set([1, 2, 3, 4, 5]), set(graph.get_all_vertices()))

    def test_get_vertex_environment(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 4)
        self.assertSequenceEqual([2, 3], graph.get_vertex_environment(1))
        self.assertSequenceEqual([1, 4], graph.get_vertex_environment(2))
        self.assertEqual(None, graph.get_vertex_environment(100))

    def test_is_adjacent_vertices(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(3, 4)
        self.assertTrue(graph.is_adjacent_vertices(1, 2))
        self.assertTrue(graph.is_adjacent_vertices(3, 4))
        self.assertFalse(graph.is_adjacent_vertices(1, 4))
        self.assertFalse(graph.is_adjacent_vertices(5, 10))

    def test_is_connected(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(2, 4)
        graph.add_edge(3, 4)
        self.assertTrue(utils.is_graph_connected(graph))
        graph.add_edge(5, 6)
        self.assertFalse(utils.is_graph_connected(graph))

    def test_is_bipartite(self):
        graph = Graph()
        self.assertTrue(utils.is_bipartite(graph))
        graph.add_vertices([1, 2, 3])
        self.assertTrue(utils.is_bipartite(graph))
        graph.add_edge(1, 2)
        graph.add_edge(3, 4)
        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 5)
        graph.add_edge(5, 6)
        self.assertTrue(utils.is_bipartite(graph))
        graph.add_edge(5, 6)
        graph.add_edge(1, 5)
        self.assertTrue(utils.is_bipartite(graph))

    # def test_find_euler_path(self):
    #     node_list = [chr(ord('a') + i) for i in range(6)]
    #     correct_answers = ['a', 'b', 'c', 'd', 'f', 'c', 'e', 'a', 'd', 'e', 'f', 'a']
    #     graph = Graph()
    #     graph.add_vertices(node_list)
    #     graph.add_edge(node_list[0], node_list[1])
    #     graph.add_edge(node_list[0], node_list[3])
    #     graph.add_edge(node_list[0], node_list[4])
    #     graph.add_edge(node_list[0], node_list[5])
    #
    #     graph.add_edge(node_list[4], node_list[2])
    #     graph.add_edge(node_list[4], node_list[3])
    #     graph.add_edge(node_list[4], node_list[5])
    #
    #     graph.add_edge(node_list[2], node_list[1])
    #     graph.add_edge(node_list[2], node_list[3])
    #     graph.add_edge(node_list[2], node_list[5])
    #
    #     graph.add_edge(node_list[5], node_list[3])
    #
    #     path = utils.find_euler_path(graph)
    #
    #     self.assertSequenceEqual(path, correct_answers)
    #     # for node, correct_answer in zip(path, correct_answers):
    #     #     self.assertEqual(node, correct_answers)
    #
    #     path = graph.euler_cycle()


if __name__ == 'main':
    unittest.main()
