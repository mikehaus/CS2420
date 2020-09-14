"""
CourseList Class declaration
CS2420 - P3 Recursive Linked List
courselist.py
Mike Hollingshaus
"""
from course import Course
from recursioncounter import RecursionCounter

#-------- START Courselist Class Definition -------#

class CourseList():
    """
    Courselist is a fairly standard implementation of a linked list
    but all nodes are "Courses" in an academic sense. All iteration done is
    recursive.
    """
    def __init__(self):
        """
        CourseList Constructor
        """
        self.head = None
        self.itr = None

    def insert(self, course):
        """
        Inserts course Course into list in ascending course number order
        """
        if self.size() == 0:
            self.itr = self.head
            self.head = course
            return
        self.insert_recursive_helper(self.head, course)

    def remove(self, number):
        """
        Removes first occurance of course with
        course number number
        """
        self.remove_recursive_helper(self.head, number, 'first')

    def remove_all(self, number):
        """
        Removes all courses with course number number.
        """
        self.remove_recursive_helper(self.head, number, 'all')

    def find(self, number):
        """
        If target coursenumber not found at head, recursively
        iterates through list. If found returns course number else returns
        -1
        """
        if self.head is None:
            return -1
        if self.head.number() == number:
            return number
        return self.traverse_recursive_find_helper(self.head, number)

    def size(self):
        """
        Returns list size.
        """
        if self.head is None:
            return 0
        return self.size_recursive_helper(self.head, 0)

    def calculate_gpa(self):
        """
        Calculates GPA based on grade attribute stored in Course Node class.
        Might need to be weighted not sure.
        """
        if self.size() == 0:
            return 0.0
        grade_point_total_array = self.traverse_recursive_gpa_helper(self.head, 0.0, 0.0)
        return grade_point_total_array[0] / grade_point_total_array[1]

    def is_sorted(self):
        """
        Boolean return value recursively searches through and if sorted returns true.
        Else returns False.
        """
        if self.head is None:
            return True
        return self.traverse_recursive_sorted_helper(self.head.next, self.head.number())

    def __str__(self):
        course_string = ''
        return self.traverse_recursive_string_helper(self.head, course_string)

    def __iter__(self):
        """
        Creates iterator for List and returns self.
        """
        self.itr = self.head
        return self

    def __next__(self):
        """
        Increments the iterator attr for CourseList.
        """
        if self.itr.next == None:
            raise StopIteration
        self.itr = self.itr.next
        return self.itr

#------ START Recursive Helper Methods -------#

    def traverse_recursive_string_helper(self, course, course_string):
        """
        Traverses recursively through list and concatentates
        all Course str functions into a single string.
        """
        RecursionCounter()
        if course is None:
            return course_string
        course_string += str(course)
        return self.traverse_recursive_string_helper(course.next, course_string)

    def traverse_recursive_find_helper(self, course, target):
        """
        Traverses list recursively and returns Course Node that
        matches with number value. Returns course number if found
        and if not found, returns Null
        """
        RecursionCounter()
        if course is None:
            return -1
        if course.number() == target:
            return course
        return self.traverse_recursive_find_helper(course.next, target)

    def traverse_recursive_gpa_helper(self, course, grade_point_total, credit_hr_total):
        """
        Traverses list recursively and returns Course Node that
        matches with number value. Returns Node and if not found, returns
        Null
        """
        RecursionCounter()
        if course is None:
            return [grade_point_total, credit_hr_total]
        grade_point_total += (course.grade() * course.credit_hr())
        credit_hr_total += course.credit_hr()
        return self.traverse_recursive_gpa_helper(course.next, grade_point_total, credit_hr_total)

    def traverse_recursive_sorted_helper(self, course, last_course_num):
        """
        Traverses list recursively and validates classes are in order.
        Returns True if Sorted False if Unsorted
        """
        RecursionCounter()
        if course is None:
            return True
        if course.number() < last_course_num:
            return False
        return self.traverse_recursive_sorted_helper(course.next, course.number())

    def insert_recursive_helper(self, node, course):
        """
        Recursively inserts node
        """
        RecursionCounter()
        if course.number() < node.number():
            course.next = node
            course.prev = node.prev
            if course.prev is not None:
                course.prev.next = course
            node.prev = course
            if node == self.head:
                self.head = course
                self.itr = course
            return
        if node.next is None:
            node.next = course
            course.prev = node
            return
        return self.insert_recursive_helper(node.next, course)

    def remove_recursive_helper(self, node, course_num, case):
        """
        Recursive function that removes node Course from list if
        course_num matches node.number (coursenumber)
        case param is to tell whether we are removing first or all instances
        """
        RecursionCounter()
        if node is None:
            return
        if node.number() == course_num:
            node.prev.next = node.next
            node.next.prev = node.prev
            if case == 'first':
                return
        self.remove_recursive_helper(node.next, course_num, case)

    def size_recursive_helper(self, node, size):
        """
        Recursive helper function to return the size of the list
        based on how many nodes there are.
        """
        RecursionCounter()
        if node is None:
            return size
        size += 1
        return self.size_recursive_helper(node.next, size)

#------ END Recursive Helper Methods ------#
#------- END Courselist Class Definition -----#