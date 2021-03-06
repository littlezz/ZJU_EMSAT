__author__ = 'zz'



from mainapp.models import CourseLesson
from random import shuffle

import logging
logging.basicConfig(level=logging.WARNING, format='%(message)s' ,)

MAXCOURSES = 13
EXCLUDE = (2, 4, 5, 8, 10, 12, 13)
#humanread(1, 3, 6, 7, 9, 11)
STARTAT = (0, 2, 5, 6, 8, 10)
WEEK = (1, 2, 3, 4, 5, 6, 7)
supportkey = ('code', 'arrange','season', 'status')  # 确保status在最后
#SEASON = ('春', '夏', '秋', '冬')
SEASON = (0, 1, 2, 3)





class Day:
    """

    data struct:
        data[season][WEEK][STARTAT][supportkey]
        for example,
        data[0][1][2]['name'],
        name of the Second lesson on Monday on spring term
    """



    def __init__(self, whichseason, whichday, table, credit_manager):
        self.table = table
        self.nowday = table[whichseason][whichday]
        self.whichseason = whichseason
        self.whichday = whichday
        self.credit_manager = credit_manager

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

        if course.season:
            seasons = list(map(int,course.season.split(',')))
        else:
            return False

        if course.firstcourse:
            whichday1, *coursetimes1 = map(int,course.firstcourse.split(','))

            if any(self.table[j][whichday1][i] for j in seasons for i in coursetimes1):

                return False
        else:
            return False

        if course.secondcourse:
            whichday2, *coursetimes2 = map(int,course.secondcourse.split(','))
            if any(self.table[j][whichday2][i] for j in seasons for i in coursetimes2):
                return False


        for i in coursetimes1:
            self.course_table_update(seasons, whichday1, i, course, 1)

        if course.secondcourse:
            for i in coursetimes2:
                self.course_table_update(seasons, whichday2, i, course, 1)


        self.credit_manager.add(course.code, course.credit)
        return True

    def course_table_update(self, seasons, whichday, whichcourse, newcourse, status):

        for whichseason in seasons:
            self.table[whichseason][whichday][whichcourse] = dict((key, getattr(newcourse, key)) for key in supportkey[:-1])
            self.table[whichseason][whichday][whichcourse].update(status=status)




class Credit:
    def __init__(self):
        self.credit = 0
        self._dict = dict()
    def add(self, coursecode, coursecredit):
        if coursecode not in self._dict:
            self._dict[coursecode] = coursecredit
            self.credit += coursecredit

    def remove(self,coursecode):
        if coursecode in self._dict:
            discard_credit = self._dict.pop(coursecode)
            self.credit -= discard_credit


class Table:


    def __init__(self, table=None):
        self.table = table if table else dict((j,dict((i, [None]*13) for i in WEEK)) for j in SEASON)
        self.week = WEEK
        self.season = SEASON
        self.credit_manager = Credit()
    def user_fullcourse(self):

        for whichseason in self.season:
            for whichday in self.week:
                day = Day(whichseason, whichday, self.table)
                day.full()




