no_test_case=int(raw_input())
for i in xrange(no_test_case):
	A,B,C,D,K=map(int,raw_input().split())
	t=1
	f=1
	while f<=k:
		t=t+1
		f=A*pow(t,3)+B*pow(t,2)+C*t+D
	print t-1
