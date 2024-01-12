from math import *
from sys import stdin
from functools import cmp_to_key
import queue


class bill:
    def __init__(self , id , name, old ,new):
        self.id = id 
        self.name = name
        self.old = old
        self.new =new
        s = new - old
        if s <= 50:
            s *= 100
            s += s * 0.02
        elif s >= 51 and s <= 100:
            s = 50 * 100 + (s-50) * 150 
            s += s * 0.03
        else:
            s = 50 * 100 + 50 * 150 + (s - 100) * 200
            s += s * 0.05
        self.tien = round(s)
    def __str__(self):
        return f'{self.id} {self.name} {self.tien}'

a = list()
for i in range(int(input())):
    id = 'KH{:02d}'.format(i + 1)
    name = input()
    old = int(input())
    new = int(input())
    sv = bill(id, name, old ,new)
    a.append(sv)
a.sort(key = lambda self : -self.tien)
for i in a:
    print(i)