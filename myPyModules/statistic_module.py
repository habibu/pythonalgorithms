def maxMin(*a):

	for index in range(len(a)):
		if(a[index] != 0 ):
			
			print 'Max number: ',max(a[index])
			print 'Min number: ',min(a[index])

def sumValues(*a):
	for index in range(len(a)):
		print 'Sum of numbers: ',sum(a[index])

def meanValues(*a):
	for index in range(len(a)):
		if(a[index] != 0 ):
	
			meanValue = float(sum(a[index]) / len(a[index]))
			print 'Mean value:  %.2f ' % meanValue

if   __name__ == '__main__':
	
	values = [1,2.1,3,4,5,6,7,89,10,-2.9,-1]

	print  maxMin(values)
	print  sumValues(values)
	print  meanValues(values)


