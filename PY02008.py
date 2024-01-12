from math import *
from sys import stdin
from functools import cmp_to_key
import queue


def prime(n):
    for  i in range(2 , int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True if n > 1 else False

def ger_prime(n):
    a = []
    num = 2
    while(len(a) < n):
        if prime(num):
            a.append(num)
        num += 1
    return a
def solve(n ,x):
    b = ger_prime(n)
    c = [x]
    for i in b:
        x += i
        c.append(x)
    return c

a , b = map(int , input().split())
res = solve(a , b)
print(res)
        
