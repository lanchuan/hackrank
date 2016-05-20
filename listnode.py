class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def found(lis):
	x=ListNode(0)
	h=x
	for i in lis:
		x.next=ListNode(i)
		x=x.next
	return h.next
def foundlis(lis):
	res=[]
	for i in lis:
		res.append(found(i))
	return res
def printlis(lis):
	while lis!=None:
		print lis.val
		lis=lis.next
def printheap(heap):
	i=1
	flag=1
	for x in heap:
		if i == flag:
			print x.val
			flag=2*flag+1
		elif i<flag:
			print x.val,
		i+=1
