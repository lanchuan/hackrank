class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        if x<0:
            return False
        a=x
        base=1
        length=0
        while(a):
            a=a/10
            base=base*10
            length+=1
        base/=10
        for i in range(length/2):
            if x/base%10!=x%10:
                return False
            x/=10
            base/=100
        return True