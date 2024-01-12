from math import *
from sys import stdin
from functools import cmp_to_key
import queue
from datetime import datetime, timedelta

s = input()
a = list(s.split())
a[-1] = a[-1].upper()
for i in range(0 ,len(a) - 1):
    a[i] = a[i].title()
for i in range(0,len(a) - 1):
    if i != len(a) - 1:
        print(a[i], end = ' ')
    else:
        print(a[i], end =', ')
print(a[-1])