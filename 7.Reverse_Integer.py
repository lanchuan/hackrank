class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        if s[0]=='-':
            x=0-int(s[:0:-1])
            if x<-2147483648:
                return 0
            else:
                return x
        else:
            x=int(s[::-1])
            if x>2147483647:
                return 0
            else:
                return x