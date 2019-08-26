''' Habibu Abdullahi @2019.0731 '''
import cubic_polynomial_module as cubic

''' Test for  function to calculate cubic polynomial '''

while True:
	
	xValue = float(input('Enter x value: '))
	if xValue == -1:
		print ('You enter the break keyword')
		break
	yValue = cubic.cubicPoly(xValue)
	print('The y value is: ', yValue)
	print ('Enter -1 to cancel')
	
