from math import *
from sys import stdin
from functools import cmp_to_key
import queue

for t in range(int(input())):
    n = int(input())
    k = int(input())
    print(str(n).count(str(k)))