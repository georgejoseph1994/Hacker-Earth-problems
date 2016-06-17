no_testcase=int(raw_input())
for k in xrange(no_testcase):
	N,K,P=map(int,raw_input().split())
	#number_list=range(1,N+1)
	removal_nos=[]
	removal_nos=map(int,raw_input().split())
	for i in removal_nos:
		if i<P:
			P=P+1
		#number_list.remove(removal_nos[i])
	#if (len(number_list)-1<P):
	if (N-K)<P:
		print '-1'
	else:		
		print P



