# Sherlock’s Speedy Chase

from math import ceil

k = int(input()) # speed (m/s)
n = int(input()) # number of buildings 
a = list(map(int, input().split())) # height of each building
i = 0 # variable (number of building)
h = 0 # his location's height
target = 0 # target height
total = 0 # total time

while i < n: # main loop

    target = a[i] # target height
 
    if target > h: # if target is higher than his location
        temp = (target - h) / k # time
        total += ceil(temp) # add to total
        h = target # update

    else: # if target is lower than or equal to his location 
        temp = (h - target) / k # time
        total += ceil(temp) # add to total
        h = target # update

    i += 1 # update

total += n + ceil(h/k) # add to total
print(total)
