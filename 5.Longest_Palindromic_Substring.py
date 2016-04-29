class Solution(object):
    def longestPalindrome(self, s):
        b=['^']
        preprocess(s,b)
        p=[0]*len(b)
        C=R=0
        for i in range(len(b)-1):
            i_mirror=(C-(i-C))
            diff=R-i
            if diff>0:
                if p[i_mirror]<diff:
                    p[i]=p[i_mirror]
                else:
                    p[i]=diff
                    while b[i+p[i]+1]==b[i-p[i]-1]:
                        p[i]+=1
                    C=i
                    R=i+p[i]
            else:
                p[i]=0
                while b[i+p[i]+1]==b[i-p[i]-1]:
                    p[i]+=1
                C=i
                R=i+p[i]

        maxlen=0
        center=0
        for j in range(len(p)):
            if maxlen<p[j]:
                maxlen=p[j]
                center=j
        return s[(center-maxlen-1)/2:(center-maxlen-1)/2+maxlen]
       
def preprocess(s,b):
    a=list(s)
    for i in a:
        b+='#'+i
    b+='#$'