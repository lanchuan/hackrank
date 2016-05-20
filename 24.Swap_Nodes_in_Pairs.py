import listnode

class Solution(object):
	def swapPairs(self, head):
		list0=listnode.ListNode(0)
		list0.next=head
		lis0=list0
		while list0.next!=None and list0.next.next!=None:
			swap(list0)
			list0=list0.next.next

		return lis0.next

def swap(node): 
	a=node.next
	b=node.next.next
	node.next=b
	a.next=b.next
	b.next=a

a=listnode.found([2,5,3,4,6,2,2])
s=Solution()
a=s.swapPairs(a)
listnode.printlis(a)
