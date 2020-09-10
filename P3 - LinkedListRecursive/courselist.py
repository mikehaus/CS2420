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
        return
    
    def find(self, number):
        return

    def size(self):
        return self.listsize

    def size_increment(self):
        self.listsize += 1

    def size_decrement(self):
        self.listsize -= 1

    def calculate_gpa(self):
        return

    def is_sorted(self):
        return
    
    def __str__(self):
        return

    def insert_helper(self, Node, Course):
        """
        Recursively inserts node
        """
        if Course.number() < Node.number():
            Course.next = Node
            Course.prev = Node.prev
            if Course.prev != None:
                Course.prev.next = Course
            Node.prev = Course
            if Node == self.head:
                self.head = Course
            self.size_increment()
            return
        if Node.next == None:
            Node.next = Course
            Course.prev = Node
            self.size_increment()
            return
        self.insert_helper(Node.next, Course)


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
    course = Course(23.0, "cs 230", 3.0, 2.5)
    course = Course(230, 240, 3.0, 2.5)
    course = Course(230, "cs 230", 3, 2.5)
    course = Course(230, "cs 230", 3.0, 2)

main()