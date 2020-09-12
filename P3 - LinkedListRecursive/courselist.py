"""
CourseList Class declaration
CS2420 - P3 Recursive Linked List
courselist.py
Mike Hollingshaus
"""
from course import Course

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
        self.listsize = 0

    def insert(self, course):
        """
        Inserts course Course into list in ascending course number order
        """
        if self.size() == 0:
            self.head = course
            self.size_increment()
            return
        return self.insert_recursive_helper(self.head, course)

    def remove(self, number):
        """
        Removes first occurance of course with
        course number number
        """
        if self.head is None:
            return
        return self.remove_recursive_helper(self.head, number)

    def remove_all(self, number):
        """
        Sets head to equal NULL which will get rid of all data in list.
        """
        self.head = None
        self.listsize = 0
        return

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
        return self.listsize

    def size_increment(self):
        """
        Increments list size.
        """
        self.listsize += 1

    def size_decrement(self):
        """
        Decrements List Size.
        """
        self.listsize -= 1

    def calculate_gpa(self):
        """
        Calculates GPA based on grade attribute stored in Course Node class.
        Might need to be weighted not sure.
        """
        if self.size() == 0:
            return 0.0
        grade_point_total = self.traverse_recursive_gpa_helper(self.head, 0.0)
        return grade_point_total / self.size()

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
        self.itr = 0
        return self

    def __next__(self):
        """
        Increments the iterator attr for CourseList.
        """
        itr = self.itr
        self.itr += 1
        return itr

#------ START Recursive Helper Methods -------#

    def traverse_recursive_string_helper(self, course, course_string):
        """
        Traverses recursively through list and concatentates
        all Course str functions into a single string.
        """
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
        if course is None:
            return -1
        if course.number() == target:
            return target
        return self.traverse_recursive(course.next, target)

    def traverse_recursive_gpa_helper(self, course, grade_point_total):
        """
        Traverses list recursively and returns Course Node that
        matches with number value. Returns Node and if not found, returns
        Null
        """
        if course is None:
            return grade_point_total
        grade_point_total += course.grade()
        return self.traverse_recursive_gpa_helper(course.next, grade_point_total)

    def traverse_recursive_sorted_helper(self, course, last_course_num):
        """
        Traverses list recursively and validates classes are in order.
        Returns True if Sorted False if Unsorted
        """
        if course is None:
            return True
        if course.number() < last_course_num:
            return False
        return self.traverse_recursive_sorted_helper(course.next, course.number())

    def insert_recursive_helper(self, node, course):
        """
        Recursively inserts node
        """
        if course.number() < node.number():
            course.next = node
            course.prev = node.prev
            if course.prev != None:
                course.prev.next = course
            node.prev = course
            if node == self.head:
                self.head = course
            self.size_increment()
            return
        if node.next is None:
            node.next = course
            course.prev = node
            self.size_increment()
            return
        self.insert_recursive_helper(node.next, course)

    def remove_recursive_helper(self, node, course_num):
        """
        Recursive function that removes node Course from list if
        course_num matches node.number (coursenumber)
        """
        if node is None:
            return
        if node.number() == course_num:
            node.prev.next = node.next
            node.next.prev = node.prev
            return
        return self.remove_recursive_helper(node.next, course_num)

#------ END Recursive Helper Methods ------#
#------- END Courselist Class Definition -----#

def main():
    courselist = CourseList()
    #print(str(courselist.calculate_gpa()))
    course = Course(230, "Data Structures", 2.0, 2.0)
    courselist.insert(course)
    #print(str(courselist.calculate_gpa()))
    course = Course(240, "Discrete Math", 4.0, 4.0)
    courselist.insert(course)
    #print(str(courselist.calculate_gpa()))
    course = Course(245, "Hardware", 3.2, 3.2)
    courselist.insert(course)
    #print(str(courselist.calculate_gpa()))
    course = Course(300, "Linux", 1.5, 1.5)
    courselist.insert(course)
    #print(str(courselist.calculate_gpa()))
    course = Course(200, "Intro to Circuits", 3.3, 3.3)
    courselist.insert(course)
    #print(str(courselist.calculate_gpa()))
    course = Course(225, "Research Lab", 3.8, 3.8)
    courselist.insert(course)
    #print(str(courselist.calculate_gpa()))
    course = Course(400, "Advanced Algorithms", 1.2, 1.2)
    courselist.insert(course)
    #print(str(courselist.calculate_gpa()))
    course = Course(350, "Mobile Development", 3.0, 3.0)
    courselist.insert(course)
    #print(str(courselist.calculate_gpa()))

    #print(str(courselist.is_sorted()))

    print(courselist.__str__())
    print(" ")
    courselist.remove(240)
    print(courselist.__str__())
    course = Course(226, "Hardware AGAIN", 3.5, 3.5)
    courselist.insert(course)
    print(courselist.__str__())

    """print(str(courselist.find(230)))
    print(str(courselist.find(245)))
    print(str(courselist.find(400)))
    print(str(courselist.find(322)))
    print(str(courselist.find(200)))
    print(str(courselist.find(-1)))
    print(str(courselist.find("cat")))"""
    #course = Course(23.0, "cs 230", 3.0, 2.5)
    #course = Course(230, 240, 3.0, 2.5)
    #course = Course(230, "cs 230", 3, 2.5)
    #course = Course(230, "cs 230", 3.0, 2)

main()
