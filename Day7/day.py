from AOC import * 
import collections
import math
import itertools
import time
import random
import pandas as pd
import numpy as np


DAY = 7
DEBUG = True
# s = get_input(DAY).strip().split('\n')
s = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.split("\n")

# PART 1
 
PART = 1
ANS = 0
    
class Folders:
    def __init__(self, name,parent = None, files = None, folder = None) -> None:
        self.name = name
        self.parent = parent
        self.tabFolder = []
        self.tabFiles = []
        
    def addFolder(self, folder):
        self.tabFolder.append(folder)
    
    def addFile(self, file):
        self.tabFiles.append(file)
        
    def calculSomme(self):
        res = 0
        for i in range(len(self.tabFolder)):
            r = self.tabFolder[i].calculSomme()
            if r:
                res +=r
        
        for i in range(len(self.tabFiles)):
            res += int(self.tabFiles[i].size)
        if res < 100000:
            return res
        else: 
            return 0
            
class Files:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size  

strat = Folders('/')

CurrentFile = strat


for element in s:
    k = element.split(' ')
    
    if "cd" in k:
        if ".." in k:
            if CurrentFile.parent != None:
                CurrentFile = CurrentFile.parent
            else:
                CurrentFile = strat
        else:
            for i in range(len(CurrentFile.tabFolder)):
                if CurrentFile.tabFolder[i].name == k[2]:
                    CurrentFile = CurrentFile.tabFolder[i]                    
                    break
            
    elif "ls" in k:
        pass
    elif "dir" in k:
        tmp = Folders(k[1], CurrentFile)
        CurrentFile.addFolder(tmp)
    else:
        tmp2 = Files(k[1], k[0])
        CurrentFile.addFile(tmp2)


ANS = strat.calculSomme()

if(ANS and not DEBUG):    
    submit(DAY, PART, ANS)
else:
    print(f"[DEBUG] Part 1 : {ANS}")


#part 2
PART = 2
ans = 0

#
# WRITE HERE
#

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 2 : {ans}")
