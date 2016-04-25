import math
B=[]
number=0
m,n=[int(x) for x in raw_input().strip().split()]
def isPrime(a):
    for i in B:
        if a%i==0:
            return False
        if i>math.sqrt(a):
            break
    return True
b=2
j=1
while number<10001:
    if isPrime(b):
        B.append(b)
        number+=1
        if number>=m and number<=n:
            if j%10!=0:
                print b,
                j+=1
            else:
                print b
                j+=1
    b+=1
    if number>n:
        break