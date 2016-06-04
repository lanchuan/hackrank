def solution(A):
    # write your code in Python 2.7
    if A==[]:
        return -1
    B=[A[0]]
    for i in range(1,len(A)):
        B.append(B[i-1]+A[i])
    for j in range(len(A)-2,-1,-1):
        print j
        A[j]=A[j+1]+A[j]
    print A
    print B
    for i in range(len(A)-2):
        if B[i]==A[i+2]:
            return i+1
    if A[0]==0:
        return 0
    elif B[-1]==0:
        return len(B)-1
    else:
        return -1

A=[-1, 3, -4, 5, 1, -6, 2, 1] 
print solution(A)