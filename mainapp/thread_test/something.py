__author__ = 'acer'

import time
import queue

q= queue.deque()
class T:

    def __init__(self, schoolid):
        self.profile = str(time.time())+schoolid


def scope_test(schoolid):
    a=T(schoolid)
    q.append(a)
    return q
