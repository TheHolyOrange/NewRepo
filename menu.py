import sys
sys.path.append('E:\Tanisha\PYTHON\DatabaseLayer')

import csv

import clear
import display
import update
import delete
import add

def menu():
    a=int(input("1)add a record\n2)display records\n3)update records\n4)clear all records\n5)delete records\n"))
    if a==1:
        add.add()
        menu()
    elif a==2:
        display.display()
        menu()
    elif a==3:
        update.update()
        menu()
    elif a==4:
        clear.clear()
        menu()
    elif a==5:
        delete.delete()
        menu()

menu()

