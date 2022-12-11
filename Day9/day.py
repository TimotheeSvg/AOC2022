from AOC import * 
import collections
import math
import itertools
import time
import random
import pandas as pd
import numpy as np


DAY = 9
DEBUG = False

if DEBUG:
        s = [
            ['R', 5],
            ['U', 8],
            ['L', 8],
            ['D', 3],
            ['R', 17],
            ['D', 10],
            ['L', 25],
            ['U', 20]
            ]

else:
        s = [[a for a in x.split(' ') ] for x in get_input(DAY).strip().split('\n')]
        for e in range(len(s)):
            s[e][1] = int(s[e][1])


    
        
# PART 1 
PART = 1
ANS = 1

t,h = [0,0], [0,0]
q = {'0 0' : 1}
#y x

for i in range(len(s)):
    for n in range(s[i][1]):
        if s[i][0] == 'R':
            t[1] +=1
            if h[1] < t[1] -1:
                h[1] = t[1] -1
                h[0] = t[0]
                if f'{h[0]} {h[1]}' not in q:
                    q[f'{h[0]} {h[1]}'] = 1
                    ANS+=1

        if s[i][0] == 'L':
            t[1] -=1
            if h[1] > t[1] +1:
                h[1] = t[1] +1
                h[0] = t[0]
                if f'{h[0]} {h[1]}' not in q:
                    q[f'{h[0]} {h[1]}'] = 1
                    ANS+=1


        if s[i][0] == 'U':
            t[0] -=1
            if h[0] > t[0] +1:
                h[0] = t[0] +1
                h[1] = t[1]
                if f'{h[0]} {h[1]}' not in q:
                    q[f'{h[0]} {h[1]}'] = 1
                    ANS+=1


        if s[i][0] == 'D':
            t[0] +=1
            if h[0] < t[0] -1:
                h[0] = t[0] -1
                h[1] = t[1]
                if f'{h[0]} {h[1]}' not in q:
                    q[f'{h[0]} {h[1]}'] = 1
                    ANS+=1

if(ANS and not DEBUG):    
    submit(DAY, PART, ANS)
else:
    print(f"[DEBUG] Part 1 : {ANS}")


#part 2
PART = 2
ANS = 0

class Knot():
    def __init__(self,id) -> None:
        self.precedent = None
        self.id = id
        self.y = 0
        self.x = 0


class Rope:
    def __init__(self) -> None:
        self.q = {'0 0' : 1}
        self.knots = []
        self.head = Knot(0)
        self.ans = 0
        self.knots.append(self.head)
        last = self.head
        for i in range(1,10):
            tmp = Knot(i)
            tmp.precedent = last
            last = tmp
            self.knots.append(tmp)


    def moveHead(self, dir, nbr):
        for i in range(nbr):
            if dir == 'R':
                self.knots[0].x +=1

            if dir == 'L':
                self.knots[0].x -=1

            if dir == 'U':
                self.knots[0].y -=1

            if dir == 'D':
                self.knots[0].y +=1
     
            self.tchekRope()


    def tchekRope(self):
        for i in range(1, len(self.knots)):
            if self.knots[i].x < self.knots[i-1].x -1:
                if i == 9:
                    if f'{self.knots[i].y} {self.knots[i].x}' not in self.q:
                        self.q[f'{self.knots[i].y} {self.knots[i].x}'] = 1

                        self.ans +=1

                self.knots[i].x = self.knots[i-1].x -1

                if self.knots[i].y > self.knots[i-1].y:
                    self.knots[i].y -= 1
                elif self.knots[i].y < self.knots[i-1].y:
                    self.knots[i].y += 1
                    
            if self.knots[i].x > self.knots[i-1].x +1:
                if i == 9:
                    if f'{self.knots[i].y} {self.knots[i].x}' not in self.q:
                        self.q[f'{self.knots[i].y} {self.knots[i].x}'] = 1
                        self.ans +=1

                self.knots[i].x = self.knots[i-1].x +1

                if self.knots[i].y > self.knots[i-1].y:
                    self.knots[i].y -= 1
                elif self.knots[i].y < self.knots[i-1].y:
                    self.knots[i].y += 1

            if self.knots[i].y > self.knots[i-1].y +1:
                if i == 9:
                    if f'{self.knots[i].y} {self.knots[i].x}' not in self.q:
                        self.q[f'{self.knots[i].y} {self.knots[i].x}'] = 1
                        self.ans +=1

                self.knots[i].y = self.knots[i-1].y +1

                if self.knots[i].x > self.knots[i-1].x:
                    self.knots[i].x -= 1
                elif self.knots[i].x < self.knots[i-1].x:
                    self.knots[i].x += 1

            if self.knots[i].y < self.knots[i-1].y -1:
                if i == 9:
                    if f'{self.knots[i].y} {self.knots[i].x}' not in self.q:
                        self.q[f'{self.knots[i].y} {self.knots[i].x}'] = 1
                        self.ans +=1

                self.knots[i].y = self.knots[i-1].y -1

                if self.knots[i].x > self.knots[i-1].x:
                    self.knots[i].x -= 1
                elif self.knots[i].x < self.knots[i-1].x:
                    self.knots[i].x += 1

r = Rope()
for e in s:
    r.moveHead(e[0], e[1])

ANS = r.ans+2 #???
print(len(r.q))
if(ANS and not DEBUG):    
    submit(DAY, PART, ANS)
else:
    print(f"[DEBUG] Part 2 : {ANS}")
