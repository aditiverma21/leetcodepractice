def fib(N: int):
        # The most optimised solution of fibonacci
	prv1=0
	prv2=1
	sum=0
	if N==0:
		return 0
	if N==1:
		return 1
	for i in range(2,N+1):
		sum=prv1+prv2
		prv1=prv2
		prv2=sum

	return sum
	'''
	#using list
	sum=[0,1]
	for n in range(2,N+1):
		val=sum[n-1]+sum[n-2]
		sum.append(val)
		
	return sum[N]
	
	#recursion call
	if N==0:
		return 0
	elif N==1:
		return 1
	else:
		return self.fib(N-2)+self.fib(N-1)
	'''
n=int(input())	
result=fib(n)
print(result)