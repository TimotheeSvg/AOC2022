from AOC import * 
import collections
import math
import itertools
import time
import random
import pandas as pd
import numpy as np


DAY = 4
DEBUG = False
s = [[[int(g) for g in f.split('-')] for f in e.split(',')] for e in get_input(DAY).strip().split('\n')]

# PART 1 
PART = 1
ans = 0

for e in s:
    if e[0][0] <= e[1][0] and e[0][1] >= e[1][1]:
        ans+=1
    elif e[1][0] <= e[0][0] and e[1][1] >= e[0][1]:
        ans+=1

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 1 : {ans}")


#part 2
PART = 2
ans = 0

for e in s:
    if e[0][0] <= e[1][0] and e[0][1] >= e[1][0]:
        ans+=1
    elif e[1][0] <= e[0][0] and e[1][1] >= e[0][0]:    
        ans+=1

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 2 : {ans}")
