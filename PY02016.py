from math import *
from sys import stdin
from functools import cmp_to_key
import queue

for t in range(int(input())):
    m , n = {} , int(input())
    a = list(map(int , input().split()))
    res = -10**9
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
        res = max(res, m[i])
    if(res <= n // 2):
        print('NO')
    else:
        ans = 10**9
        for i in m:
            if m[i] == res:
                ans = min(ans , i)
        print(ans)
    