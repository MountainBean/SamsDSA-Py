class Q_Node:
    def __init__(self, value: object) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"({self.value})->{self.next}"


class Queue:
    """
    Queue class, a LinkeedList that only takes from the front of
    the queue and always appends to the end.
    """

    def __init__(self, value=None) -> None:
        if value is not None:
            new_node = Q_Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.first = None
            self.last = None
            self.length = 0

    def __str__(self) -> str:
        temp = self.first
        out = f""
        while temp is not None:
            out += str(temp)
            temp = temp.next
        return out

    def enqueue(self, value: object) -> bool:
        """
        O(1)
        adds an item to the end of the queue

        Args:
            value (object): value to give the new node

        Returns:
            bool: True when successful
        """
        new_node = Q_Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self) -> Q_Node:
        """
        O(1)
        removes the item from the front of the queue.

        Returns:
            Q_Node: Item removed from the front of the list
        """
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.last = None
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp
