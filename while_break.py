prompt = 'Test break by enter 5: '

while True:
	a = float(raw_input(prompt))
	if (a == 5):
		break
		print 'Congrats u break a break'
	else:
		print 'Keep trying'
