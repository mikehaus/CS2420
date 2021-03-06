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
        return self

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
        if not isinstance(src, str) or not isinstance(dest, str) or not (isinstance(w, float) or isinstance(w, int)):
            raise ValueError('Parameters for add_edge method of invalid type')

        if src not in self.graph:
            raise ValueError('Parameter src not in Graph')
        if dest not in self.graph:
            raise ValueError('Parameter dest not in Graph')
        self.graph[src].append(tuple((dest, float(w))))
        return self

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

    def minDistance(self, u, v, distances):
        """
        Compares distances between two vertices and
        updates distance if necessary
        """
        path_weight = distances[u][0] + self.get_weight(u, v)
        if path_weight < distances[v][0]:
            distances[v][0] = path_weight
            path_list = []
            path_list += distances[u][1]
            distances[v][1] = path_list
            distances[v][1].append(v)

    def dijkstra_shortest_path(self, src, dest='null'):
        """
        @type tuple
        Return a tuple (path length, the list of the vertices
        on the path from dest back to src).
        If no path exists, return the tuple (math.inf, empty list).
        If destination node not provided, calculates overall dsp for single vertex.
        """
        # If no second argument provided returns dictionary
        if src not in self.graph:
            raise ValueError('Argument src not key in graph')

        if dest == 'null':
            return self.dsp_dict(src)

        if src == dest:
            return (0.0, [src])

        dsp = (0.0, [])
        default = (math.inf, [])
        visited = []
        distances = {}
        for vertex in self.vertices:
            if vertex != src:
                distances[vertex] = [math.inf, []]
            else:
                visited.append(vertex)
                distances[vertex] = [0.0, [vertex]]

        current = src
        index = 0
        #while dest not in visited:
        while index <= 6:
            for vertex in self.graph[current]:
                self.minDistance(current, vertex[0], distances)
                visited.append(vertex[0])
                #if vertex[0] == dest:
                    # I'm too lazy to go back and prepend stuff
                    #distances[vertex[0]][1].reverse()
                    #dsp = (distances[vertex[0]][0], distances[vertex[0]][1])
                    #return dsp
            index += 1
            if index >= len(visited):
                return default
            current = visited[index]
        min_dist = []
        for vertex in distances:
            distances[vertex][1].reverse
            vertex_arr = distances[vertex]
            if vertex_arr[1][0] == src and vertex_arr[1][len(vertex_arr[1]) - 1] == dest:
                if len(min_dist) == 0:
                    min_dist = vertex_arr
                elif min_dist[0] > vertex_arr[1][0]:
                    min_dist = vertex_arr
        if len(min_dist) == 0:
            return default
        min_dist[1].reverse()
        return (min_dist[0], min_dist[1])

    def dsp_dict(self, src):
        """
        Return a dictionary of the shortest weighted path
        between src and all other vertices using Dijkstra's
        shortest path algorithm.
        In the dictionary, the key is the vertex label, the value
        is a tuple (path length, the list of vertices on the path
        from key back to src).
        """
        # This one basically does shortest path for all vertices
        # in a simple for loop using original Dijkstra function
        dsp = {}
        for vertex in self.vertices:
            dsp[vertex] = self.dijkstra_shortest_path(src, vertex)
        return dsp

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
                if (len(self.graph[vertex]) > 1 and i < len(vertex) - 1):
                    vertex_str += ', '
            vertex_str += ']\n'
            output += vertex_str
        return output


#------- END GRAPH CLASS DEFINITION --------#
