def poly(x):
	'''
	Evaluate the polynomial y = x³ - 7x² + 14x - 5
	'''
	return pow(x,3) - 7 * pow(x,2) + 14 * x - 5.0

while True:
	
	xValue = float(input("Enter a value for x: "))
	if (xValue == 0):
		print ('You enter breaking value')
		break
	yValue = poly(xValue)
	print ("Y value:   ",yValue )
	print ('Enter 0 to break the loop')
