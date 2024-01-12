from math import *
from sys import stdin
from functools import cmp_to_key
import queue

while True:
    a = list(map(int, input().split()))
    if a.count(0) == 4:
        break
    cnt = 0
    while a.count(a[0]) != 4:
        b = a.copy()
        for i in range(4):
            a[i] = abs(b[i] - b[(i + 1) % 4])
        cnt += 1
    print(cnt)