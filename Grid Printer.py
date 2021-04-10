# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:01:19 2021

@author: saduq.rahman
"""

def grid(n):
    x = ('+----' * n + '+')
    y = ('\n' +'|    ' *  (n+1)) 
    return ((x + 4*y) +'\n')*n + x
print(grid(3))
print(grid(15))


def grid(row,col):
    x = ("+-----" * col + "+")
    y = ("\n" + "|     " * (col+1))
    return ((x + 4*y) +"\n")*row + x
print(grid(3,3))
print(grid(5,5))


def print_beams(a):
    print("+", end="")
    for i in range(a-1):
        print("-----+",end="")
    print("-----+")  

def print_row(a):
    print("|", end="")
    for i in range(a-1):
        print("     |", end="")
    print("     |")

def print_grid(a,b):
    print_beams(a)
    for i in range(b):
        for i in range(4):
            print_row(a)
        print_beams(a)

a=6
b=5
print_grid(a, b)
