from math import *
from sys import stdin
from functools import cmp_to_key
import queue

def check(n):
    for i in range(2 , int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True if n > 1 else  False

for t in range(int(input())):
    a = list(int(i) for i in input())
    l , cnt = len(a) , 0
    for i in range(len(a)):
        if check(a[i]):
            cnt += 1
    if (cnt > l - cnt ) and check(l):
        print('YES')
    else:
        print('NO')