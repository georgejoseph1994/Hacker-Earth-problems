no_test_cases=int(raw_input())
for i in xrange(no_test_cases):
	N,K=map(int,raw_input(),split())
	loc=raw_input()
	location=[]
	location=loc.split()

	low=1,high=1e9,ans=-1
	
