from math import *
from sys import stdin
from functools import cmp_to_key
import queue

class time:
    def __init__(self,id, name, inh , outh):
        self.id = id
        self.name = name
        self.inh = inh
        self.outh = outh
        a = inh.split(':')
        b = outh.split(':')
        self.val = int(b[0]) *60 + int(b[1]) - int(a[0]) * 60 - int(a[1])
    def __str__(self):
        return f'{self.id} {self.name} {(self.val) // 60} gio {(self.val)  % 60} phut'
a = list()
for i in range(int(input())):
    id = input()
    name = input()
    inh = input()
    outh = input()
    b = time(id , name, inh , outh)
    a.append(b)
a.sort(key = lambda self : (-self.val))
for i in a:
    print(i)            