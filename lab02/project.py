from typing import Any


# making representation of node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# making representation of linked list
class LinkedList:
    # initializing list
    def __init__(self):
        self.head = None
        self.tail = None

    # making print(_list) will actually print what we want, not object with address
    def __str__(self):
        out = ""
        node = self.head
        while node != None:
            if node.next != None:
                out += str(node.value) + " -> "
            else:
                out += str(node.value)
            node = node.next
        return out

    # returning length of list
    def __len__(self):
        length = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            length += 1
        return length

    # placing new node at the beginning
    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node

    # placing new node at the end
    def append(self, value: Any) -> None:
        if self.head != None:
            new_node = self.tail
            new_node.next = Node(value)
            self.tail = new_node.next
        else:
            self.push(value)

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
        while last.next.next != None:
            last = last.next
        last.next = None
        self.tail = last
        return temp.value

    # removing given node's.next
    def remove(self, after: Node) -> Any:
        new_node = after.next.next
        after.next = new_node


# making representation of stack
class Stack:
    # implementing linked list
    _storage: LinkedList

    # initializing stack
    def __init__(self):
        self._storage = LinkedList()

    # making print(stack) will actually print what we want, not object with address
    def __str__(self):
        temp = self._storage.head.next
        out = str(self._storage.head.value)
        while temp != None:
            out += '\n' + str(temp.value)
            temp = temp.next
        return out

    # returning length of stack
    def __len__(self):
        return len(self._storage)

    # placing new item at the top of the stack
    def push(self, element: Any) -> None:
        self._storage.append(element)

    # returning and deleting item from the top of the stack
    def pop(self) -> Any:
        return self._storage.remove_last()


class Queue:
    _storage: LinkedList()

    # initializing queue
    def __init__(self):
        self._storage = LinkedList()

    # returning length of queue
    def __len__(self):
        return len(self._storage)

    # making print(queue) will actually print what we want, not object with address
    def __str__(self):
        temp = self._storage.head.next
        out = str(self._storage.head.value)
        while temp != None:
            out += ', ' + str(temp.value)
            temp = temp.next
        return out

    # returning value of first item in queue
    def peek(self) -> Any:
        return self._storage.head.value

    # placing new item at the end of queue
    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    # returning and deleting first item in queue
    def dequeue(self) -> None:
        return self._storage.pop()


# testing if list works
list_ = LinkedList()
assert list_.head == None

# # testing if push works
list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'

# testing if append works
list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'

# testing if insert works
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

# testing if pop works
first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element
assert str(list_) == '1 -> 5 -> 9 -> 10'

# testing if remove_last works
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

# testing if remove works
second_node = list_.node(at=1)
list_.remove(second_node)
assert str(list_) == '1 -> 5'

# testing if stack works
stack = Stack()
assert len(stack) == 0

# testing if push works
stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3

# testing if pop works
top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2

# testing if queue works
queue = Queue()
assert len(queue) == 0

# testing if enqueue works
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

# testing if dequeue works
client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2

print(list_)
print('\n')
print(stack)
print('\n')
print(queue)
