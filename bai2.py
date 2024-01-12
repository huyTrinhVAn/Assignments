from math import *
from sys import stdin
from functools import cmp_to_key
import queue

def check1(n):
    for i in range(2 , int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True if n > 1 else False 
def check(s):
    for i in range(len(s)):
        if i % 2 != int(s[i]) % 2:
            return False
    return True


for t in range(int(input())):
    s = input()
    res = s[-4:]
    if check1(int(res)):
        print('YES')
    else :
        print('NO')