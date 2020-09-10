from course import Course

"""
CS2420 - P3 Recursive Linked List
courselist.py
Mike Hollingshaus
"""

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

    def insert(self, Course):
        """
        Inserts course Course into list in ascending course number order
        """
        if self.size() == 0: 
            self.head = Course
            self.size_increment()
            return
        return self.insert_recursive_helper(self.head, Course)

    def remove(self, number):
        """
        Removes first occurance of course with
        course number number
        """
        return
    
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
        if self.head == None: return -1
        if self.head.number() == number: return number
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
        return
    
    def __str__(self):
        return

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

    def traverse_recursive_find_helper(self, course, target):
        """
        Traverses list recursively and returns Course Node that
        matches with number value. Returns course number if found 
        and if not found, returns Null
        """
        if course == None: return -1
        if course.number() == target: return target
        return self.traverse_recursive(course.next, target)

    def traverse_recursive_gpa_helper(self, course, grade_point_total):
        """
        Traverses list recursively and returns Course Node that
        matches with number value. Returns Node and if not found, returns
        Null
        """
        if course == None: return grade_point_total
        grade_point_total += course.grade()
        return self.traverse_recursive_gpa_helper(course.next, grade_point_total)

    def insert_recursive_helper(self, node, course):
        """
        Recursively inserts node
        """
        if course.number() < node.number():
            course.next = node
            course.prev = node.prev
            if course.prev != None: course.prev.next = course
            node.prev = course
            if node == self.head: self.head = course
            self.size_increment()
            return
        if node.next == None:
            node.next = course
            course.prev = node
            self.size_increment()
            return
        self.insert_recursive_helper(node.next, course)


def main():
    courselist = CourseList()
    print(str(courselist.calculate_gpa()))
    course = Course(230, "cs 230", 2.0, 2.0)
    courselist.insert(course)
    print(str(courselist.calculate_gpa()))
    course = Course(240, "cs 230", 4.0, 4.0)
    courselist.insert(course)
    print(str(courselist.calculate_gpa()))
    course = Course(245, "cs 230", 3.2, 3.2)
    courselist.insert(course)
    print(str(courselist.calculate_gpa()))
    course = Course(300, "cs 230", 1.5, 1.5)
    courselist.insert(course)
    print(str(courselist.calculate_gpa()))
    course = Course(200, "cs 230", 3.3, 3.3)
    courselist.insert(course)
    print(str(courselist.calculate_gpa()))
    course = Course(225, "cs 230", 3.8, 3.8)
    courselist.insert(course)
    print(str(courselist.calculate_gpa()))
    course = Course(400, "cs 230", 1.2, 1.2)
    courselist.insert(course)
    print(str(courselist.calculate_gpa()))
    course = Course(350, "cs 230", 3.0, 3.0)
    courselist.insert(course)
    print(str(courselist.calculate_gpa()))

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