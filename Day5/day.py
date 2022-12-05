from AOC import * 
import collections
import math
import itertools
import time
import random
import pandas as pd
import numpy as np
import re

linePyramid = """    [G] [R]                 [P]    
    [H] [W]     [T] [P]     [H]    
    [F] [T] [P] [B] [D]     [N]    
[L] [T] [M] [Q] [L] [C]     [Z]    
[C] [C] [N] [V] [S] [H]     [V] [G]
[G] [L] [F] [D] [M] [V] [T] [J] [H]
[M] [D] [J] [F] [F] [N] [C] [S] [F]
[Q] [R] [V] [J] [N] [R] [H] [G] [Z]
 1   2   3   4   5   6   7   8   9"""

lineMouv = """move 5 from 8 to 2
move 2 from 4 to 5
move 3 from 3 to 9
move 4 from 1 to 8
move 5 from 9 to 1
move 3 from 3 to 8
move 2 from 4 to 7
move 6 from 6 to 5
move 5 from 2 to 4
move 2 from 9 to 1
move 1 from 7 to 1
move 4 from 7 to 3
move 5 from 1 to 5
move 3 from 1 to 4
move 8 from 5 to 3
move 7 from 3 to 2
move 10 from 4 to 7
move 1 from 7 to 3
move 1 from 6 to 2
move 3 from 8 to 4
move 4 from 3 to 2
move 1 from 1 to 2
move 4 from 3 to 1
move 2 from 1 to 7
move 3 from 5 to 1
move 7 from 8 to 4
move 9 from 5 to 1
move 9 from 2 to 7
move 6 from 4 to 9
move 14 from 7 to 5
move 2 from 1 to 4
move 6 from 7 to 1
move 4 from 4 to 9
move 6 from 2 to 8
move 2 from 4 to 9
move 2 from 9 to 3
move 3 from 8 to 3
move 5 from 9 to 4
move 1 from 2 to 9
move 5 from 5 to 3
move 3 from 2 to 7
move 1 from 1 to 4
move 3 from 7 to 5
move 4 from 9 to 6
move 2 from 9 to 3
move 5 from 1 to 6
move 7 from 6 to 5
move 1 from 2 to 3
move 10 from 1 to 5
move 1 from 8 to 3
move 14 from 3 to 7
move 1 from 8 to 4
move 2 from 6 to 1
move 28 from 5 to 9
move 1 from 2 to 1
move 5 from 4 to 6
move 2 from 4 to 3
move 13 from 7 to 8
move 1 from 3 to 5
move 1 from 5 to 2
move 1 from 3 to 6
move 1 from 5 to 6
move 22 from 9 to 1
move 1 from 2 to 7
move 3 from 9 to 5
move 2 from 7 to 5
move 18 from 1 to 4
move 7 from 8 to 3
move 4 from 6 to 8
move 2 from 5 to 8
move 5 from 3 to 9
move 2 from 5 to 1
move 3 from 6 to 8
move 1 from 5 to 9
move 2 from 3 to 6
move 10 from 1 to 5
move 15 from 8 to 6
move 10 from 6 to 8
move 1 from 9 to 4
move 1 from 1 to 3
move 4 from 4 to 3
move 5 from 3 to 5
move 9 from 5 to 6
move 13 from 6 to 5
move 8 from 5 to 7
move 8 from 9 to 6
move 2 from 6 to 4
move 2 from 6 to 2
move 3 from 7 to 4
move 2 from 2 to 8
move 1 from 5 to 4
move 3 from 7 to 9
move 1 from 5 to 9
move 5 from 6 to 9
move 10 from 8 to 3
move 3 from 8 to 1
move 5 from 9 to 2
move 1 from 6 to 4
move 4 from 5 to 6
move 7 from 3 to 7
move 5 from 6 to 5
move 19 from 4 to 8
move 15 from 8 to 3
move 2 from 1 to 5
move 7 from 5 to 9
move 2 from 7 to 2
move 3 from 3 to 8
move 5 from 5 to 8
move 10 from 9 to 3
move 1 from 4 to 2
move 10 from 8 to 3
move 29 from 3 to 2
move 2 from 3 to 4
move 1 from 1 to 5
move 2 from 8 to 4
move 1 from 9 to 1
move 1 from 3 to 9
move 1 from 1 to 9
move 2 from 3 to 4
move 33 from 2 to 1
move 2 from 2 to 4
move 1 from 3 to 1
move 22 from 1 to 2
move 6 from 4 to 9
move 4 from 7 to 1
move 16 from 1 to 4
move 3 from 7 to 6
move 2 from 9 to 4
move 1 from 5 to 2
move 9 from 4 to 2
move 1 from 6 to 5
move 7 from 4 to 2
move 6 from 9 to 8
move 4 from 4 to 9
move 4 from 8 to 3
move 2 from 4 to 3
move 2 from 2 to 5
move 2 from 5 to 2
move 1 from 5 to 6
move 3 from 9 to 5
move 1 from 6 to 8
move 2 from 6 to 5
move 1 from 3 to 2
move 1 from 8 to 4
move 2 from 8 to 2
move 5 from 5 to 6
move 44 from 2 to 8
move 1 from 4 to 8
move 3 from 6 to 8
move 2 from 6 to 2
move 37 from 8 to 3
move 1 from 9 to 4
move 1 from 2 to 5
move 5 from 8 to 6
move 1 from 4 to 6
move 1 from 2 to 4
move 16 from 3 to 2
move 1 from 4 to 5
move 1 from 8 to 3
move 4 from 8 to 2
move 1 from 8 to 7
move 2 from 5 to 8
move 15 from 2 to 4
move 5 from 6 to 3
move 1 from 7 to 4
move 1 from 8 to 9
move 1 from 6 to 7
move 1 from 8 to 3
move 2 from 2 to 8
move 1 from 9 to 3
move 2 from 8 to 4
move 1 from 4 to 6
move 33 from 3 to 7
move 1 from 6 to 3
move 1 from 4 to 8
move 1 from 8 to 9
move 4 from 4 to 3
move 9 from 4 to 7
move 3 from 4 to 8
move 11 from 7 to 2
move 14 from 7 to 6
move 1 from 8 to 3
move 1 from 9 to 5
move 1 from 5 to 1
move 8 from 2 to 9
move 1 from 8 to 7
move 6 from 3 to 6
move 18 from 6 to 4
move 1 from 2 to 7
move 1 from 3 to 6
move 14 from 4 to 2
move 4 from 4 to 3
move 3 from 6 to 3
move 19 from 2 to 6
move 16 from 6 to 8
move 1 from 1 to 8
move 16 from 8 to 7
move 3 from 9 to 4
move 3 from 6 to 2
move 3 from 4 to 7
move 4 from 3 to 2
move 2 from 2 to 4
move 4 from 9 to 8
move 5 from 2 to 8
move 29 from 7 to 5
move 6 from 8 to 2
move 2 from 3 to 4
move 2 from 2 to 6
move 1 from 3 to 5
move 4 from 2 to 6
move 8 from 7 to 5
move 1 from 7 to 5
move 2 from 8 to 6
move 1 from 8 to 7
move 6 from 6 to 1
move 2 from 7 to 6
move 1 from 9 to 7
move 3 from 1 to 7
move 3 from 6 to 1
move 1 from 7 to 6
move 3 from 1 to 6
move 1 from 1 to 5
move 4 from 6 to 3
move 2 from 4 to 2
move 38 from 5 to 6
move 3 from 3 to 8
move 4 from 8 to 6
move 22 from 6 to 8
move 1 from 7 to 8
move 2 from 6 to 2
move 2 from 5 to 2
move 2 from 2 to 1
move 2 from 4 to 6
move 2 from 2 to 1
move 1 from 1 to 9
move 2 from 8 to 5
move 2 from 2 to 8
move 2 from 5 to 2
move 2 from 7 to 2
move 1 from 3 to 1
move 4 from 1 to 8
move 1 from 9 to 5
move 1 from 1 to 7
move 1 from 2 to 8
move 29 from 8 to 3
move 15 from 3 to 2
move 12 from 2 to 5
move 1 from 1 to 6
move 3 from 2 to 1
move 6 from 3 to 8
move 2 from 3 to 9
move 1 from 6 to 7
move 12 from 5 to 8
move 2 from 7 to 1
move 2 from 1 to 4
move 2 from 4 to 2
move 1 from 5 to 8
move 1 from 3 to 6
move 2 from 3 to 4
move 3 from 1 to 4
move 5 from 8 to 9
move 4 from 4 to 2
move 5 from 9 to 6
move 26 from 6 to 8
move 7 from 2 to 8
move 3 from 3 to 1
move 1 from 6 to 4
move 14 from 8 to 6
move 2 from 1 to 2
move 1 from 1 to 3
move 18 from 8 to 5
move 15 from 8 to 2
move 5 from 6 to 8
move 4 from 5 to 8
move 7 from 2 to 5
move 2 from 9 to 6
move 1 from 2 to 1
move 7 from 2 to 3
move 7 from 8 to 1
move 2 from 6 to 3
move 1 from 4 to 6
move 2 from 8 to 6
move 10 from 3 to 9
move 18 from 5 to 8
move 1 from 4 to 6
move 2 from 1 to 9
move 12 from 6 to 9
move 1 from 6 to 9
move 9 from 8 to 4
move 6 from 1 to 2
move 3 from 8 to 9
move 14 from 9 to 8
move 5 from 4 to 9
move 2 from 4 to 5
move 16 from 8 to 5
move 12 from 5 to 4
move 7 from 5 to 1
move 1 from 1 to 8
move 1 from 5 to 8
move 1 from 4 to 9
move 8 from 2 to 7
move 12 from 4 to 3
move 2 from 2 to 5
move 1 from 3 to 2
move 3 from 5 to 4
move 1 from 4 to 8
move 3 from 4 to 9
move 18 from 9 to 8
move 8 from 3 to 1
move 5 from 8 to 1
move 1 from 2 to 5
move 3 from 7 to 1
move 3 from 7 to 5
move 1 from 8 to 9
move 5 from 9 to 7
move 2 from 3 to 6
move 16 from 1 to 4
move 14 from 8 to 6
move 2 from 5 to 6
move 4 from 1 to 6
move 3 from 4 to 9
move 15 from 6 to 1
move 5 from 4 to 3
move 2 from 8 to 2
move 6 from 4 to 3
move 15 from 1 to 5
move 14 from 5 to 3
move 5 from 6 to 2
move 2 from 4 to 7
move 1 from 1 to 6
move 2 from 3 to 4
move 3 from 8 to 1
move 1 from 5 to 1
move 5 from 7 to 1
move 7 from 1 to 3
move 3 from 6 to 2
move 4 from 9 to 5
move 2 from 4 to 3
move 4 from 7 to 9
move 8 from 2 to 9
move 1 from 9 to 1
move 2 from 2 to 8
move 11 from 9 to 1
move 6 from 5 to 1
move 21 from 3 to 2
move 1 from 8 to 5
move 5 from 1 to 7
move 12 from 1 to 8
move 1 from 5 to 2
move 5 from 3 to 2
move 4 from 7 to 2
move 1 from 7 to 8
move 13 from 2 to 5
move 13 from 2 to 5
move 2 from 2 to 1
move 1 from 1 to 9
move 26 from 5 to 4
move 3 from 2 to 7
move 2 from 3 to 9
move 1 from 1 to 6
move 5 from 3 to 2
move 2 from 9 to 6
move 1 from 1 to 8
move 3 from 1 to 6
move 24 from 4 to 9
move 13 from 9 to 1
move 2 from 6 to 2
move 3 from 7 to 5
move 2 from 9 to 7
move 8 from 8 to 3
move 4 from 8 to 5
move 2 from 7 to 2
move 8 from 9 to 4
move 10 from 1 to 2
move 1 from 9 to 1
move 1 from 9 to 2
move 4 from 3 to 2
move 4 from 1 to 8
move 3 from 4 to 8
move 12 from 2 to 3
move 3 from 4 to 6
move 5 from 3 to 2
move 9 from 3 to 9
move 4 from 2 to 9
move 1 from 3 to 7
move 6 from 8 to 2
move 4 from 6 to 8
move 1 from 3 to 8
move 6 from 9 to 1
move 2 from 1 to 8
move 5 from 5 to 8
move 3 from 6 to 8
move 1 from 5 to 1
move 7 from 8 to 2
move 1 from 1 to 4
move 1 from 4 to 6
move 1 from 9 to 4
move 1 from 5 to 9
move 1 from 4 to 7
move 12 from 8 to 2
move 4 from 4 to 3
move 2 from 3 to 1
move 1 from 7 to 2
move 1 from 6 to 8
move 1 from 8 to 6
move 4 from 9 to 3
move 1 from 9 to 3
move 13 from 2 to 3
move 3 from 1 to 7
move 2 from 9 to 4
move 2 from 1 to 9
move 2 from 7 to 2
move 1 from 4 to 1
move 2 from 7 to 5
move 14 from 3 to 8
move 1 from 8 to 5
move 2 from 1 to 4
move 2 from 3 to 4
move 2 from 3 to 4
move 10 from 8 to 3
move 2 from 4 to 8
move 1 from 9 to 3
move 3 from 2 to 3
move 16 from 2 to 4
move 1 from 8 to 5
move 11 from 3 to 4
move 2 from 3 to 7
move 3 from 5 to 1
move 1 from 1 to 2
move 3 from 2 to 5
move 1 from 1 to 9
move 2 from 7 to 4
move 8 from 4 to 3
move 1 from 6 to 7
move 1 from 8 to 6
move 1 from 5 to 1
move 6 from 3 to 5
move 2 from 1 to 3
move 5 from 5 to 7
move 2 from 7 to 2
move 2 from 3 to 4
move 4 from 7 to 1
move 1 from 6 to 8
move 1 from 2 to 1
move 3 from 1 to 6
move 2 from 9 to 6
move 8 from 2 to 1
move 2 from 6 to 2
move 2 from 6 to 3
move 6 from 3 to 5
move 2 from 4 to 6
move 2 from 2 to 9
move 1 from 8 to 6
move 2 from 6 to 5
move 1 from 9 to 1
move 11 from 5 to 8
move 7 from 8 to 6
move 23 from 4 to 1
move 1 from 5 to 9
move 1 from 4 to 6
move 2 from 4 to 8
move 1 from 3 to 1
move 6 from 8 to 3
move 2 from 9 to 6
move 3 from 6 to 1
move 3 from 8 to 7
move 1 from 3 to 6
move 18 from 1 to 2
move 5 from 3 to 8
move 13 from 2 to 9
move 5 from 9 to 7
move 1 from 8 to 6
move 5 from 2 to 6
move 2 from 1 to 7
move 9 from 7 to 8
move 11 from 8 to 6
move 2 from 9 to 4
move 16 from 6 to 1
move 2 from 4 to 6
move 1 from 8 to 9
move 1 from 7 to 6
move 8 from 1 to 5
move 3 from 6 to 5
move 8 from 6 to 4
move 7 from 9 to 5
move 1 from 8 to 1
move 6 from 5 to 1
move 9 from 5 to 7
move 4 from 7 to 9
move 1 from 4 to 8
move 1 from 8 to 3
move 1 from 1 to 8
move 1 from 8 to 7
move 22 from 1 to 3
move 1 from 6 to 7
move 2 from 9 to 4
move 1 from 9 to 6
move 1 from 9 to 4
move 10 from 4 to 3
move 1 from 1 to 2
move 2 from 5 to 4
move 27 from 3 to 8
move 5 from 3 to 9"""

 
 
linePyramid = linePyramid.split('\n')
max_ = int(max(linePyramid.pop()))

tab=[[] for _ in range(max_)]
tab2=[[] for _ in range(max_)]

for i in range(len(linePyramid)):
    id = 0
    for y in range(len(linePyramid[i])):
        if 64 < ord(linePyramid[i][y]) < 91: 
            tab[id].append(linePyramid[i][y])
            tab2[id].append(linePyramid[i][y])
            
            
        if 1< y < 6:   
            if y % 5 == 0:
                id+=1
        else:
            if y %4 == 1:
                id +=1      
                          
for i in range(len(tab)):
    tab[i] = tab[i][::-1]
    tab2[i] = tab2[i][::-1]
    
lineMouv = lineMouv.split('\n')
tabMouv = []
for i in lineMouv:
    tabMouv.append(list(map(int, re.findall(r'\d+', i))))
    
    
DAY = 5
DEBUG = True


# PART 1 
PART = 1
ans = ''

for i in tabMouv:
    for y in range(i[0]):
        tab[i[2] - 1].append(tab[i[1] - 1].pop())
    

for i in tab:
    ans+= i[len(i) - 1]

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 1 : {ans}")


#part 2
PART = 2
ans = ''

for i in tabMouv:
    pickTower = tab2[i[1] - 1]
    pickElement = pickTower[len(pickTower)-i[0]:len(pickTower)]
    for y in range(i[0]):
        tab2[i[1] - 1].pop()
        
    targetTower = tab[i[2]-1]
    tab2[i[2]-1].extend(pickElement)
    
for i in tab2:
    ans+= i[len(i) - 1]
    
if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 2 : {ans}")
