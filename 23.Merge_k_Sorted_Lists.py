# Definition for singly-linked list.
import listnode

class Solution(object):
	def mergeKLists(self, lists):
		#make a heap
		heap=[]
		result=listnode.ListNode(0)
		pointer=result
		for i in lists:
			if i==None:
				continue
			heap.append(i)
			l=len(heap)
			while l>1:
				if heap[l-1].val<heap[l/2-1].val:
					swap(heap,l-1,l/2-1)
					l=l/2
				else:
					break
		if len(heap)==1:
			return heap[0]
		while heap!=[]:
			pointer.next=heap[0]
			if heap[0].next!=None:
				heap[0]=heap[0].next
				adjust(heap)
			else:
				heap[0]=heap[-1]
				heap.pop()
				adjust(heap)
			pointer=pointer.next
		return result.next
		
def adjust(heap):
	index=0
	l=len(heap)-1
	while 2*(index+1)<=l:
		if heap[2*(index+1)-1].val>heap[2*(index+1)].val:
			if heap[index].val>heap[2*(index+1)].val:
				swap(heap,index,2*(index+1))
				index=2*(index+1)
			else:
				break
		else:
			if heap[index].val>heap[2*(index+1)-1].val:
				swap(heap,index,2*(index+1)-1)
				index=2*(index+1)-1
			else:
				break

	if 2*(index+1)-1==l:
		if heap[index].val>heap[2*(index+1)-1].val:
			swap(heap,index,l)

def swap(heap,a,b):
	temp=heap[a]
	heap[a]=heap[b]
	heap[b]=temp

a=[[-6,-6,-4,2],[-10,-5,0,1,1,1,1,3,3],[-10,-10,-4,-3,0,1,1],[-10,-6,-6,-5,-4,-4,-3,3,4],[],[-5,-5,-3,2,2],[0],[-10,-7,-6,-2,-1,1,1,2]]
x=listnode.foundlis(a)
s=Solution()
b=s.mergeKLists([listnode.ListNode(1),None])
y=s.mergeKLists(x)
while y!=None:
	print y.val
	y=y.next