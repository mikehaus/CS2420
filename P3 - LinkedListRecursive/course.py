
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
        if not isinstance(number, int): raise TypeError
        if not isinstance(name, str): raise TypeError
        if not isinstance(credit_hr, float): raise TypeError
        if not isinstance(grade, float): raise TypeError
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
        return 'cs' + str(number()) + name() + ' Grade:' + str(grade()) + ' Credit Hours: ' + str(credit_hr())
