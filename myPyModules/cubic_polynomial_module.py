''' Module to calculate cubic polynomial '''

def cubicPoly(x,a=1,b=2,c=4,d=4):
	''' 
		Function y = ax³ + bx² + cx + d 
	'''
	return (a * pow(x,3) + b * pow(x,2) + c * x + d)

if __name__ == '__main__':

	while True:
		
		xValue = float(input('Enter x value: '))
		if xValue == -1:
			print ('You enter the break keyword')
			break
		yValue0 = cubicPoly(xValue)
		yValue	= cubicPoly(xValue,3,4,1)
		print('The y value is: ', yValue0, 'Y value with coefficients', yValue)
		print ('Enter -1 to cancel')
		
