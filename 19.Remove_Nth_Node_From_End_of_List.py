# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		p=head
		q=head
		if head== None:
			return None
		if n<1:
			return None
		p=head
		for i in range(n):
			if p.next!=None:
				p=p.next
			else:
				if i==n-1:
					return head.next
				return None
		while p.next!=None:
			p=p.next
			q=q.next
		q.next=q.next.next
		return head

head=ListNode(0)
h=head
for i in range(1,3):
	print i
	a=ListNode(i)
	head.next=a
	head=a
h=h.next
s=Solution()
h=s.removeNthFromEnd(h,2)
while h!=None:
	print h.val
	h=h.next