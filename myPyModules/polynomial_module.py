''' A module to be import and called @2019.07.31 Habibu'''
def poly(x):
	'''
	Evaluate the polynomial y = x³ - 7x² + 14x - 5
	'''
	return pow(x,3) - 7 * pow(x,2) + 14 * x - 5.0

if __name__ == '__main__':
	print ('Testing polynomial function')
	xValue = float(input('Enter value of x: '))
	yValue = poly(xValue)
	print ("The result of Y: ", yValue)


