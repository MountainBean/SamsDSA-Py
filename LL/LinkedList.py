class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"({self.value})->"

    def __repr__(self) -> str:
        return f"({self.value})->{id(self.next)}"


class LinkedList:
    """_summary_
    """

    def __init__(self, firstValue) -> None:
        """
        Contructor takes a value and puts it in the first node of the linked list

        Args:
            firstValue (object): this can be an integersfor simple examples 
            but through the magic of Python, this can be any object.
        """
        new_node = Node(firstValue)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self) -> str:
        temp = self.head
        out = ""
        while temp is not None:
            out += str(temp)
            temp = temp.next
        return out

    def append(self, value) -> bool:
        """
        appends a given value to the end of the linked list. Moves the tail 
        pointer to the end of the list

        Args:
            value (object): this can be an integersfor simple examples 
            but through the magic of Python, this can be any object.

        Returns:
            bool: Return True when successful
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

    def prepend(self, value) -> bool:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        loc = 0
        while loc != index:
            temp = temp.next
            loc += 1
        return temp

    def set_value(self, index, value) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value) -> bool:
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
