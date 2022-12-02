from AOC import * 
import collections
import math

DAY = 2
DEBUG = True
s = get_input(DAY).strip().split('\n')

PART = 1
ans = 0

rule = {
    'A X' : 4,
    'B Y' : 5,
    'C Z' : 6,
    'A Y' : 8,
    'A Z' : 3,
    'B X' : 1,
    'B Z' : 9,
    'C X' : 7,
    'C Y' : 2,
    }

for e in range(len(s)):
    ans += rule[s[e]]

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 1 : {ans}")

PART = 2
ans = 0

score = {'A' : 1,'B' : 2,'C' : 3}
gagnant = {'A' : 'B','B' : 'C','C' : 'A',}
perdant = {'A' : 'C','B' : 'A','C' : 'B',}

for e in s:
    if(e[2] == 'X'):
        ans += score[e[2].replace('X', perdant[e[0]])] 
    elif(e[2] == 'Y'):
        ans += score[e[0]] + 3
    else:
        ans+= score[e[2].replace('Z', gagnant[e[0]])] + 6

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 2 : {ans}")
