class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, data):
        self.children.append(Node(data))


class StrictNode:
    def __init__(self, data):
        self.left_child = None
        self.middle_child = None
        self.right_child = None
        self.data = data


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_data(self, data):
        if data < self.data and self.left_child:
            self.left_child.insert_data(data)
        elif data < self.data:
            self.left_child = BSTNode(data)
        elif data > self.data and self.right_child:
            self.right_child.insert_data(data)
        else:
            self.right_child = BSTNode(data)

    def find(self, value):
        if self.data == value:
            return self
        elif not self.left_child and not self.right_child:
            return None
        elif value < self.data:
            return self.left_child.find(value)
        else:
            return self.right_child.find(value)

    def minimum(self):
        if not self.left_child:
            return self
        else:
            return self.left_child.minimum()


def bst_traverse_inorder(root: BSTNode, callback):
    if root is not None:
        bst_traverse_inorder(root.left_child, callback)
        callback(root)
        bst_traverse_inorder(root.right_child, callback)


def traverse_preorder(root: StrictNode, callback):
    if root is not None:
        callback(root)
        traverse_preorder(root.left_child, callback)
        traverse_preorder(root.middle_child, callback)
        traverse_preorder(root.right_child, callback)


def traverse_inorder(root: StrictNode, callback):
    if root is not None:
        traverse_inorder(root.left_child, callback)
        callback(root)
        traverse_inorder(root.middle_child, callback)
        traverse_inorder(root.right_child, callback)


def traverse_postorder(root: StrictNode, callback):
    if root is not None:
        traverse_postorder(root.left_child, callback)
        traverse_postorder(root.middle_child, callback)
        traverse_postorder(root.right_child, callback)
        callback(root)


def count_leaves(root: StrictNode):
    if root is None:
        return 0

    if root.left_child is None and root.middle_child is None and root.right_child is None:
        return 1
    else:
        return count_leaves(root.left_child) + count_leaves(root.middle_child) + count_leaves(root.right_child)


def node_depth(root: StrictNode, node: StrictNode, level: int = 0):
    if root == node:
        return level

    if root is None:
        return -1

    left_sub_level = node_depth(root.left_child, node, level + 1)
    if left_sub_level != -1:
        return left_sub_level

    middle_sub_level = node_depth(root.middle_child, node, level + 1)
    if middle_sub_level != -1:
        return middle_sub_level

    right_sub_level = node_depth(root.right_child, node, level + 1)
    if right_sub_level != -1:
        return right_sub_level

    return -1


class Tree:
    def __init__(self, root: Node = None):
        self.root = root

    def traverse_breadth_first(self, callback):
        nodes = [self.root]

        while nodes:
            if nodes[0].children:
                nodes.extend(nodes[0].children)

            callback(nodes.pop(0))

    def traverse_depth_first(self, callback):
        nodes = [self.root]

        while nodes:
            callback(nodes[0])

            if nodes[0].children:
                nodes[0:0] = nodes[0].children

            nodes.pop(0)


class BST:
    def __init__(self, *args):
        self.root: BSTNode = BSTNode(args[0])

        for data in args[1:]:
            self.insert_data(data)

    def insert_data(self, data):
        self.root.insert_data(data)

    def traverse(self, callback):
        bst_traverse_inorder(self.root, callback)

    def find(self, value):
        return self.root.find(value)

    def minimum(self):
        return self.root.minimum()
