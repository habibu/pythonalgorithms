a = input ('Enter a number: ')
b = input ('Enter another number: ')

try:
	print a/b
except ZeroDivisionError:
	print 'The second number must not be zero'
