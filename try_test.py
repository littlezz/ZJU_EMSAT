__author__ = 'zz'

"""
import  os,sys
sys.path.append('/home/zz/program/baiduclub/EMSAT')
os.environ['DJANGO_SETTINGS_MODULE'] = 'EMSAT.settings'
from django.conf import settings
"""

#import os
#import sys
#sys.path.append(os.getcwd())
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EMSAT.settings")
#from django.conf import settings
from mainapp.models import  CourseLesson
a=CourseLesson.objects.get(pk=1)
print(a)


