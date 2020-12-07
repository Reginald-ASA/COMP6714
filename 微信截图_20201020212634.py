# Generating Elias-gamma and Elias-delta codes in Python
import math


def unary_encode(n):
	return '1' * n + '0'


def binary_encode(n, width):
	r = ''
	for i in range(0,width): 
		if ((1<<i) & n) > 0:
			r = "1" + r 
		else:
			r = '0' + r
	return r


def gamma_encode (n):
	logn = int(math.log(n,2))
	return unary_encode( logn ) + " " + binary_encode(n, logn)


def delta_encode(n): 
	logn = int(math.log(n,2))
	if n == 1:
		return "0" 
	else:
		loglog = int(math.log(logn+1,2))
		residual = logn+1 - int(math.pow(2, loglog))
		return unary_encode( loglog ) + ' ' + binary_encode( residual, loglog ) + ' ' + binary_encode(n, logn)


if __name__ == "__main__":
	res = ''
	temp = 0
	for n in [1,2,7,13,8,11,91]:
		print(n+temp)
		temp += n
	for n in [1,2,7,13,8,11,91]:
		logn = int(math.log(n,2))
		loglogn = int(math.log(logn+1,2))
		print( n, "d_r", logn )
		print( n, "d_dd", loglogn)
		print( n , "d_dr", logn +  1 - int(math.pow(2,loglogn)))
		term = delta_encode(n)
		print( n, "can encode to", term)
		res += term
		# print( n, "gamma",  gamma_encode(n))
		# print( n, "binary", binary_encode(n))
	res = res.replace(' ','')
	res1 = ''
	for i in range(len(res)):
		c = res[i]
		if (i+1) % 8 == 0:
			c += ' '
		res1 += c
	print(res1)
