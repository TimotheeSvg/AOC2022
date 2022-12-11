from AOC import * 
import collections
import math
import itertools
import time
import random
import pandas as pd
import numpy as np

DAY = 10
DEBUG = False

if DEBUG:
    s = [[y for y in x.split(' ')]for x in get_example(DAY).strip().split('\n')]
else:
    s = [[y for y in x.split(' ')]for x in get_input(DAY).strip().split('\n')]

# PART 1 
PART = 1
ANS = []

def tchekDuring():
    if step == 20:
        ANS.append(x*step)
    elif step == 60:
        ANS.append(x*step)
    elif step == 100:
        ANS.append(x*step)
    elif step == 140:
        ANS.append(x*step)
    elif step == 180:
        ANS.append(x*step)
    elif step == 220:
        ANS.append(x*step)

step = 0
x = 1
for e in s:
    if len(e) == 1:
        step +=1
        tchekDuring()
    else:
        step+=1
        tchekDuring()
        step+=1
        tchekDuring()
        x += int(e[1])
ANS = sum(ANS)

if(ANS and not DEBUG):    
    submit(DAY, PART, ANS)
else:
    print(f"[DEBUG] Part 1 : {ANS}")

#part 2
PART = 2

ANS2 = []
sprite = [0,1,2]
step = 0
crt = ''

def crtManage(crt):
    if step%40 == 0 and len(crt) > 1:
        ANS2.append(crt)
        crt = ''

    if step %40 in sprite:
        crt +='#'
    else:
        crt +='.'

    return crt

for e in s:
    if len(e) == 1:
        crt = crtManage(crt)
        step +=1
    else:
        crt = crtManage(crt)
        step+=1
        crt = crtManage(crt)
        step+=1
        sprite = list(map(lambda x: x+int(e[1]), sprite))
    
ANS2.append(crt)

for i in range(len(ANS2)):
    print(ANS2[i])
