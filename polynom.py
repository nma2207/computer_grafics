import os
def polynom(list, x):
	result=0
	#a(n)*x^n+a(n-1)*x^(n-1)+..+a(1)*x+a0==((((..((a(n)*x+a(n-1))*x+a(n-2))*x...)*x+a(1))*x+a0
	for i in list[-1::-1]:
		result*=x
		result+=i
	return result

os.system('cls')
print 'write elements of polynom, please'
list=[float(i) for i in raw_input().split()]
print 'write x,please'
x=float(raw_input())
print 'res=',polynom(list,x)