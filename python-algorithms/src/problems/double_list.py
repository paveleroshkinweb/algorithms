# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.head is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        node_prev = node.prev
        nodeToInsert.prev = node_prev
        if node_prev is None:
            self.head = nodeToInsert
        else:
            node_prev.next = nodeToInsert
        nodeToInsert.next = node
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return

        node_next = node.next
        if node_next is None:
            self.tail = nodeToInsert
            node.next = self.tail
        else:
            nodeToInsert.next = node_next
            node_next.prev = nodeToInsert

        nodeToInsert.prev = node
        node.next = nodeToInsert


    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        assert position >= 1
        current = self.head
        while current and position > 1:
            current = current.next
            position -= 1
        if current:
            self.insertBefore(current, nodeToInsert)


    def removeNodesWithValue(self, value):
        # Write your code here.
        current = self.head
        while current:
            new_current = current.next
            if current.value == value:
                self.remove(current)
            current = new_current


    def remove(self, node):
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node is self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node


    def containsNodeWithValue(self, value):
        # Write your code here.
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


l = DoublyLinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
l.setHead(n1)
l.insertAfter(n1, n2)
l.insertAfter(n2, n3)
l.insertAfter(n3, n4)
l.insertAfter(n4, n5)
l.insertAfter(n5, n6)
l.insertAfter(n6, n7)

# print(l.head.next.value)
l.insertAtPosition(1, Node(1))

print(l.head.value, l.tail.value)
print(l.head.next.next. value)

