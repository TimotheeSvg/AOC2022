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
s = get_input(DAY).strip().split('\n')

# PART 1
class Folders:
    def __init__(self, name,parent = None, files = None, folder = None) -> None:
        self.name = name
        self.parent = parent
        self.tabFolder = []
        self.tabFiles = []
        self.size = 0
        
    def addFolder(self, folder):
        self.tabFolder.append(folder)
    
    def addFile(self, file):
        self.tabFiles.append(file)
                
    def calculSomme(self):
        for i in range(len(self.tabFolder)):
            somme = self.tabFolder[i].calculSomme()
            if somme:
                self.size += somme 
        
        for i in range(len(self.tabFiles)):
            self.size += int(self.tabFiles[i].size)
        tabaille.append(int(self.size))
        return self.size

    def tester(self):
        for i in range(len(self.tabFolder)):
            self.tabFolder[i].afficher()
        
        print(f"La taille de {self.name} est égal à {self.size}") 

            
class Files:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size  

PART = 1
ANS = 0
tabaille = []

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


strat.calculSomme()
ANS = sum([x for x in tabaille if x < 100000])

if(ANS and not DEBUG):    
    submit(DAY, PART, ANS)
else:
    print(f"[DEBUG] Part 1 : {ANS}")


#part 2
PART = 2
ans = 0
totalSpace = 70_000_000 -  30_000_000

minFile = 99999999999
tabaille = sorted(set(tabaille))
print(tabaille)
for i in range(len(tabaille)):
    if totalSpace - (strat.size - tabaille[i]) > 0:
        print(tabaille[i])

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 2 : {ans}")
