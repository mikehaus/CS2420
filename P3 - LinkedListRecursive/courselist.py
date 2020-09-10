from course import Course

class CourseList():

    def __init__(self):
        self.head = None
        self.listsize = 0

    def insert(self, Course):
        """
        inserts course Course into list in ascending course number order
        """
        if self.size() == 0: 
            self.head = Course
            self.size_increment()
            return
        return self.insert_helper(self.head, Course)

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
        iterates through list. If found returns Node else returns
        -1
        """
        if self.head == None: return -1
        if self.head.number() == number: return number
        return self.traverse_recursive(self.head, number)

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
        return

    def is_sorted(self):
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

    def traverse_recursive(self, node, target):
        """
        Traverses list recursively and returns Course Node that
        matches with number value. Returns Node and if not found, returns
        Null
        """
        if node == None: return -1
        if node.number() == target: return target
        return self.traverse_recursive(node.next, target)

    def insert_helper(self, node, course):
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
        self.insert_helper(node.next, course)


def main():
    courselist = CourseList()
    course = Course(230, "cs 230", 3.0, 2.5)
    courselist.insert(course)
    course = Course(240, "cs 230", 3.0, 2.5)
    courselist.insert(course)
    course = Course(245, "cs 230", 3.0, 2.5)
    courselist.insert(course)
    course = Course(300, "cs 230", 3.0, 2.5)
    courselist.insert(course)
    course = Course(200, "cs 230", 3.0, 2.5)
    courselist.insert(course)
    course = Course(225, "cs 230", 3.0, 2.5)
    courselist.insert(course)
    course = Course(400, "cs 230", 3.0, 2.5)
    courselist.insert(course)
    course = Course(350, "cs 230", 3.0, 2.5)
    courselist.insert(course)

    print(str(courselist.find(230)))
    print(str(courselist.find(245)))
    print(str(courselist.find(400)))
    print(str(courselist.find(322)))
    print(str(courselist.find(200)))
    print(str(courselist.find(-1)))
    print(str(courselist.find("cat")))
    #course = Course(23.0, "cs 230", 3.0, 2.5)
    #course = Course(230, 240, 3.0, 2.5)
    #course = Course(230, "cs 230", 3, 2.5)
    #course = Course(230, "cs 230", 3.0, 2)

main()