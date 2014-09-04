__author__ = 'zz'


from itertools import groupby
from mainapp.models import CourseLesson
from random import shuffle

import logging
logging.basicConfig(level=logging.WARNING, format='%(message)s' ,)

MAXCOURSES = 13
EXCLUDE = (2, 4, 5, 8, 10, 12, 13)
#humanread(1, 3, 6, 7, 9, 11)
STARTAT = (0, 2, 5, 6, 8, 10)
WEEK = (1, 2, 3, 4, 5, 6, 7)
supportkey = ('name', 'time', 'status')
#记得在course_table_update 中也修改






class CustomList(list):
    """
    Normal list index start at 0, but the courses index start at 1.
    rewrite the setitem and getitem,everytime key = key-1
    """
    def __setitem__(self, key, value):
        super(list, self).__setitem__(key-1, value)

    def __getitem__(self, item):
        return super(list, self).__getitem__(item-1)




class Day:
    """
    data struct:
        data[WEEK][STARTAT][supportkey]
        for example,
        data[1][2]['name'],
        name of the Second lesson on Monday
    """



    def __init__(self, whichday, table):
        self.table = table
        self.whichday = whichday
        self.nowday = table[whichday]

    def full(self):
        freetime = (num for (num, i) in enumerate(self.nowday) if (not i) and  (num in STARTAT) )



        for time in freetime:
            if not self.nowday[time]:
                temp = CourseLesson.objects.filter(startday=self.whichday).filter(startcourse=time)
                courses = list(temp)
                shuffle(courses)
                logging.debug(courses[:5])
                for course in courses:
                    success = self._try_putin(course)
                    if success:
                        break

    def _try_putin(self,course):
        logging.debug(course)
        if course.firstcourse:
            whichday1, *coursetimes1 = map(int,course.firstcourse.split(','))

            if any(self.table[whichday1][i] for i in coursetimes1):
                return False
        else:
            return False

        if course.secondcourse:
            whichday2, *coursetimes2 = map(int,course.secondcourse.split(','))
            if any(self.table[whichday2][i] for i in coursetimes2):
                return False


        for i in coursetimes1:
            self.course_table_update(whichday1, i, course, 1)

        if course.secondcourse:
            for i in coursetimes2:
                self.course_table_update(whichday2, i, course, 1)

        print(course.arrange)

        return True

    def course_table_update(self, whichday, whichcourse, newcourse, status):
        self.table[whichday][whichcourse] = {
                                                'name': newcourse.code,
                                                'time': newcourse.arrange,
                                                'status': status,
                                                }








class Table:
    week = WEEK
    voidtable = dict((i, [None]*13) for i in WEEK)

    def __init__(self, table=None):
        self.table = table if table else self.voidtable

    def user_fullcourse(self):
        for whichday in self.week:
            day = Day(whichday, self.table)
            day.full()





