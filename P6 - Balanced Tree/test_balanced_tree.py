import unittest
from binarysearchtree import Node, BinarySearchTree
from random import seed, sample
from recursioncounter import RecursionCounter as rc
import io
import sys

class TestInOrder(unittest.TestCase):
    def test_inorder(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 4000), k=126)
        for x in data:
            bst.add(x)

        data.sort()
        tree_data = list(bst.inorder())
        self.assertEqual(data, tree_data)


class TestHeight(unittest.TestCase):
    def test_tree_height(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.height(), -1)
        for i in range(511):
            bst.add(i)

        self.assertEqual(bst.height(), 510)
        bst.rebalance_tree()
        self.assertEqual(bst.height(), 8)
class TestRebalance(unittest.TestCase):
    def test_rebalance(self):
        bst = BinarySearchTree()
        seed(0)
        data = sample(range(1, 4000), k=126)
        data.sort()
        for x in data:
            bst.add(x)
        original_height = bst.height()
        self.assertEqual(data[0], bst.root.data)

        bst.rebalance_tree()
        tree_data = list(bst.inorder())
        self.assertEqual(data, tree_data)
        self.assertNotEqual(original_height, bst.height())

class TestCodingStandards(unittest.TestCase):
    def test_code_quality(self):
        from pylint import epylint as lint
        (pylint_stdout, _) = lint.py_run("binarysearchtree.py", return_std=True)
        output = pylint_stdout.getvalue()
        offset = output.rfind(" been rated at ")
        if offset != -1:
            output = output[offset:]
            end = output.find('/')
            output = output[15:end]
            score = float(output)
            self.assertGreaterEqual(score, 8.5)

if __name__=='__main__':
    unittest.main()
