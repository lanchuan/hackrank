class Solution(object):
	def divide(self, dividend, divisor):
		def div(times,val):
			
			if val+val<=dividend:
				temp_times,temp_val=div(times+times,val+val)
				while temp_val+val<=dividend:
					temp_val+=val
					temp_times+=times
				#print temp_times,temp_val
				return temp_times,temp_val
			else:
				#print times,val
				return times,val

		if divisor==0:
			return -1 
		if divisor==1:
			return dividend
		flag=0
		if (divisor>0 and dividend<0) or (divisor<0 and dividend>0):
			flag=1
		dividend=abs(dividend)
		divisor=abs(divisor)
		if divisor<=dividend:
			temp1,temp2=div(1,divisor)
			if flag:
				temp1=0-temp1
			return min(max(-2147483648,temp1),2147483647)
		else:
			return 0

s=Solution()
print s.divide(56,3)

