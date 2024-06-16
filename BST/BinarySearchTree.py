class Node:
    def __init__(self, value: int) -> None:
        """
        A BST Node has two pointers. The left pointer must point to a Node with a value less
        than the value of the current Node. The right must point to a Node with a value greater
        than the value of the current Node.

        Args:
            value (int): an int value for demonstartion purposes
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        # This is dumb
        return f"{self.value}\n↙ ↘\n{id(self.left)}|{id(self.right)}"


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> bool:
        """
        O(log n) Divide and conquer
        adds a new node and puts it at the correct location in the Binary Tree.

        Args:
            value (int): int value for purpose of demonstration.

        Returns:
            bool: True when successful
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value) -> bool:
        """
        O(log n)
        Searches the BST for a given value. 

        Args:
            value (int): int value to search for

        Returns:
            bool: True if the given value is in the BST
        """
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
