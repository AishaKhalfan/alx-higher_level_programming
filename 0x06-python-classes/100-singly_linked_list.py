#!/usr/bin/python3
"""Defines Node module/
and SinglyLinkedList Module
"""


class Node():
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the data of the node"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the value of next node"""
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        """Sets the print behavior of the SinglyLinkedList object"""
        sll_str = ""
        node = self.__head

        if node is not None:
            while node is not None:
                sll_str += str(node.data) + '\n'
                node = node.next_node

        return sll_str[:-1]

    def sorted_insert(self, value):
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
