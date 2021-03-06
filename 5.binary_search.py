def bin_srch(A,X):
	lo=0
	hi=len(A)
	while(lo<hi):
		mid=(lo+hi)//2
		midval=A[mid]
		if midval<X:
			lo=mid+1
		elif midval>X:
			hi=mid
		else:
			return mid
	return -1


if __name__=="__main__":
	N,Q=map(int,raw_input().split())
	A=[int(x) for x in raw_input().split()]
	A.sort()
	for i in xrange(Q):
		X=input()
		if bin_srch(A,X)!='-1':
			print "YES"
		else:
			print  "NO"


