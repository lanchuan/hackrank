class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		head=ListNode(0)
		result=head
		if l1==None:
			return l2
		if l2==None:
			return l1
		while l1!=None and l2!=None:
			if l1.val<=l2.val:
				head.next=l1
				head=head.next
				l1=l1.next
			else:
				head.next=l2
				head=head.next
				l2=l2.next
		if l1==None:
			head.next=l2
		elif l2==None:
			head.next=l1
		return result.next


a=ListNode(1)
b=ListNode(2)
ha=a
hb=b
for i in range(2,8,2):
	print i
	x=ListNode(i)
	a.next=x
	a=a.next
for j in range(3,9,3):
	print j
	x=ListNode(j)
	b.next=x
	b=b.next
s=Solution()
r=s.mergeTwoLists(ha,hb)
while r!=None:
	print r.val
	r=r.next

