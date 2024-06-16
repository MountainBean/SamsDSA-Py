class Graph:
    """
    Python implementation of a graph using an adjacency list (dict) to keep track of 
    all vertices and edges. Edges are bi-directional and are recorded in both vertices'
    lists.
    """

    def __init__(self) -> None:
        """
        Vertices and edges are recorded in a dictionary. Vertices are the keys and their
        edges are values in lists for each key value.
        """
        self.adj_list = {}

    def add_vertex(self, vertex) -> bool:
        """
        O(n)
        adds a new empty vertex as a key in the dict. Like the Node of a linked list.
        Contains information.

        Args:
            vertex (object): value to store in the vertex

        Returns:
            bool: True when successful
        """
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2) -> bool:
        """
        Creates a bidirectional link between two vertices v1 and v2.
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

    def remove_edge(self, v1, v2) -> bool:
        """
        Removes edge from graph if present.

        Args:
            v1 (_type_): _description_
            v2 (_type_): _description_

        Returns:
            bool: True if successful
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                return False
            return True
        return False

    def remove_vertex(self, vertex) -> bool:
        """
        removes all adges connected to this vertex, then removes the vertex.


        Args:
            vertex (_type_): _description_

        Returns:
            bool: _description_
        """
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
