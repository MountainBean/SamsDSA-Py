class Q_Node:
    def __init__(self, value: object) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"({self.value})->{self.next}"


class Queue:
    def __init__(self, value) -> None:
        new_node = Q_Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def __str__(self) -> str:
        temp = self.first
        out = f""
        while temp is not None:
            out += str(temp)
            temp = temp.next
        return out

    def enqueue(self, value: object) -> bool:
        new_node = Q_Node
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            return True

    def dequeue(self) -> Q_Node:
        if self.length == 0:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        return temp
