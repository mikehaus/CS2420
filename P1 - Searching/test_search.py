import unittest
from search import linear_search, recursive_binary_search, jump_search
from random import seed, sample
from time import perf_counter
from math import sqrt
from recursioncounter import RecursionCounter
import time

class TestSearchTiming(unittest.TestCase):
    def test_search_at_end(self):
        self.DATA_SIZE = 1000000
        seed(0)
        self.data = sample(range(self.DATA_SIZE * 3), k=self.DATA_SIZE)
        self.data.sort()

        start = time.perf_counter()
        result = recursive_binary_search(self.data, self.data[-1])
        fastest = time.perf_counter() - start
        self.assertTrue(result) 

        start = time.perf_counter()
        result = linear_search(self.data, self.data[-1])
        slowest = time.perf_counter() - start
        self.assertTrue(result)
        self.assertLess(fastest * 10000, slowest * 10000)

        start = time.perf_counter()
        result = jump_search(self.data, self.data[-1])
        fastest = time.perf_counter() - start
        self.assertTrue(result)
        self.assertLess(fastest * 10000, slowest * 10000)

    def test_search_at_beginning(self):
        self.DATA_SIZE = 1000
        seed(0)
        self.data = sample(range(self.DATA_SIZE * 3), k=self.DATA_SIZE)
        self.data.sort()

        result = linear_search(self.data, self.data[0])
        self.assertTrue(result) 
        
        result = recursive_binary_search(self.data, self.data[0])
        self.assertTrue(result) 

        result = jump_search(self.data, self.data[0])
        self.assertTrue(result) 

    def test_search_at_middle(self):
        self.DATA_SIZE = 1000
        seed(0)
        self.data = sample(range(self.DATA_SIZE * 3), k=self.DATA_SIZE)
        self.data.sort()

        result = linear_search(self.data, self.data[(self.DATA_SIZE // 2) - 1])
        self.assertTrue(result) 
        
        result = recursive_binary_search(self.data, self.data[(self.DATA_SIZE // 2) - 1])
        self.assertTrue(result) 

        result = jump_search(self.data, self.data[(self.DATA_SIZE // 2) - 1])
        self.assertTrue(result) 

    def test_search_not_found(self):
        self.DATA_SIZE = 1000
        seed(0)
        self.data = sample(range(self.DATA_SIZE * 3), k=self.DATA_SIZE)
        self.data.sort()

        result = linear_search(self.data, self.DATA_SIZE * 4)
        self.assertFalse(result) 
        
        result = recursive_binary_search(self.data, self.DATA_SIZE * 4)
        self.assertFalse(result) 

        result = jump_search(self.data, self.DATA_SIZE * 4)
        self.assertFalse(result) 

class TestParameterChecking(unittest.TestCase):
    def test_bad_params(self):
        self.DATA_SIZE = 1000
        seed(0)
        self.data = sample(range(self.DATA_SIZE * 3), k=self.DATA_SIZE)
        self.data.sort()

        self.assertRaises(ValueError, linear_search, self.data, "cat")
        self.assertRaises(ValueError, recursive_binary_search, self.data, "cat")
        self.assertRaises(ValueError, jump_search, self.data, "cat")

        self.data[0] = "cat"
        self.assertRaises(ValueError, linear_search, self.data, 0)
        self.assertRaises(ValueError, recursive_binary_search, self.data, 0)
        self.assertRaises(ValueError, jump_search, self.data, 0)

class TestBinarySearchRecursion(unittest.TestCase):
    def test_recursion(self):
        self.DATA_SIZE = 1000
        seed(0)
        self.data = sample(range(self.DATA_SIZE * 3), k=self.DATA_SIZE)
        self.data.sort()
        recursive_binary_search(self.data, self.data[-1])
        self.assertGreater(RecursionCounter.recursion_count, 9)

class TestCodingStandards(unittest.TestCase):
    def test_code_quality(self):
        from pylint import epylint as lint
        import glob
        for file_name in glob.glob('*.py'):
            if file_name[:5] != "test_" and file_name != "recursioncounter.py":
                (pylint_stdout, _) = lint.py_run(file_name, return_std=True)
                output = pylint_stdout.getvalue()
                offset = output.rfind(" been rated at ")
                if offset != -1:
                    output = output[offset:]
                    end = output.find('/')
                    output = output[15:end]
                    score = float(output)
                    self.assertGreaterEqual(score, 8.5)

if __name__ == '__main__':
    unittest.main()