"""
P8 - Graph ADT CS2420
Mike Hollingshaus
"""
import math

#------- Vertex Helper Class --------#
class Vertex:
    """
    Vertex Structure to hold vertex info
    """
    def __init__(self, label):
        """
        Vertex constructor
        @param label: string name of vertex
        @param adjacent: list of labels of adjacent vertices used for validation
        @param adjacent_vertices: list of tuples of adjacent vertices and weights
        """
        self.label = label
        self.adjacent = []
        self.adjacent_vertices = []

    def add_adjacent(self, adjacent, weight):
        """
        Adds adjacent vertex to self of weight weight
        """
        self.adjacent.append(adjacent.label)
        self.adjacent_vertices.append([adjacent.label, weight])

    def get_adjacent(self):
        """
        returns just list of adjacent labels
        """
        return self.adjacent

    def get_adjacent_vertices(self):
        """
        Returns all adjacent vertices
        """
        return self.adjacent_vertices

    def get_label(self):
        """
        Returns label of vertex
        """
        return self.label

    def get_weight(self, adjacent):
        """
        Returns weight of adjacent vertex
        """
        for vertex in self.adjacent_vertices:
            if vertex[0] == adjacent:
                return vertex[1]


#------- BEGIN GRAPH CLASS DEFINITION -------#
class Graph():
    """
    Graph ADT Class Definition
    """
    def __init__(self):
        """
        Constructor for Graph
        @param vertices: list of all vertices
        @param graph: dictionary representation of graph
        """
        self.vertices = []
        self.graph = {}
        self.visited = []

    def add_vertex(self, label):
        """
        Add a vertex with a specified label.
        Return the graph.
        Label must be a string or raise ValueError.
        """
        if not isinstance(label, str):
            raise ValueError('param label is not string')

        self.vertices.append(label)
        self.graph[label] = Vertex(label)
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
        if not isinstance(src, str) or not isinstance(dest, str) or not isinstance(w, float):
            raise ValueError('Parameters for add_edge method of invalid type')

        if src not in self.graph:
            raise ValueError('Parameter src not in Graph')
        if dest not in self.graph:
            raise ValueError('Parameter dest not in Graph')
        self.graph[src].add_adjacent(self.graph[dest], w)

    def get_weight(self, src, dest) -> float:
        """
        @type float
        Return the weight on edge src-dest
        (math.inf if no path exists,
        raise ValueError if src or dest not added to graph).
        """
        # Validating both src and dest in graph
        if src not in self.graph or dest not in self.graph:
            raise ValueError('Either source or destination vertex not added to graph')

        adjacent_list = self.graph[src].get_adjacent()
        if dest not in adjacent_list:
            return math.inf
        adjacent_vertex_list = self.graph[src].get_adjacent_vertices()
        # Searches for exact vertex
        for i in range(adjacent_vertex_list):
            # Once it gets a match returns the weight
            if adjacent_list[i] == dest:
                return float(adjacent_list[1])

    def dfs(self, starting_vertex):
        """
        Return a generator for traversing the graph
        in depth-first order starting fro the specified vertex.
        Raise a ValueError if the vertex doesn't exist
        """
        self.dfs_helper(self.visited, self.graph, starting_vertex)

    def dfs_helper(self, visited, graph, starting_vertex):
        """
        Recursive dfs helper
        """
        if starting_vertex not in visited:
            visited.append(starting_vertex)
            for vertex in graph:
                for adjacent in graph[vertex].adjacent_vertices:
                    self.dfs_helper(visited, graph, adjacent)


    def bfs(self, starting_vertex):
        """
        Return a generator for traversing the graph
        in breadth-first order starting fro the specified vertex.
        Raise a ValueError if the vertex doesn't exist
        """
        visited = {}
        queue = []

        queue.append(starting_vertex)
        visited[starting_vertex] = True

        while queue:
            starting_vertex = queue.pop(0)
            for vertex in self.adjacent_vertices:
                queue.append(vertex)
                visited[vertex] = True

    def dijkstra_shortest_path(self, src, dest) -> list:
        """
        @type list
        Return a tuple (path length, the list of the vertices
        on the path from dest back to src).
        If no path exists, return the tuple (math.inf, empty list).
        """
        return

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
        num_vertices = len(self.vertices)
        output = 'numVertices: ' + str(num_vertices) + '\n'
        output += 'Vertex' + '\t' + 'Adjacentcy List' + '\n'
        for v_label in self.vertices:
            vertex = self.graph[v_label]
            vertex_str = vertex.label + '\t'
            for i in range(0, len(vertex.adjacent_vertices)):
                adjacent = vertex.adjacent_vertices[i]
                vertex_str += "[('" + adjacent[0] + ', ' + str(adjacent[1]) + ')'
                if i < len(vertex.adjacent_vertices) - 1:
                    vertex_str += ', '
            vertex_str += ']\n'
            output += vertex_str
        return output


#------- END GRAPH CLASS DEFINITION --------#
