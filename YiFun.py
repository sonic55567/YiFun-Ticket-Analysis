from typing import Coroutine
import matplotlib.pyplot as plt
from itertools import combinations, permutations
import random

from matplotlib.pyplot import plot

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# compute combinations of two balls
comb = list(combinations(num, 2))

# compute the times that every possible steps will appear
flag = [0]*10
for i in comb :
    flag[(i[0]+i[1])%10] = flag[(i[0]+i[1])%10]+1

# creat the table
table = list()
index = 0
for i in flag :
    for j in range(i) :
        table.append(index)
    index = index+1
circle = [-1, 5, 9, 7, 1, 4, -1, 6, 0, 3, 8, 2]

win = [0]*10
# start to walk
for times in range(1000000) :
    circle = [-1, 5, 9, 7, 1, 4, -1, 6, 0, 3, 8, 2]
    now = 0
    while True :
        step = random.randint(0, 44)
        step = table[step]
        for i in range(step):
            now = now+1
            if now>=len(circle) :
                now = 0
        if circle[now] != -1 :
            win[circle[now]] = win[circle[now]]+1
            circle.remove(circle[now])
            now = now-1
        if(len(circle) == 5) :
            break
    

for i in range(10) :
    win[i] = win[i]/1000000
plt.xticks(range(10))
plt.bar(range(10), win)
plt.show()
print(win)



