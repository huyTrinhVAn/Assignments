from math import *
from sys import stdin
from functools import cmp_to_key
import queue

n = 10
res =set()
a = list()
while(len(a) < 10):
    b = list(map(int , input().split()))
    for i in b: 
        a.append(i)
for i in range(n):
    res.add(a[i] % 42)
print(len(res))