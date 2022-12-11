from AOC import * 
import collections
import math
import itertools
import time
import random
import pandas as pd
import numpy as np


DAY = 8
DEBUG = False
s = [[int(y) for y in x ]for x in get_input(DAY).strip().split('\n')]
# s = [[int(y) for y in x ]for x in get_example(DAY).strip().split('\n')]

# PART 1 
PART = 1
ANS = 0

def tcheck(y,x):
    tmpy = y
    tmpx = x -1
    test = 0
    while tmpx >=0:
        if s[y][x] <= s[tmpy][tmpx]:
            test+=1
            break

        tmpx -=1

    tmpx = x +1

    while tmpx <len(s[0]):
        if s[y][x] <= s[tmpy][tmpx]:
            test+=1
            break
        tmpx +=1

    tmpx = x
    tmpy -=1

    while tmpy >= 0:

        if s[y][x] <= s[tmpy][tmpx]:
            test+=1
            break
        tmpy -=1
    tmpy = y+1

    while tmpy < len(s):
        if s[y][x] <= s[tmpy][tmpx]:
            test+=1
            break
        tmpy +=1
       
    if test == 4:
        return False
    else:
        return True
   
for y in range(len(s)):
    for x in range(len(s[0])):        
        if tcheck(y, x):
            ANS +=1

if(ANS and not DEBUG):    
    submit(DAY, PART, ANS)
else:
    print(f"[DEBUG] Part 1 : {ANS}")

#part 2
PART = 2
ANS = 0

def tcheck2(y,x):
    tmpy = y
    tmpx = x -1
    test = 0
    a,b,c,d = 0,0,0,0
    while tmpx >=0:
        if s[y][x] <= s[tmpy][tmpx]:
            a+=1
            test+=1
            break
        a+=1
        tmpx -=1
    tmpx = x +1

    while tmpx <len(s[0]):
        if s[y][x] <= s[tmpy][tmpx]:
            b+=1
            test+=1
            break
        b+=1
        tmpx +=1

    tmpx = x
    tmpy -=1
    
    while tmpy >= 0:

        if s[y][x] <= s[tmpy][tmpx]:
            c+=1
            test+=1
            break
        c+=1
        tmpy -=1
    tmpy = y+1

    while tmpy < len(s):
        if s[y][x] <= s[tmpy][tmpx]:
            d+=1
            test+=1
            break
        d+=1
        tmpy +=1
   
    return a*b*c*d
    
for y in range(len(s)):
    for x in range(len(s[0])):        
        t = tcheck2(y, x)
        if t > ANS:
            ANS = t

if(ANS and not DEBUG):    
    submit(DAY, PART, ANS)
else:
    print(f"[DEBUG] Part 2 : {ANS}")
