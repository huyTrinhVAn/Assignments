from math import *
from sys import stdin
from functools import cmp_to_key
import queue

class candidate:
    sum = 0
    def __init__(self , name , date, s1 ,s2 ,s3):
        self.name = name
        self.date = date
        self.s1 = s1
        self.s2 =s2
        self.s3 = s3
        self.sum = s1 + s2  + s3
    def __str__(self):
        return f'{self.name} {self.date} {self.sum:.1f}'
    
name = input()
date = input()
s1 = float(input())
s2 =float(input())
s3 =float(input())
a = candidate(name,date, s1 , s2, s3)
print(a)