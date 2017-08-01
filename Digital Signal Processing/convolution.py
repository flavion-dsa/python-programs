def linear_convolve(x, h):
	m = len(x)
	n = len(h)
	y = []
	
	for i in range(1, m+n):
		conv_sum = 0
		for j in range(1, i+1):
			if (i-j+1) <= n and j <= m:
				conv_sum += x[j-1]*h[i-j]
		y.append(round(conv_sum, 2))
		
	print("y(n) : ")
	print(y)
	
def circular_convolve(x, h):
	if len(x) != len(h):
		print("Can't perform circular convolution")
		return
		
	y = []
	
	for n in range(len(x)):
		conv_sum = 0
		for m in range(len(h)):
			conv_sum += x[m]*h[(n-m)%len(h)]
		y.append(round(conv_sum, 2))
	
	print("y(n) : ")
	print(y)
	
if __name__ == '__main__':
	print("========== CONVOLUTION ==========")
	print("Enter samples for signal x(n) :")
	x = [float(temp) for temp in raw_input().strip().split(' ')]
	print("Enter samples for signal h(n) :")
	h = [float(temp) for temp in raw_input().strip().split(' ')]
	print("=================================")
	print("1. Linear Convolute \n2. Circular Convolute")
	print("=================================")
	choice = lambda i: linear_convolve(x, h) if i == 1 else circular_convolve(x, h)
	choice(int(input()))
	

