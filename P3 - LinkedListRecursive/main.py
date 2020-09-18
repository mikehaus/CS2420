import sys
from course import Course
from courselist import CourseList

"""
Main driver file for 
Project 3 2420
Mike Hollingshaus
"""

def line_parse(line):
    """
    Parse an individual line for charachers 
    and append them to returned line
    """
    parsed_course = line.split(',', 4)
    return parsed_course

def parser(file, course_list):
    """
    Parse text of filepath file
    """
    courseData = []
    filelines = file.readlines()
    for line in filelines:
        courseData = []
        lineparsed = line_parse(line)
        for part in lineparsed:
            courseData.append(part)
            print(part)
        course = Course(int(courseData[0]), courseData[1], float(courseData[2]), float(courseData[3]))
        course_list.insert(course)

    return course_list

def main():
    """
    main function driver for reading in file and then
    processing input.
    NOTE: I have my own test code commented out below
    """
    course_list = CourseList()
    file = open('data.txt', 'r')
    course_list = parser(file, course_list)    


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