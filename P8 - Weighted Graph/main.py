from graph import Graph


def main():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_edge('A', 'C', 5.0)
    g.add_edge('A', 'B', 3.0)
    print(g.graph['A'].get_weight('B'))
    g.add_vertex('C')
    g.add_edge('A', 'C', 4.0)
    g.add_edge('B', 'C', 4.0)
    g.add_edge('B', 'A', 4.0)
    g.add_edge('C', 'A', 4.0)
    print(str(g))

main()