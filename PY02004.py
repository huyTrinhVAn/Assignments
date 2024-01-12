from math import *
from sys import stdin
from functools import cmp_to_key
import queue


n = int(input())
a = list(int(i) for i in input().split())
cnt = 0
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        cnt+= 1
print(cnt)

