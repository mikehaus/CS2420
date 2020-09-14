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
    def __init__(self, number = 0, name = "", credit_hr = 0.0, grade = 0.0):
        """
        Init function for Course Class.
        """
        if not isinstance(number, int):
            raise ValueError
        if not isinstance(name, str):
            raise ValueError
        if not isinstance(credit_hr, float):
            raise ValueError
        if not isinstance(grade, float):
            raise ValueError
        self._name = name
        self._number = number
        self._credit_hr = credit_hr
        self._grade = grade
        self.next = None
        self.prev = None

    def number(self):
        """returns attr course number"""
        return self._number

    def name(self):
        """returns attr course name"""
        return self._name

    def credit_hr(self):
        """returns attr credit hours"""
        return self._credit_hr

    def grade(self):
        """returns attr grade"""
        return self._grade

    
    def __str__(self):
        """returns formatted string as req'd by output"""
        return 'cs {self.number} {self.name} Grade: {self.grade} \
          Credit Hours: {self.credit_hr}\n'.format(self = self)

#-------- END Course Class Definition -------#
