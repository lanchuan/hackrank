#!/bin/python3

import sys


n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]
    h=3
    for k in range(i,j+1):
        if width[k]<h:
            h=width[k]
    print(h)
