from math import *
from sys import stdin
from functools import cmp_to_key
import queue


for t in range(int(input())):
    a = list(int(i) for i in input())
    sum , mul = 0 , 0
    for i in range(len(a)):
        if i % 2 == 0 :
            sum += a[i]
        else:
            if a[i] != 0:
                if mul == 0:
                    mul = a[i]
                else :
                    mul *= a[i]
    print(str(sum) + " " + str(mul))
    