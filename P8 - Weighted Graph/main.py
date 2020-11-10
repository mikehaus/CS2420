from graph import Graph


def main():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 2)
    g.add_edge("A", "F", 9)

    g.add_edge("B", "F", 6)
    g.add_edge("B", "D", 15)
    g.add_edge("B", "C", 8)

    g.add_edge("C", "D", 1)

    g.add_edge("E", "C", 7)
    g.add_edge("E", "D", 3)

    g.add_edge("F", "E", 3)
    print(g.bfs('A'))
    print(g.dfs('A'))
    print(str(g))

main()