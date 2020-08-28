"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
 which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    string = []
    def serializer(node):
        if not node:
            string.append('?')
        else:
            string.append(str(node.val))
            serializer(node.left)
            serializer(node.right)
    serializer(root)
    return ",".join(string)

def deserialize(s):
    values = iter(s.split(','))
    def deserializer():
        val = next(values)
        if val == '?':
            return None
        else:
            node = Node(val)
            node.left = deserializer()
            node.right = deserializer()
            return node
    return deserializer()


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(node)).left.left.val == 'left.left')