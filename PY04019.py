from math import *
from sys import stdin
from functools import cmp_to_key
import queue

class employee:
    def __init__(self , id ,name, thm,prm):
        self.id = id
        self.name = name
        self.thm = thm
        self.prm = prm
        while self.thm > 10 : self.thm /= 10
        while self.prm > 10 : self.prm /= 10
        self.total = (self.thm + self.prm) / 2
        if self.total > 9.5: self.status = "XUAT SAC"
        elif self.total >= 8: self.status = "DAT"
        elif self.total >= 5: self.status = "CAN NHAC"
        else: self.status = "TRUOT"
    def __str__(self):
        return f'{self.id} {self.name} {self.total:.2f} {self.status}'

a = list()

for i in range(int(input())):
    id = 'TS0{:d}'.format(i + 1)
    name = input()
    thm = float(input())
    prm = float(input())
    b = employee(id, name,thm,prm)
    a.append(b)
a.sort(key = lambda self : -self.total )
for i in a:
    print(i)