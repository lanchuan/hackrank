import listnode

class Solution(object):
	def reverseKGroup(self, head, k):
		if head==None:
			return head
		list0=listnode.ListNode(0)
		lis0=list0
		list0.next=head
	#	print list0.val
		while list0.next!=None:
			flag=True
			check=list0.next
			for i in range(k):
				if check==None:
					flag=False
					break
				check=check.next
			if flag==False:
				break
			list0.next=swap(list0.next,None,k-1)
			for i in range(k):
				list0=list0.next
			list0.next=check
		return lis0.next

def swap(head,head0,k):
	x=head.next
	head.next=head0
	if k==0:
		return head
	else:
		return swap(x,head,k-1)


s=Solution()
a=listnode.found([1,2,3,4,5])
b=s.reverseKGroup(a,2)
#b=swap(a,None,4)
listnode.printlis(b)

