from AOC import * 
import collections
import math

DAY = 1
DEBUG = True
s = get_input(DAY).strip()


# PART 1 
PART = 1
ans = None

ans = max(map(sum, [[int(nbr)for nbr in tabNbrStr.strip('\n').split('\n')] for tabNbrStr in s.split('\n\n')]))

if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 1 : {ans}")

print("je suis le bot")
#part 2
PART = 2
ans = 0

tabnbr = list(map(sum,[[int(nbr)for nbr in tabNbrStr.strip('\n').split('\n')] for tabNbrStr in s.split('\n\n')]))

for _ in range(3):
    ans +=max(tabnbr)
    tabnbr.remove(max(tabnbr))


if(ans and not DEBUG):    
    submit(DAY, PART, ans)
else:
    print(f"[DEBUG] Part 2 : {ans}")
