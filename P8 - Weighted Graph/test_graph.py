import unittest
from graph import Graph
import io
import math

class TestDefineGraph(unittest.TestCase):
    def test_vertex_edge_weight(self):
        g = Graph()
        self.assertRaises(ValueError, g.add_vertex, 0)
        g.add_vertex("A")
        x = g.add_vertex("B")
        self.assertRaises(ValueError, g.add_edge,"A", "cat", 10.0)
        self.assertRaises(ValueError, g.add_edge,"A", "B", "cat")
        self.assertIsInstance(x, Graph)
        x = g.add_edge("A", "B", 10.0)
        self.assertEqual(g.get_weight("A", "B"), 10)
        self.assertEqual(g.get_weight("B", "A"), math.inf)
        self.assertIsInstance(x, Graph)

    def test_traversal(self):
        g = Graph()
        self.assertRaises(ValueError, g.add_vertex, 0)
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")
        g.add_vertex("D")
        g.add_vertex("E")
        g.add_vertex("F")

        g.add_edge("A", "B", 1.0)
        g.add_edge("A", "C", 1.0)

        g.add_edge("B", "D", 1.0)

        g.add_edge("C", "E", 1.0)

        g.add_edge("E", "F", 1.0)

        gen = g.bfs("A")
        data = [x for x in gen]
        self.assertEqual(data[0], "A")
        self.assertEqual(data[-1], "F")
        self.assertEqual(len(data), 6)
        gen = g.bfs("C")
        data = [x for x in gen]
        self.assertEqual(len(data), 3)

        gen = g.dfs("A")
        data = [x for x in gen]
        self.assertEqual(data[0], "A")
        self.assertIn(data[-1], ("D", "F"))
        self.assertEqual(len(data), 6)
        gen = g.dfs("C")
        data = [x for x in gen]
        self.assertEqual(len(data), 3)

    def test_print(self):
        g = Graph()
        self.assertRaises(ValueError, g.add_vertex, 0)
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")
        g.add_vertex("D")
        g.add_vertex("E")
        g.add_vertex("F")

        g.add_edge("A", "B", 1.0)
        g.add_edge("A", "C", 1.0)

        g.add_edge("B", "D", 1.0)

        g.add_edge("C", "E", 1.0)

        g.add_edge("E", "F", 1.0)
        
        output = str(g)
        self.assertEqual(output[:14], "numVertices: 6")
    
class TestGraphPaths(unittest.TestCase):
    def test_shortest_path(self):
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

        self.assertRaises(ValueError, g.dijkstra_shortest_path, "cat")
        data = g.dijkstra_shortest_path("A", "B")
        self.assertIsInstance(data, tuple)
        self.assertEqual(data, (2.0, ['B', 'A']))
        data = g.dijkstra_shortest_path("A", "C")
        self.assertEqual(data, (10.0, ['C', 'B', 'A']))
        data = g.dijkstra_shortest_path("A", "D")
        self.assertEqual(data, (11.0, ['D', 'C', 'B', 'A']))
        data = g.dijkstra_shortest_path("A", "F")
        self.assertEqual(data, (8.0, ['F', 'B', 'A']))
        data = g.dijkstra_shortest_path("D",'A')
        self.assertEqual(data, (math.inf, []))

        data = g.dijkstra_shortest_path("A")
        self.assertIsInstance(data, dict)
        self.assertDictEqual(data, {'A':(0.0, ['A']), 'B':(2.0, ['B', 'A']), 'C':(10.0, ['C', 'B', 'A']), 'D':(11.0, ['D', 'C', 'B', 'A']), 'E':(11.0, ['E', 'F', 'B', 'A']), 'F':(8.0, ['F', 'B', 'A'])})
        
        data = g.dijkstra_shortest_path("D")
        self.assertDictEqual(data, {'A':(math.inf, []), 'B':(math.inf, []), 'C':(math.inf, []), 'D':(0.0, ['D']), 'E':(math.inf, []), 'F':(math.inf, [])})

class TestCodeingStandards(unittest.TestCase):
    def test_code_quality(self):
        from pylint import epylint as lint
        (pylint_stdout, _) = lint.py_run("graph.py", return_std=True)
        output = pylint_stdout.getvalue()
        offset = output.rfind(" been rated at ")
        if offset != -1:
            output = output[offset:]
            end = output.find('/')
            output = output[15:end]
            score = float(output)
            self.assertGreaterEqual(score, 8.5)        
        





