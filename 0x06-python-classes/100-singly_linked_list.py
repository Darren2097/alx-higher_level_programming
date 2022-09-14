#!/usr/bin/python3
"""Creates 2 classes named Node and SinglyLinkedList that defines a node of
a singly linked list"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """__init__ method that sets data and next_node of node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets the data of the node"""

        return self.__data

    @data.setter
    def data(self, value):
        """sets the data of the node"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """gets the next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next node"""

        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        """__init__ method defined for singly linked list"""

        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert method inserts a new Node into the correct sorted
        position in the list (increasing order)"""

        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            node = self.__head
            while node.next_node:
                if new.data >= node.data:
                    new.next_node = node.next_node
                    node.next_node = new
                    break
                elif new.data < node.data:
                    new.next_node = node
                    self.__head = new
                    break
                node = node.next_node

if __name__ == '__main__':
    sll = SinglyLinkedList()

    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
