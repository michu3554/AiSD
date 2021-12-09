from typing import Any, Callable, List


# making class for node
class BinaryNode:

    # initializing node
    def __init__(self, value: Any):
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.value = value

    # making print() actually prints value of node
    def __str__(self):
        return str(self.value)

    # checking if node is leaf
    def is_leaf(self):
        if self.left_child != None or self.right_child != None:
            return False
        return True

    # adding left child as a new node
    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)
        self.left_child.parent = self

    # adding right child as a new node
    def add_right_child(self, value):
        self.right_child = BinaryNode(value)
        self.right_child.parent = self

    # function will do transverse traversing over children
    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)

    # function will do reverse traversing over children
    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    # function will do longitudinal traversing over children
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)

    # making .show() printing the tree
    def show(self, level = 0):
        if self.right_child != None:
            self.right_child.show(level + 1)
        print(' ' * 5 * level + "->",self.value)
        if self.left_child != None:
            self.left_child.show(level + 1)

class BinaryTree:
    root: BinaryNode
    # initializing tree
    def __init__(self, value):
        self.root = BinaryNode(value)

    # transverse traversing starting in root
    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    # reverse traversing starting in root
    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    # longitudinal traversing starting in root
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)
    # showing the tree
    def show(self):
        self.root.show()

# making left_line function that prints left side of tree
def left_line(tree: BinaryTree) -> List[BinaryNode]:
    list = []
    root = tree.root
    while root != None:
        list.append(root.value)
        root = root.left_child
    return list

tree = BinaryTree(10)

tree.root.add_left_child(9)
tree.root.add_right_child(2)

tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)

tree.root.right_child.add_right_child(6)
tree.root.right_child.add_left_child(4)

assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False

tree.show()

print(left_line(tree))