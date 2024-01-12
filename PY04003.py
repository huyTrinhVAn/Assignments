from math import *
from sys import stdin
from functools import cmp_to_key
import queue


class pso:
    def __init__(self , t ,m):
        self.t = t
        self.m = m
    def __str__(self):
        m = gcd(self.t , self.m)
        self.t //= m
        self.m //= m
        return f'{self.t}{"/"}{self.m}'
    
if __name__ == "__main__":
    a = list(map(int ,input().split()))
    a = pso(a[0] , a[1])
    print(a)
    