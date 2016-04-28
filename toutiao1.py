a=int(input())
s=[] 
di={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0} 
head=[]
big=0
x=9
def sum1(s): 
    cursum=0 
    num=0 
    for i in s:
    	num=0
        for j in i: 
            num=num*10+di[j] 
        cursum+=num 
    return cursum 
def count(s): 
    for i in s: 
        k=10**(len(i)-1)
        for j in i: 
            di[j]+=k 
            k/=10 
for i in range(a): 
    s.append(raw_input().strip())
    head.append(s[0])
count(s)
dic=sorted(di.iteritems(),key=lambda d:d[1])
for m in dic:
    if m[0] not in head:
        a=m
        dic.remove(m)
        break
dic.reverse()
dic.append(a)
for i  in dic:
	di[i[0]]=x
	x-=1

print sum1(s)
