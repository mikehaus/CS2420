"""
P8 - Graph ADT CS2420
Mike Hollingshaus
"""

class Graph():
    """
    Graph ADT Class Definition
    """
    def __init__(self):
        """
        Constructor for Graph
        """
        self.vertices = []

    def add_vertex(self, label):
        """
        Add a vertex with a specified label.
        Return the graph.
        Label must be a string or raise ValueError.
        """
        try:
            str(label)
        except:
            raise ValueError('@param label not of type string')
        
        return self.graph

    def add_edge(self, src, dest, w):
        """
        Add an edge from vertex src to vertex dest with weight w.
        Return the graph.
        Validate:
        @param src, 
        @param dest,
        @param w.
        Raise ValueError if not valid.
        """
        return self.graph

    def get_weight(self, src, dest) -> float:
        """
        @type float
        Return the weight on edge src-dest
        (math.inf if no path exists,
        raise ValueError if src or dest not added to graph).
        """
        return weight.format(float)

   def dfs(self, starting_vertex):
       """
       Return a generator for traversing the graph
       in depth-first order starting fro the specified vertex.
       Raise a ValueError if the vertex doesn't exist
       """

    def bfs(self, starting_vertex):
        """
        Return a generator for traversing the graph
        in breadth-first order starting fro the specified vertex.
        Raise a ValueError if the vertex doesn't exist
        """

    def dijkstra_shortest_path(self, src, dest) -> list:
        """
        @type list
        Return a tuple (path length, the list of the vertices
        on the path from dest back to src).
        If no path exists, return the tuple (math.inf, empty list).
        """

    def dijkstra_shortest_path(self, src) -> dict:
        """
        Return a dictionary of the shortest weighted path
        between src and all other vertices using Dijkstra's
        shortest path algorithm.
        In the dictionary, the key is the vertex label, the value
        is a tuple (path length, the list of vertices on the path
        from key back to src).
        """

    def __str__(self) -> str:
        """
        Produce a string representation of the graph that
        can be used with print().
        """