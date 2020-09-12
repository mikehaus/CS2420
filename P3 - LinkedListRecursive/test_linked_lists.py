import unittest
from course import Course
from courselist import CourseList
from main import main as mn
import random
from recursioncounter import RecursionCounter
import io
import sys

class TestEmptyCourse(unittest.TestCase):
    def test_course_creation(self):
        # make sure that an empty course is correct
        c = Course()
        self.assertEqual(c.name(), "")
        self.assertEqual(c.number(), 0)
        self.assertEqual(c.credit_hr(), 0.0)
        self.assertEqual(c.grade(), 0.0)
        self.assertEqual(c.next, None)

class TestNominalCourse(unittest.TestCase):
    def test_course_creation_with_parameters(self):
        c = Course(1234, "Test Name", 3.0, 3.72)
        self.assertEqual(c.number(), 1234)
        self.assertEqual(c.name(), "Test Name")
        self.assertAlmostEqual(c.credit_hr(), 3.0)
        self.assertAlmostEqual(c.grade(), 3.72)
        self.assertIsNone(c.next)

        self.assertRaises(ValueError, Course, "cat")
        self.assertRaises(ValueError, Course, 1234, None)
        self.assertRaises(ValueError, Course, 1234, "Test Name", "cat")
        self.assertRaises(ValueError, Course, 1234, "Test Name", 3.0, "cat")
        self.assertRaises(ValueError, Course, -1)
        self.assertRaises(ValueError, Course, 1234, "Test Name", -2.1)
        self.assertRaises(ValueError, Course, 1234, "Test Name", 0.0, -2.0)

class TestEmptyCourseList(unittest.TestCase):
    def test_empty_courselist(self):
        cl = CourseList()
        self.assertIsNone(cl.head)
        self.assertEqual(cl.size(), 0)
        self.assertAlmostEqual(cl.calculate_gpa(), 0.0)
        self.assertAlmostEqual(cl.calculate_gpa(), 0.0)
        self.assertTrue(cl.is_sorted())
    
class TestNominalCourseList(unittest.TestCase):
    def test_insert(self):
        random.seed(0)
        cl = CourseList()
        for _ in range(37):
            cl.insert(Course(random.randrange(1000, 7000), "test", 1.0, 2.0))

        self.assertEqual(cl.size(), 37)
        self.assertTrue(cl.is_sorted())

    def test_remove(self):
        random.seed(0)
        cl = CourseList()
        courseNumbers = []
        for _ in range(37):
            courseNumbers.append(random.randrange(1000, 7000))
        for number in courseNumbers:
            cl.insert(Course(number, "test", 1.0, 2.0))

        course = cl.find(courseNumbers[0])
        self.assertEqual(course.number(), courseNumbers[0])
        course = cl.find(courseNumbers[10])
        self.assertEqual(course.number(), courseNumbers[10])
        course = cl.find(courseNumbers[36])
        self.assertEqual(course.number(), courseNumbers[36])

        for i in range(0, 30, 3):
            cl.remove(courseNumbers[i])

        self.assertEqual(cl.size(), 27)
        self.assertTrue(cl.is_sorted())

    def test_remove_all(self):
        cl = CourseList()
        cl.insert(Course(1000))
        for _ in range(20):
            cl.insert(Course(1200))
        cl.insert(Course(1800))
        self.assertEqual(cl.size(), 22)
        cl.remove_all(1200)
        self.assertEqual(cl.size(), 2)


    def test_gpa(self):
        random.seed(0)
        cl = CourseList()
        total_credits = 0.0
        total_grade_points = 0.0
        for _ in range(10):
            credits = random.uniform(1.0, 5.0)
            grade = random.uniform(0.0, 4.0)
            total_credits += credits
            total_grade_points += credits * grade
            cl.insert(Course(1234, "Test", credits, grade))

        self.assertAlmostEqual(cl.calculate_gpa(), (total_grade_points / total_credits))

    def test_iterate_list(self):
        cl = CourseList()
        cl.insert(Course(1000))
        for _ in range(20):
            cl.insert(Course(1200))
        totalCourses = 0
        for _ in cl:
            totalCourses += 1
        self.assertEqual(totalCourses, 21)

class TestRecursion(unittest.TestCase):
    def test_insert_recursion(self):
        RecursionCounter.recursion_count = 0
        cl = CourseList()
        for i in range(1000, 1010):
            cl.insert(Course(i, "Test", 1.0, 1.0))
        self.assertGreater(RecursionCounter.recursion_count, 40)

    def test_size_recursion(self):
        cl = CourseList()
        for i in range(1000, 1010):
            cl.insert(Course(i, "Test", 1.0, 1.0))
        RecursionCounter.recursion_count = 0
        cl.size()
        self.assertGreater(RecursionCounter.recursion_count, 9)

    def test_find_recursion(self):
        cl = CourseList()
        for i in range(1000, 1010):
            cl.insert(Course(i, "Test", 1.0, 1.0))
        RecursionCounter.recursion_count = 0
        cl.find(-1)
        self.assertGreater(RecursionCounter.recursion_count, 9)

    def test_remove_recursion(self):
        cl = CourseList()
        for i in range(1000, 1010):
            cl.insert(Course(i, "Test", 1.0, 1.0))
        RecursionCounter.recursion_count = 0
        cl.remove(1005)
        self.assertGreater(RecursionCounter.recursion_count, 4)
        
    def test_sorted_recursion(self):
        cl = CourseList()
        for i in range(1000, 1010):
            cl.insert(Course(i, "Test", 1.0, 1.0))
        RecursionCounter.recursion_count = 0
        cl.is_sorted()
        self.assertGreater(RecursionCounter.recursion_count, 9)
    
    def test_gpa_recursion(self):
        tmp = TestNominalCourseList()
        RecursionCounter.recursion_count = 0
        tmp.test_gpa()
        self.assertGreater(RecursionCounter.recursion_count, 28)


class TestCodeingStandards(unittest.TestCase):
    def test_code_quality(self):
        from pylint import epylint as lint
        import glob
        for file_name in glob.glob('*.py'):
            if file_name[:5] != "test_":
                (pylint_stdout, _) = lint.py_run(file_name, return_std=True)
                output = pylint_stdout.getvalue()
                offset = output.rfind(" been rated at ")
                if offset != -1:
                    output = output[offset:]
                    end = output.find('/')
                    output = output[15:end]
                    score = float(output)
                    self.assertGreaterEqual(score, 8.5)

class TestDriverOutput(unittest.TestCase):
    def test_main_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        mn()
        sys.stdout = sys.__stdout__
        data = "".join(captured_output.getvalue().split())

        data1 = "Current List: (5)cs1030 Introduction to Computers Grade:3.2 Credit Hours: 2.0cs1400 Introduction to Programming Grade:3.6 Credit Hours: 4.0cs1410 C++ Programming Grade:2.6 Credit Hours: 4.0cs2420 Introduction to Data Structures Grade:3.2 Credit Hours: 4.0cs2810 Computer Architecture Grade:3.8 Credit Hours: 3.0Cumulative GPA: 3.259".replace(" ","")
        self.assertEqual(data, data1)    

if __name__ == "__main__":
    unittest.main()
