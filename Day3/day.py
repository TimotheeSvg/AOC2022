from AOC import * 
import collections
import math
import itertools
import time
import random
import pandas as pd
import numpy as np


DAY = 3
DEBUG = True
s = get_input(DAY).strip().split('\n')

# PART 1 
PART = 1
ans = 0

for e in s:
    taille = len(e)//2    
    for i in e[:taille]:
        if i in e[taille:]:
            if ord(i) > 92:
                ans += ord(i) - 96
            else:
                ans  += ord(i) - 38
            break

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 1 : {ans}")


#part 2
PART = 2
ans = 0

s = [[s[i], s[i+1], s[i+2]] for i in range(0,len(s),3)]

for e in s:
    for i in set(e[0]):
        if i in set(e[1]) and i in set(e[2]):
            if ord(i) > 92:
                ans += ord(i) - 96
            else:
                ans  += ord(i) - 38
    
if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 2 : {ans}")
