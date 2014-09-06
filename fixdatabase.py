__author__ = 'zz'


def fix_season():
    from mainapp.models import CourseLesson
    SEASON = ('春', '夏', '秋', '冬')
    a=CourseLesson.objects.all()
    for i in a:
        seasons=[]
        for j in i.term:
            seasons.append(str(SEASON.index(j)))
        i.season = ','.join(seasons)
        i.save()


