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
        currnode = self.head
        if Course.number() < currnode.number():
            Course.next = currnode
            self.head = Course
            self.size_increment()
            return
        for i in range(0, self.size()):
            if Course.number() > currnode.number():
                if currnode.next == None:
                    currnode.next = Course
                    self.size_increment()
                    return
                elif Course.number() < currnode.next.number():
                    Course.next = currnode.next
                    currnode.next = Course
                    self.size_increment()
                    return
            currnode = currnode.next

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

    def __itr__(self):
        return
    
    def __next__(self):
        return


def main():
    course = Course(23.0, "cs 230", 3.0, 2.5)
    course = Course(230, 240, 3.0, 2.5)
    course = Course(230, "cs 230", 3, 2.5)
    course = Course(230, "cs 230", 3.0, 2)

main()