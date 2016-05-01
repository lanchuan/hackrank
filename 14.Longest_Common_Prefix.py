class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
        	return ""
        if len(strs)==1:
        	return strs[0]
        longest=strs[0]
        for i in strs[1:]:
        	j=-1
        	for j in range(min(len(longest),len(i))):
        		if i[j]!=longest[j]:
        			j=j-1
        			break
        	longest=longest[:j+1]
        return longest