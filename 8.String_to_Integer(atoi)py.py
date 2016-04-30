class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str=="":
            return 0
        try:
            x=int(str)
            for i in str:
                if i == ' ':
                    continue
                elif i=='+' or i=='-':
                    if str[i+1]==' ':
                        return 0
                else:
                    break
        except:
            flag=1
            i=0
            if i<len(str):
                while str[i]==' ':
                    i+=1
                if str[i]=='+':
                    i+=1
                elif str[i]=='-':
                    flag=-1
                    i+=1
                begin=i
                
            if i<len(str):
                while str[i]=='0':
                    i+=1
                begin=i
            if i<len(str):
                while str[i]>='0' and str[i]<='9':
                    i+=1
                    if i>=len(str):
                        break
                
            end=i
            if begin==end:
                return 0
            x=flag*int(str[begin:end])
        if x>2147483647:
            return 2147483647
        elif x<-2147483648:
            return -2147483648
        return x