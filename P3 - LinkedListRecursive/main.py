"""
Main driver file for
Project 3 2420
Mike Hollingshaus
"""
from course import Course
from courselist import CourseList

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
    course_data = []
    filelines = file.readlines()
    for line in filelines:
        course_data = []
        lineparsed = line_parse(line)
        for part in lineparsed:
            course_data.append(part)
        course = Course(int(course_data[0]), course_data[1], float(course_data[2]), float(course_data[3]))
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
    file.close()
    print(str(course_list))

main()
