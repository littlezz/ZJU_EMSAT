__author__ = 'zz'

"""
import  os,sys
sys.path.append('/home/zz/program/baiduclub/EMSAT')
os.environ['DJANGO_SETTINGS_MODULE'] = 'EMSAT.settings'
from django.conf import settings
"""

from mainapp.lib import choose

t=choose.Table()
t.user_fullcourse()
