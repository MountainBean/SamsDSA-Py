class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"({self.value})->{id(self.next)}"


class LinkedList:
    """
    Simple implementation of a Linked List using Python Classes. 
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
        new_node = Node(firstValue)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self) -> str:
        """
        O(n)
        builds the string representation of the LL

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
        appends a given value to the end of the linked list. Moves the tail 
        pointer to the end of the list

        Args:
            value (object): this can be an integers for simple examples 
            but through the magic of *Dynamic typing* (derogatory), this can be 
            any object.

        Returns:
            bool: True when successful
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node:
        """
        O(n)
        removes the last item in the LinkedList.
        Iterates down the LinkedList to find the 2nd-to-last Node, disconnects 
        it's pointer from the tail node, moves the tail pointer to the new
        tail Node, and then returns the old tail Node.

        Returns:
            Node: The Tail Node of the LinkedList, None if LinkedList is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value: object) -> bool:
        """
        O(1)
        Adds a given value to the front of the LinkedList.

        Args:
            value (object): this can be an integers for simple examples 
            but through the magic of *Dynamic typing* (derogatory), this can be 
            any object.

        Returns:
            bool: True when successful
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node:
        """
        O(1)
        Removes the first node from the LinkedList
        Changes the head Node next pointer to none, moves the head node pointer
        to the next Node along, and returns the removed Node.


        Returns:
            Node: The removed Node from the front of the LinkedList
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index: int) -> Node:
        """
        O(n)
        Finds the Node at the given index in the LinkedList. 
        Iterates down the LinkedList until it reached the given index. Returns
        the node without removing it.

        Args:
            index (int): The location to query in the LinkedList. Must be 
            a positive and less than the length of the list.

        Returns:
            Node: The Node objecct at the given index in the LinkedList.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        loc = 0
        while loc != index:
            temp = temp.next
            loc += 1
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
        LinkedList, shifting the following Nodes down by one.

        Args:
            index (int): The location in the LinkedList to insert the given value
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
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index: int) -> Node:
        """
        O(n)
        Removes the Node from the given index in the LinkedList

        Args:
            index (int): The location of the Node to be removed

        Returns:
            Node: The removed Node. None if LL is empty
        """
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self) -> None:
        """
        (O)n
        Iterates down the LinkedList, reversing the direction of the pointers
        so the LinkedList is reversed and the head and tail pointers are
        swapped
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next           # Initialise before while loop
        while temp is not None:
            after = temp.next       # 1st iteration won't change
            temp.next = before
            before = temp
            temp = after
