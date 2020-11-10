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

    def add_vertex(self, label):
        """
        Add a vertex with a specified label.
        Return the graph.
        Label must be a string or raise ValueError.
        """
        if not isinstance(label, str):
            raise ValueError('param label is not string')

        self.vertices.append(label)
        self.graph[label] = []
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
        if not isinstance(src, str) or not isinstance(dest, str) or not isinstance(w, int):
            raise ValueError('Parameters for add_edge method of invalid type')

        if src not in self.graph:
            raise ValueError('Parameter src not in Graph')
        if dest not in self.graph:
            raise ValueError('Parameter dest not in Graph')
        self.graph[src].append(tuple((dest, float(w))))
        return self.graph

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
        vertex = self.graph[src]
        for i in range(0, len(vertex)):
            edge = vertex[i]
            if edge[0] == dest:
                return edge[1]
        return math.inf

    def bfs(self, starting_vertex):
        """
        Return a generator for traversing the graph
        in breadth-first order starting fro the specified vertex.
        Raise a ValueError if the vertex doesn't exist
        """
        visited = []
        self.bfs_helper(visited, starting_vertex)
        return visited

    def bfs_helper(self, visited, starting_vertex):
        """
        Recursive bfs helper
        """
        if starting_vertex[0] not in visited:
            visited.append(starting_vertex[0])
        for adjacent in self.graph[starting_vertex[0]]:
            if adjacent[0] not in visited:
                visited.append(adjacent[0])
        for adjacent in self.graph[starting_vertex[0]]:
            self.bfs_helper(visited, adjacent)                

    def dfs(self, starting_vertex):
        """
        Return a generator for traversing the graph
        in depth-first order starting fro the specified vertex.
        Raise a ValueError if the vertex doesn't exist
        """
        visited = []
        self.dfs_helper(visited, starting_vertex)
        return visited

    def dfs_helper(self, visited, starting_vertex):
        """
        Helper recursive DFS method.
        """
        if starting_vertex[0] not in visited:
            visited.append(starting_vertex)
        for i in range(len(self.graph[starting_vertex]), 0, -1):
            self.dfs_helper(visited, self.graph[starting_vertex][i - 1][0])


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
        output += 'Vertex' + '\t' + 'Adjacency List' + '\n'
        for vertex in self.graph:
            vertex_str = vertex[0] + '\t' + '['
            for i in range(len(self.graph[vertex])):
                vertex_str += "('" + self.graph[vertex][i][0] + "', " + str(self.graph[vertex][i][1]) + ')'
                if (len(self.graph[vertex]) > 1 and i <= len(vertex) - 1):
                    vertex_str += ', '
            vertex_str += ']\n'
            output += vertex_str
        return output


#------- END GRAPH CLASS DEFINITION --------#
