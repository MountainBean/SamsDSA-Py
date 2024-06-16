class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2) -> bool:
        """
        Weirdly, the example in the tutorial used the keys() method in the if statement.
        seems unecesary and increases the complexity.

        Args:
            v1 (_type_): _description_
            v2 (_type_): _description_

        Returns:
            bool: True if successful
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                return False
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
