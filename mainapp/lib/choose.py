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
supportkey = ('name', 'time', 'status')  #记得在course_table_update 中也修改
#SEASON = ('春', '夏', '秋', '冬')
SEASON = (0, 1, 2, 3)







class Day:
    """
    data struct:
        data[WEEK][STARTAT][supportkey]
        for example,
        data[1][2]['name'],
        name of the Second lesson on Monday



    data struct:
        data[season][WEEK][STARTAT][supportkey]
        for example,
        data[0][1][2]['name'],
        name of the Second lesson on Monday on spring term
    """



    def __init__(self, whichseason, whichday, table):
        self.table = table
        self.nowday = table[whichseason][whichday]
        self.whichseason = whichseason
        self.whichday = whichday


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



        return True

    def course_table_update(self, seasons, whichday, whichcourse, newcourse, status):

        for whichseason in seasons:
            self.table[whichseason][whichday][whichcourse] = {
                                                    'name': newcourse.code,
                                                    'time': newcourse.arrange,
                                                    'status': status,
                                                    }


"""
class Season:


    def __init__(self, season, week=WEEK):
        self.season = season
        self.week = week

    def user_fullcourse(self):

"""


class Table:


    def __init__(self, table=None):
        self.table = table if table else dict((j,dict((i, [None]*13) for i in WEEK)) for j in SEASON)
        self.week = WEEK
        self.season = SEASON
    def user_fullcourse(self):

        #for whichday in self.week:
        #    day = Day(whichday, self.table)
        #    day.full()
        for whichseason in self.season:
            for whichday in self.week:
                day = Day(whichseason, whichday, self.table)
                day.full()




