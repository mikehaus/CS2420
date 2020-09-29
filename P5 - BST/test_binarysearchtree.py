import unittest
from binarysearchtree import Node, BinarySearchTree
from random import seed, sample
from main import main as mn
from recursioncounter import RecursionCounter as rc
import io
import sys

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = Node(12345)
        self.assertTrue(node.is_leaf())
        self.assertEqual(node.data, 12345)
        self.assertEqual(node.height, 0)
        node.update_height()
        self.assertEqual(node.height, 0)

class TestBinarySearchTree(unittest.TestCase):
    def test_tree_creation(self):
        bst = BinarySearchTree()
        self.assertEqual(len(bst), 0)
        self.assertTrue(bst.is_empty())

    def test_tree_size(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=123)
        for datum in data:
            bst.add(datum)
        self.assertEqual(len(bst), 123)

    def test_tree_height(self):
        bst = BinarySearchTree()
        bst.add(123)
        self.assertEqual(bst.height(), 0)
        bst.add(12)
        bst.add(2)
        self.assertEqual(bst.height(), 2)

    def test_find(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=123)
        for datum in data:
            bst.add(datum)
        self.assertEqual(bst.find(data[0]).data, data[0])
        self.assertEqual(bst.find(401), None)

    def test_remove(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 100), k=10)
        for datum in data:
            bst.add(datum)
        bst.remove(data[0])
        self.assertEqual(bst.find(data[0]), None)

    def test_preorder(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=123)
        for datum in data:
            bst.add(datum)
        output = bst.preorder()
        self.assertTrue(isinstance(output, list))
        self.assertEqual(len(output), 123)
        self.assertEqual(output[0], data[0])

    def test_string(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        mn()
        sys.stdout = sys.__stdout__
        data = "".join(captured_output.getvalue().split())

        data1 = "21,9,4,2,3,7,14,10,18,15,26,30,28,21(4)9(3)4(2)2(1)[Empty]3(0)[leaf]7(0)[leaf]14(2)10(0)[leaf]18(1)15(0)[leaf][Empty]26(2)[Empty]30(1)28(0)[leaf][Empty]26(3)10(2)2(1)[Empty]3(0)[leaf]14(0)[leaf]30(1)28(0)[leaf][Empty]"
        self.assertEqual(data, data1)

class RecursionTests(unittest.TestCase):
    def test_recursive_add(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=20)
        rc.recursion_count = 0
        for datum in data:
            bst.add(datum)
        self.assertGreater(rc.recursion_count, 40)

    def test_recursive_find(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=20)
        rc.recursion_count = 0
        for datum in data:
            bst.add(datum)
        rc.recursion_count = 0
        bst.find(data[11])
        self.assertGreater(rc.recursion_count, 3)

    def test_recursive_preorder(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=20)
        rc.recursion_count = 0
        for datum in data:
            bst.add(datum)
        rc.recursion_count = 0
        bst.preorder()
        self.assertGreater(rc.recursion_count, 30)

    def test_recursive_str(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=20)
        rc.recursion_count = 0
        for datum in data:
            bst.add(datum)
        rc.recursion_count = 0
        str(bst)
        self.assertGreater(rc.recursion_count, 20)

    def test_recursive_length(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=20)
        rc.recursion_count = 0
        for datum in data:
            bst.add(datum)
        rc.recursion_count = 0
        len(bst)
        self.assertGreater(rc.recursion_count, 30)

    def test_recursive_remove(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 400), k=20)
        for datum in data:
            bst.add(datum)
        rc.recursion_count = 0
        for datum in data:
            bst.remove(datum)
        self.assertGreater(rc.recursion_count, 40)

        
        

class TestCodeingStandards(unittest.TestCase):
    def test_code_quality(self):
        from pylint import epylint as lint
        (pylint_stdout, _) = lint.py_run("main.py", return_std=True)
        output = pylint_stdout.getvalue()
        offset = output.rfind(" been rated at ")
        if offset != -1:
            output = output[offset:]
            end = output.find('/')
            output = output[15:end]
            score = float(output)
            self.assertGreaterEqual(score, 8.5)
        (pylint_stdout, _) = lint.py_run("binarysearchtree.py", return_std=True)
        output = pylint_stdout.getvalue()
        offset = output.rfind(" been rated at ")
        if offset != -1:
            output = output[offset:]
            end = output.find('/')
            output = output[15:end]
            score = float(output)
            self.assertGreaterEqual(score, 8.5)


