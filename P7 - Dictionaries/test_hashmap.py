import unittest
from hashmap import HashMap
from main import main as mn
import io
import sys


class TestKeyPresent(unittest.TestCase):
    def test_empty_map(self):
        hm = HashMap()
        self.assertEqual(hm.capacity(), 8)
        self.assertEqual(hm.size(), 0)

    def test_key_present(self):
        hm = HashMap()
        self.assertEqual(hm.get("asdf"), None)
        self.assertEqual(hm.get("asdf", 0), 0)
        hm.set("qwerty", 12345)
        self.assertEqual(hm.get("qwerty"), 12345)
        self.assertEqual(hm.size(), 1)
        self.assertEqual(hm.capacity(), 8)

class TestNominalMap(unittest.TestCase):
    def test_ten_keys(self):
        hm = HashMap()
        keys = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
        values = list(range(1, 11))
        for i in range(len(keys)):
            hm.set(keys[i], values[i])
        self.assertEqual(hm.get("sixth"), 6)
        self.assertNotEqual(hm.get("sixth"), 7)
        self.assertNotEqual(hm.get("sixth"), 5)
        hm.set("third", 409)
        self.assertEqual(hm.get("third"), 409)
        self.assertEqual(hm.size(), 10)
        self.assertEqual(hm.capacity(), 16)

class TestRehash(unittest.TestCase):
    def test_rehashing(self):
        keys = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
        values = list(range(1, 11))
        hm = HashMap()
        self.assertEqual(hm.size(), 0)
        self.assertEqual(hm.capacity(), 8)
        for i in range(0, 5):
            hm.set(keys[i], values[i])
        self.assertEqual(hm.size(), 5)
        self.assertEqual(hm.capacity(), 8)
        output = hm.keys()
        self.assertEqual(len(output), 5)
        for key in output:
            self.assertIn(key, keys)
        for i in range(5, 10):
            hm.set(keys[i], values[i])
        self.assertEqual(hm.size(), 10)
        self.assertEqual(hm.capacity(), 16)
        output = hm.keys()
        for key in output:
            self.assertIn(key, keys)
        for key in keys:
            self.assertIn(key, output)
        
class TestMainOutput(unittest.TestCase):
    def test_main_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        mn()
        sys.stdout = sys.__stdout__
        data = "".join(captured_output.getvalue().split())
        data1 = "Themostcommonwordsare:the1818and940to809of631it610she553you481said462in431alice403was358that330as274her248with228"
        self.assertEqual(data, data1)

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
        (pylint_stdout, _) = lint.py_run("hashmap.py", return_std=True)
        output = pylint_stdout.getvalue()
        offset = output.rfind(" been rated at ")
        if offset != -1:
            output = output[offset:]
            end = output.find('/')
            output = output[15:end]
            score = float(output)
            self.assertGreaterEqual(score, 8.5)

        
        


