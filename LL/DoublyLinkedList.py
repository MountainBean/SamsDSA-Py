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
