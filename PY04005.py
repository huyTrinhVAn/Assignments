from math import *
from sys import stdin
from functools import cmp_to_key
import queue


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        x1 = self.x - p.x
        y1 = self.y - p.y
        return sqrt(pow(x1, 2) + pow(y1, 2))

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def solve(self):
        ab = self.p1.distance(self.p2)
        bc = self.p2.distance(self.p3)
        ca = self.p3.distance(self.p1)
        if max(ab, bc, ca) * 2 >= ab + bc + ca:
            print('INVALID')
        else:
            print('{:.3f}'.format(ab + bc + ca))

# Đọc số bộ test
t = int(input())

for _ in range(t):
    a = list(map(float, input().split()))
    i = 0
    for _ in range(1):
        triangle = Triangle(Point(a[i], a[i + 1]), Point(a[i + 2], a[i + 3]), Point(a[i + 4], a[i + 5]))
        triangle.solve()
        i += 6
