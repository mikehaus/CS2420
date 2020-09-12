"""
Course Class Declaration
CS2420 - P3 Recursive Linked List
course.py
Mike Hollingshaus
"""

#-------- START Course Class Definition ------#

class Course:
    """
    Course class which stores the attributes of a class
    and provides basic methods for retrieving said attrs
    from class.

    KEY ATTRIBUTES:
    number - Course number as Integer
    name - Course name as String
    credit_hr - Course Credit Hours as float
    grade - Grade as float
    """
    def __init__(self, number, name, credit_hr, grade):
        """
        Init function for Course Class.
        """
        if not isinstance(number, int):
            raise TypeError
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(credit_hr, float):
            raise TypeError
        if not isinstance(grade, float):
            raise TypeError
        self.coursenumber = number
        self.coursename = name
        self.coursecredit_hr = credit_hr
        self.coursegrade = grade
        self.next = None
        self.prev = None

    def number(self):
        """returns attr course number"""
        return self.coursenumber

    def name(self):
        """returns attr course name"""
        return self.coursename

    def credit_hr(self):
        """returns attr credit hours"""
        return self.coursecredit_hr

    def grade(self):
        """returns attr grade"""
        return self.coursegrade

    def __str__(self):
        """returns formatted string as req'd by output"""
        return 'cs {self.coursenumber} {self.coursename} Grade: {self.coursegrade} \
          Credit Hours: {self.coursecredit_hr}\n'.format(self = self)

#-------- END Course Class Definition -------#
