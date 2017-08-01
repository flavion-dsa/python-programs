def cross_correlate(x, y, n1, n2):
	N1 = len(x)
	N2 = len(y)
	mi = n1-(n2+N2-1)
	mf = mi+(N1+N2-2)
	result = []
	
	for _ in range(N1-N2+1):
		y.append(0) 
	
	for arg in range(mi, mf+1):
		corr_sum = 0
		if arg < 0:
			negative = True
			limit = N1 + arg
		else:
			negative = False
			limit = N1 - arg
		
		for n in range(1, limit+1):
			if not negative:
				corr_sum += x[n+arg-1]*y[n-1]
			else:
				corr_sum += x[n-1]*y[n-arg-1]			
		result.append(corr_sum)
		
	print(result)	
	
def auto_correlate(x):
	N = len(x)
	mi = -(N-1)
	mf = mi+(2*N-2)
	result = []
	
	for arg in range(mi, mf+1):
		corr_sum = 0	
		if arg < 0:
			negative = True
			limit = N + arg
		else:
			negative = False
			limit = N - arg
		
		for n in range(1, limit+1):
			if not negative:
				corr_sum += x[n+arg-1]*x[n-1]
			else:
				corr_sum += x[n-1]*x[n-arg-1]
		result.append(corr_sum)
		
	print(result)
	
if __name__ == '__main__':
	print("=========== CORRELATION ===========")
	print("1. Cross correlate \n2. Auto correlate")
	choice = int(input())
	print("===================================")
	print("Enter samples for x(n) :")
	x = [float(temp) for temp in raw_input().split(' ')]
	if choice == 1:
		print("Enter start index for x(n) :")
		n1 = int(input())
		print("Enter samples for y(n) :")
		y = [float(temp) for temp in raw_input().split(' ')]
		print("Enter start index for y(n) :")
		n2 = int(input())
		cross_correlate(x, y, n1, n2)
	else:
		auto_correlate(x)
		
	
				
