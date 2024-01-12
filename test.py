from math import *
from sys import stdin
from functools import cmp_to_key
import queue
from datetime import datetime, timedelta
class bill:
    def __init__(self, id , name, room,  ind , outd,fee ):
        self.id = id
        self.name = name
        self.room = room
        self.ind = datetime.strptime(ind , '%d/%m/%Y')
        self.outd = datetime.strptime(outd , '%d/%m/%Y')
        self.fee = fee
        if(int(room[0]) == 1):
            price = 30
        elif(int(room[0]) == 2):
            price = 45 
        elif(int(room[0]) == 3):
            price = 50
        elif(int(room[0]) == 4):
            price = 65
        elif(int(room[0]) == 5):
            price = 72
        elif(int(room[0]) == 6):
            price = 85
        elif(int(room[0]) == 7):
            price = 90
        elif(int(room[0]) == 8):
            price = 120
        else:
            price = 150

        self.stay = (self.outd - self.ind).days + 1
        self.total_price = price * int(self.stay) + fee
    def __str__(self):
        return f'{self.id} {self.name} {self.room} {self.stay} {self.total_price}'  

a = list()
for i in range(int(input())):
    id = 'KH{:02d}'.format(i + 1)
    name = input()
    room = input()
    ind = input()
    outd = input()
    fee = int(input())
    b = bill(id, name, room, ind, outd, fee)
    a.append(b)
a.sort(key = lambda self: (-self.total_price,self.stay))
for i in a:
    print(i)
        

