from math import *
from sys import stdin
from functools import cmp_to_key
import queue

class pso:
    def __init__(self, t ,m):
        self.t = t
        self.m = m
    def __str__(self):
        u = gcd(self.t , self.m)
        self.t //= u
        self.m //= u
        return f'{self.t}{"/"}{self.m}'
    
if __name__ == "__main__":
          a = list(map(int ,input().split()))
          t1 = a[0]
          m1 = a[1]
          t2 = a[2]
          m2 = a[3]
          print(pso(t1 * m2 + t2 * m1 , m1 * m2))
  
