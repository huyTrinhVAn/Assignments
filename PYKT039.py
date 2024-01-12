from math import *
from sys import stdin
from functools import cmp_to_key
import queue

def check(n , a , b):
    for i in range(n):
        if a[i] > b[i] :
            return 0
    return 1

for t in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    if check( n , a , b) == 1:
       print('YES')
    else:
       print('NO')