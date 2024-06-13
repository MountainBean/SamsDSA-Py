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

    def insert(self, index: int, value: object) -> bool:
        """
        O(n)
        Creates a new node and places it at the given index in the
        DoublyLinkedList, shifting the following Nodes down by one.

        Args:
            index (int): The location in the DoublyLinkedList to insert the given value
            value (object): The new Node value

        Returns:
            bool: True when successful
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Double_Node(value)
        before = self.get(index - 1)
        after = before.next
        after.prev = new_node
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        self.length += 1
        return True

    def remove(self, index: int) -> Double_Node:
        """
        O(n)
        Removes the DoubleNode from the given index in the DoublyLinkedList

        Args:
            index (int): The location of the Double_Node to be removed

        Returns:
            Double_Node: The removed Node. None if DLL is empty
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def swap_first_last(self) -> None:
        """
        O(1)
        Uses tuples to exchange the values of the Nodes, rather than the pointers.
        This question was a mislead. Sometimes just changing the values is easiest.
        """
        # 1. Check if the doubly linked list is empty or has only one node.
        # If so, there's nothing to swap, hence exit the function early.
        if self.head is None or self.head == self.tail:
            return

        # 2. If the list has more than one node, swap the values of the
        # head (first node) and tail (last node).
        # Note: We're only exchanging the data stored in the nodes,
        # rather than altering the structure of the linked list itself.
        self.head.value, self.tail.value = self.tail.value, self.head.value

    def reverse(self) -> None:
        """
        (O)n
        Iterates down the DoublyLinkedList, reversing the direction of the pointers
        so the DoublyLinkedList is reversed and the head and tail pointers are
        swapped
        """
        if self.length <= 1:
            return
        current = self.head
        for _ in range(self.length):
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def is_palindrome(self):
        front = self.head
        back = self.tail
        i = 0                               # This could also have been done in a
        while i < self.length/2:            # for loop with the "//" operator
            if front.value != back.value:
                return False
            front = front.next
            back = back.prev
            i += 1
        return True
