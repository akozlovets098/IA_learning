class Node:
    __slots__ = 'value', 'next_node'

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList:

    def __init__(self, head):
        self.head = head

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next_node

    def __str__(self):
        return ' -> '.join(map(str, self))


head = Node(1)
head.next_node = Node(2)
head.next_node.next_node = Node(3)
head.next_node.next_node.next_node = Node(4)

linked_list = LinkedList(head)

print('Original:', linked_list)

"""
def reverse(head):
    head_new = Node(head.value)
    current_node = head.next_node
    while current_node:
        node_new = Node(current_node.value)
        node_new.next_node = head_new
        head_new = node_new
        current_node = current_node.next_node
    return head_new
"""


def reverse(head):
    tail = None
    current_node = head
    while True:
        head_new = current_node.next_node
        current_node.next_node = tail
        tail = current_node
        if head_new is None:
            break
        current_node = head_new
    return current_node


reversed_list = LinkedList(reverse(head))

print('Reversed:', reversed_list)
