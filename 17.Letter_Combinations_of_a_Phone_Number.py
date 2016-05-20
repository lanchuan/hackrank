class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #letter=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        #out=[]
        digit=list(int(x) for x in digits)
        result=''
        out=[]
        if len(digits)==0:
            return out
        general(digit,0,result,out)
        return out
        

letter=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def general(digit,number,result,out):
    if number==len(digit):
        out.append(result)
    else:
        for i in letter[digit[number]]:
            general(digit,number+1,result+i,out)




s=Solution()
a="4522"
b="23"
print s.letterCombinations(a)
print s.letterCombinations(b)
print s.letterCombinations("")