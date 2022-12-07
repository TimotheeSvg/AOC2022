from AOC import * 
import collections
import math
import itertools
import time
import random
import pandas as pd
import numpy as np


DAY = 6
DEBUG = True
s = get_input(DAY).strip()

# PART 1 
PART = 1
ans = 0

for i in range(len(s)):
     if len(set([s[i+y] for y in range(4)])) == 4:
        ans = i +4
        break

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 1 : {ans}")


#part 2
PART = 2
ans = 0

for i in range(len(s)):
    if i < len(s) - 14:
     if len(set([s[i+y] for y in range(14)])) == 14:
        ans = i +14
        break

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 2 : {ans}")

