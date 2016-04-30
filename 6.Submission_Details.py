class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        a=[[] for i in range(numRows)]
        j=0
        flag=False
        for i in list(s):
            a[j]+=i
            if flag==False:
                j+=1
                if j==numRows:
                    j=numRows-1
                    flag=not flag
            if flag==True:
                j-=1
                if j==-1:
                    j=1
                    flag=not flag

        result=""
        for i in a:
            result+="".join(i)
        return result