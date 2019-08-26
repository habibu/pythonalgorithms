def tryCatch(a,b,c,d):

		arr = [a,b,c,d]
		for index in range(len(arr)):
			
			try:
				if (arr[index] == ''):

					print 'The parameters are: ', float( arr)
		
			except (ValueError,NameError,TypeError,SyntaxError):
				print '\n The paramenters are:', arr == null,
			
if __name__ == '__main__':
	
	a,b,c,d = input('Enter the paramenters separated by commas: ')

	result = tryCatch(a,b,c,d)
	
	print '\n Function tryCatch() called: ...'
	
				
