"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node. Implement an
XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to get_pointer and dereference_pointer functions that converts
between nodes and memory addresses.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.both = id(data)


class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.both = get_pointer(node) ^ self.tail.both
            node.both = get_pointer(self.tail)
            self.tail = node

    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = get_pointer(node)
                node = dereference_pointer(next_id)
        return node
