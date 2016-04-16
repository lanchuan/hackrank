#!/usr/bin/python3
def maxXor(l, r):
    a=bin(l)
    b=bin(r)
    x=1
    if len(a)!=len(b):
        for i in range(len(b)-3):
            x=x*2+1
        return x
    else:
        for j in range(len(b)):
            if a[j]!=b[j]:
                break
        for k in range(len(b)-j-1):
            x=x*2+1
        return x
              
if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))
