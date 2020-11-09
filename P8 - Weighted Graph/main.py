from graph import Graph


def main():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_edge('A', 'C', 5.0)
    g.add_edge('A', 'B', 3.0)
    print(g.graph['A'].get_weight('B'))

main()