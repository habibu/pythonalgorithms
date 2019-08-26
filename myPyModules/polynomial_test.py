import polynomial_module as polymodule


while True:

	xValue = float(input("Enter a value for x: "))

	test = polymodule.poly(xValue)
	if (xValue == 0):
		print ('You enter breaking value')
		break
	print ("Y value tt:   ",test )
	print ('Enter 0 to break the loop')
