from math import *
class SV:
    def __init__(self, mhs, ten, dtb, xl):
        self.mhs = mhs
        self.ten = ten
        self.dtb = dtb
        self.xl = xl
    def change(self):
        self.mhs = "HS" + format(mhs, '02d')
        if self.dtb >= 9 :
            self.xl = "XUAT SAC"
        elif self.dtb >= 8 and self.dtb < 9 :
            self.xl = "GIOI"
        elif self.dtb >= 7 and self.dtb < 8 :
            self.xl = "KHA"
        elif self.dtb >= 5 and self.dtb < 7 :
            self.xl = "TB"
        else :
            self.xl = "YEU"
    def __str__(self):
        return f'{self.mhs} {self.ten} {round(self.dtb + 0.01, 1)} {self.xl}'
# int main :
a = []
n = int(input())
for i in range(n) :
    mhs = i + 1
    ten = input()
    b = list(map(float, input().split()))
    tong = 0
    for j in range(len(b)) :
        if j == 0 or j == 1 :
            tong += b[j] * 2
        else :
            tong += b[j]
    tong /= (len(b) + 2)
    sv = SV(mhs, ten, tong, "")
    sv.change()
    a.append(sv)
a.sort(key = lambda self : (-self.dtb))
for i in a :
    print(i)