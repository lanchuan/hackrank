a=int(input())
for i in range(a):
    b=input().strip()
    k=len(b)
    c=0
    for j in range(int(k/2)):
        c+=abs(ord(b[j])-ord(b[k-j-1]))
    print(c)