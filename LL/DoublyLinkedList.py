# DoublyLinkedList implementation in Python using objects as Nodes
#
# All credit for this code goes to Scott Barrett and his Udemy course:
# "Python Data Structures & Algorithms + LEETCODE Exercises"
#
# I've writen this code following Barrett's guidance in his course and
# added it into a module and added docstrings as a learning aide to
# help me remember what I've learned


class Double_Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"({self.value})->{id(self.next)}"


class DoublyLinkedList:
    """
    Doubly Linked List implemented using Python Classes. 
    Class methods include docstrings like this one that will provide info on the
    worst-case time complexity of the method (Big-O notation) where 'n' is the
    current length of the LinkedList object.
    """

    def __init__(self, firstValue) -> None:
        """
        O(1)
        Contructor takes a value and puts it in the first node of the linked list

        Args:
            firstValue (object): this can be an integers for simple examples 
            but through the magic of *Dynamic typing* (derogatory), this can be 
            any object.
        """
        new_node = Double_Node(firstValue)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self) -> str:
        """
        O(n)
        builds the string representation of the DLL

        Returns:
            str: A complete formatted string containing all Node values
        """
        temp = self.head
        out = ""
        while temp is not None:
            out += str(temp)
            temp = temp.next
        return out

    def append(self, value: object) -> bool:
        """
        O(1)
        links a given value to the end of the DoublyLinkedList.

        Args:
            value (object): Any object can be used but integers are expected for 
            demonstration purposes

        Returns:
            bool: True when successful
        """
        new_node = Double_Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Double_Node:
        """
        O(1)
        Removes the last node in the DoublyLinkedList.
        Unlike the singly LinkedList, The pop() method on the DoublyLinkedList is
        constant time complexity as there's no need to iterate through the list
        to find the new tail node.

        Returns:
            Double_Node: The removed Double_Node. None if list is empty.
        """
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = self.tail.prev      # This will be None if length == 1
        if self.length == 1:
            self.head = None
        else:
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value: object) -> bool:
        """
        O(1)
        links a given value to the front of the DoublyLinkedList.

        Args:
            value (object): Any object can be used but integers are expected for 
            demonstration purposes

        Returns:
            bool: True when successful
        """
        new_node = Double_Node(value)
        if self.length == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Double_Node:
        """
        O(1)
        Removes the last node in the DoublyLinkedList. 
        This is just the inverse of pop.

        Returns:
            Double_Node: The removed Double_Node. None if list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next      # This will be None if length == 1
        if self.length == 1:
            self.tail = None
        else:
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index: int) -> Double_Node:
        """
        O(n)
        Returns the Node at a given index.
        The worst case complexity is optimesed with a DoublyLinkedList as the list
        is iterated through from whichever end of the list is closest
        to the index. 

        Args:
            index (int): location of the desired Node

        Returns:
            Double_Node: The Node at the given index
        """
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index: int, value: object) -> bool:
        """
        O(n)
        Changes the value held by the Node at the given index to the given
        value. Uses the get() method.

        Args:
            index (int): The location of the Node that will be edited.
            value (object): The new Node value

        Returns:
            bool: True when successful.
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
