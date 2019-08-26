def cubicPoly(x,a,b,c,d):
	
	return (a * pow(x,3) + b * pow(x,2) + c * x + d)

if __name__ == '__main__':

	while True:
		
		xValue = float(input('Enter x value: '))
		if xValue == -1:
			print ('You enter the break keyword')
			break
		
		a,b,c,d = input('Enter the values of coefficinte a,b,c,d: ')
		yValue0 = cubicPoly(xValue, a,b,c,d,)
		yValue	= cubicPoly(xValue,3,4,1,9)
		print('The y value is: ', yValue0, 'Y value with coefficients', yValue)
		print ('Enter -1 to cancel')
		
