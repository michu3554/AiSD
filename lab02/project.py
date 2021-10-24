from typing import Any


# making representation of node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# making representation of linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # placing new node at the beginning
    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node

    # placing new node at the end
    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.tail = new_node

    # returning node on given position
    def node(self, at: int) -> Node:
        if len(self) > at:
            new_node = self.head
            for at in range(at):
                new_node = new_node.next
            return new_node

    # inserting new node right after given node
    def insert(self, value: Any, after: Node) -> None:
        new_node = Node
        new_node.value = value
        new_node.next = after.next
        after.next = new_node

    # removing list's first item and returning it
    def pop(self) -> Any:
        new_node = self.head
        self.head = new_node.next
        return new_node.value

    # removing list's last item and returning it
    def remove_last(self) -> Any:
        temp = self.tail
        last = self.head
        while (last.next.next != None):
            last = last.next
        last.next = None
        self.tail = last
        return temp.value

    # removing given node's.next
    def remove(self, after: Node) -> Any:
        new_node = after.next.next
        after.next = new_node

    # returning lenght of list
    def __len__(self):
        lenght = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            lenght += 1
        return lenght

    # printing items from list
    def print(self):
        out = ""
        node = self.head
        while node != None:
            if node.next != None:
                out += str(node.value) + " -> "
            else:
                out += str(node.value)
            node = node.next
        print(out)
        return out


# testing if list works
list_ = LinkedList()
assert list_.head == None

# # testing if push works
list_.push(1)
list_.push(0)
assert list_.print() == '0 -> 1'

# testing if append works
list_.append(9)
list_.append(10)
assert list_.print() == '0 -> 1 -> 9 -> 10'

# testing if insert works
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert list_.print() == '0 -> 1 -> 5 -> 9 -> 10'

# testing if pop works
first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element
assert list_.print() == '1 -> 5 -> 9 -> 10'

# testing if remove_last works
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element
assert list_.print() == '1 -> 5 -> 9'

# testing if remove works
second_node = list_.node(at=1)
list_.remove(second_node)
assert list_.print() == '1 -> 5'
