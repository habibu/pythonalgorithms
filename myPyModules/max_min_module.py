def maxMin(*a):

	for index in range(len(a)):

		if(a[index] != 0 ):
			
			print 'Max num',max(a[index])
			print 'Min',min(a[index])

if   __name__ == '__main__':
	
	values = [1,2.1,3,4,5,6,7,89,10,-2.9,-1]

	print 'Result: ', maxMin(values)


