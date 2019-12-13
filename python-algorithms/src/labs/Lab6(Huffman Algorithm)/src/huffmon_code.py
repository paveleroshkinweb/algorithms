import heapq
from node import Node


def huffman_code(input_str):
    char_nodes = count_chars(input_str)
    priority_queue = get_priority_queue(char_nodes)
    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        parent_node = Node((node1.value[0] + node2.value[0], None), left=node1, right=node2)
        node1.set_parent(parent_node)
        node2.set_parent(parent_node)
        heapq.heappush(priority_queue, parent_node)
    huffman_dictionary = create_huffman_dictionary(char_nodes)


def count_chars(input_str):
    chars_dictionary = {}
    for char in input_str:
        chars_dictionary[char] = (chars_dictionary.get(char) or 0) + 1
    nodes = []
    for key in chars_dictionary:
        nodes.append(Node((chars_dictionary[key], key)))
    return nodes


def get_priority_queue(char_nodes):
    heap = []
    for node in char_nodes:
        heapq.heappush(heap, node)
    return heap


def create_huffman_dictionary(char_nodes):
    huffman_dictionary = {}
    for node in char_nodes:
        temp = node
        byte_sequence = ''
        while temp.parent_node is not None:
            byte_sequence = ('0' if temp == temp.parent_node.left else '1') + byte_sequence
            temp = temp.parent_node
        huffman_dictionary[node.value[1]] = byte_sequence
    return huffman_dictionary


