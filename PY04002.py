from math import *
from sys import stdin
from functools import cmp_to_key
import queue

class Rectangle :
    def __init__(self, dai, rong, mau):
        self.dai = dai
        self.rong = rong
        self.mau = mau.title()
    def __str__(self):
        if(self.dai <= 0 or self.rong <= 0) :
            return "INVALID"
        else :
            return f'{(self.rong + self.dai) * 2} {self.rong * self.dai} {self.mau}'
s = input().split()
rec = Rectangle(int(s[0]), int(s[1]), s[2])
print(rec)