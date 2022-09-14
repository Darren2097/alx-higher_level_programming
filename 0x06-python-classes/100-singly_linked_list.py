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
                if new.data >= node.data and new.data <= node.next_node.data:
                    new.next_node = node.next_node
                    node.next_node = new
                    break
                elif new.data < node.data:
                    new.next_node = node
                    self.__head = new
                    break
                node = node.next_node
            if new.data >= node.data:
                node.next_node = new
            else:
                new.next_node = node
                self.__head = new

    def __str__(self):
        """string representation of singly linked list"""

        node = self.__head
        new_list = ''
        if node is None:
            new_list = ''
        elif node.next_node is None:
            new_list += str(node.data)
        else:
            while node.next_node:
                new_list += str(node.data) + '\n'
                node = node.next_node
                new_list += str(node.data)
        return new_list
