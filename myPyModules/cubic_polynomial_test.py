import cubic_polynomial_moduleB as cubicb


for num in range(-5,5,5):
	
	xValue = float(input('Enter x value: '))
	if xValue == -1:
		print ('You enter the break keyword')
		break
	a,b,c,d = input('Enter values as a,b,c,d')
	yValue = cubicb.cubicPoly(xValue,a,b,c,d)
	print('The y value is: ', yValue)
	print ('Enter -1 to cancel')
	
