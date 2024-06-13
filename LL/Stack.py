class Stack_Node:
    def __init__(self, value: object) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"({self.value})\n ↓\n{self.next}"


class Stack:
    def __init__(self, value: object) -> None:
        new_node = Stack_Node(value)
        self.top = new_node
        self.height = 1

    def __str__(self) -> str:
        temp = self.top
        out = f""
        while temp is not None:
            out += f"{temp}\n"
            temp = temp.next
        return out

    def push(self, value: object) -> bool:
        new_node = Stack_Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self) -> Stack_Node:
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
