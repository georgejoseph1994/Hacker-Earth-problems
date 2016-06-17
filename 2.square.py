no_of_transaction=int(raw_input())
transactions=[]

tr=raw_input()
transactions=tr.split()

for i in xrange(no_of_transaction):
	transactions[i]=int(transactions[i])
no_queries=int(raw_input())

for i in xrange(no_queries):
	target=int(raw_input())
	if (target > sum(transactions)):
			print '-1'
	else:		
		sum1=transactions[0]
		for k in xrange(0,len(transactions)):
			if sum1>=target:
				print k+1
				break
			else:	
				sum1=sum1+transactions[k+1]
		
