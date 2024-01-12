from math import *
from sys import stdin
from functools import cmp_to_key
import queue
from datetime import datetime, timedelta


class Employee:
    def __init__(self, id, name, gender, dob_str, address, tax_id, contract_date_str):
        self.id = id
        self.name = name
        self.gender = gender
        self.dob = datetime.strptime(dob_str, '%d/%m/%Y')
        self.address = address
        self.tax_id = tax_id
        self.contract_date = datetime.strptime(contract_date_str, '%d/%m/%Y')

    def __str__(self):
        return f'{self.id} {self.name} {self.gender} {self.dob.strftime("%d/%m/%Y")} {self.address} {self.tax_id} {self.contract_date.strftime("%d/%m/%Y")}'


t = int(input())

employees = []


for i in range(t):
    id = '{:05d}'.format(i + 1)
    name = input()
    gender = input()
    dob_str = input()
    address = input()
    tax_id = input()
    contract_date_str = input()

    emp = Employee(id, name, gender, dob_str, address, tax_id, contract_date_str)
    employees.append(emp)


employees.sort(key=lambda emp: emp.dob)


for emp in employees:
    print(emp)
