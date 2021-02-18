"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# O(n)
def count_univals2(root):
    total_count, is_unival = helper(root)
    return total_count


def helper(root):
    if root == None:
        return (0, True)
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    is_unival = True
    if not is_left_unival or not is_right_unival:
        is_unival = False
    if root.left != None and root.left.data != root.data:
        is_unival = False
    if root.right != None and root.right.data != root.data:
        is_unival = False
    if is_unival:
        return (left_count + right_count + 1, True)
    else:
        return (left_count + right_count, False)


def is_unival(root):
    if root == None:
        return True

    if root.left != None and root.left.data != root.data:
        return False

    if root.right != None and root.right.data != root.data:
        return False

    if is_unival(root.left) and is_unival(root.right):
        return True

    return False


# O(n^2)
def count_univals(root):
    if root == None:
        return 0

    total_count = count_univals(root.left) + count_univals(root.right)
    if is_unival(root):
        total_count += 1
    return total_count


"""
            5 
          /   \ 
        4       5 
       /  \      \ 
      4    4      5 
"""
root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)

print(count_univals(root))

print(count_univals2(root))