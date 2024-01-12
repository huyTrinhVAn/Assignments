from math import *
from sys import stdin
from functools import cmp_to_key
import queue

def prime(n):
    for i in range(2 , int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True if n > 1 else False

n = int(input())
a = list(map(float, input().split()))
b = list()
ma , mi = max(a) , min(a)
for i in a:
    if i != ma and i != mi:
        b.append(i)
print('{:.2f}'.format(sum(b) / len(b)))