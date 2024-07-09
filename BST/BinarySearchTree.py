from LL.Queue import Queue, Q_Node


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

    def r_contains(self, value: int) -> bool:
        """
        Recursively searches the binary tree for a given value.
        Calls the private recursive function __r_contains() at the root node.

        Args:
            value (int): Value to search for in the BST

        Returns:
            bool: True if value is in the BST
        """
        return self.__r_contains(self.root, value)

    def __r_contains(self, node, value):
        if node == None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            # calls itself on the left (smaller) child node
            return self.__r_contains(node.left, value)
        if value > node.value:
            # calls itself on the right (larger) child node
            return self.__r_contains(node.right, value)

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_insert(self, node, value):
        if node == None:
            return Node(value)
        if value < node.value:
            node.left = self.__r_insert(node.left, value)
        if value > node.value:
            node.right = self.__r_insert(node.right, value)
        return node

    def min_value(self, current_node: Node) -> int:
        """
        O(log n)
        Minimum value in the tree from the current node as the root.
        As this is a BST, this just means we take the left pointer 
        until there are no left pointers.

        Args:
            current_node (Node): A node to begin the search for the 
            lowest-value node.

        Returns:
            int: vlaue of the minimum-value node in the tree
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        elif value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        if value == current_node.value:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.right is None:
                return current_node.left
            elif current_node.left is None:
                return current_node.right
            else:
                current_node.value = self.min_value(current_node.right)
                self.__delete_node(current_node.right, current_node.value)
        return current_node

    def BFS(self):
        current_node = self.root
        queue = Queue()
        results = []
        queue.enqueue(current_node)
        while queue.length > 0:
            current_node = queue.dequeue().value
            results.append(current_node.value)
            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)

        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return results
