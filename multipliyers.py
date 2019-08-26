x,y,z = input('Enter Start, Stop, Increment; ')
test = x,y,z

for number in range(x,y,z):
	s = pow(number,2)
	c = pow(number,3)
	print ('Number ',number, 'Square ', s, 'Cube ', c)
	
