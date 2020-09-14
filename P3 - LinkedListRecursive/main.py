from course import Course
from courselist import CourseList

def main():
    """
    main function primarily for testing
    """
    cl = CourseList()
    cl.insert(Course(1000))
    for _ in range(20):
        cl.insert(Course(1200))
    totalCourses = 0
    for _ in cl:
        totalCourses += 1
    print(str(cl.listsize))
    
    """courselist = CourseList()
    #print(str(courselist.calculate_gpa()))
    course = Course()
    courselist.insert(course)
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
    print(courselist.__str__())"""

    """print(str(courselist.find(230)))
    print(str(courselist.find(245)))
    print(str(courselist.find(400)))
    print(str(courselist.find(322)))
    print(str(courselist.find(200)))
    print(str(courselist.find(-1)))
    print(str(courselist.find("cat")))
    """#course = Course(23.0, "cs 230", 3.0, 2.5)
    #course = Course(230, 240, 3.0, 2.5)
    #course = Course(230, "cs 230", 3, 2.5)
    #course = Course(230, "cs 230", 3.0, 2)

    

main()