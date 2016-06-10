class RandomListNode(object):
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution(object):
	def copyRandomList(self, head):
		if not head:
			return None
		p=head
		d={}
		while p:
			d[p]=RandomListNode(p.label)
			p=p.next
		d[None]=None
		p=head
		while p:
			d[p].next=d[p.next]
			d[p].random=d[p.random]
			p=p.next
		return d[head]
