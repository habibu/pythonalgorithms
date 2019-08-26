prompt = 'Please enter a positive number less than 10:'

x = -1  # Initialise x to an invalide number

while x <= 0 or x > 9:
	x = float(raw_input(prompt))

print 'Thank you. That number is  OK'


