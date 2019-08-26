def tryCatch(a,b,c,d):

	try:
		arr = [a,b,c]
		for index in range(len(arr)):

			if (arr[index]):
				print 'The parameters are: %.2f' % arr[index] 
	except ValueError:
		print 'Value error occored'

if __name__ == '__main__':
	
	a,b,c,d = input('Enter the paramenters separated by commas: ')

	result = tryCatch(a,b,c,d)
	
	print '\n Function tryCatch() called: %.2f ' % result
	
				
