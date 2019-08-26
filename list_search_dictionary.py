friends_dictionary = {
	'Ada':'1991','Adidas':'1992','Asaf':'1990','Will':'2001','Jackson':'2004','Sam':'1989','Samson':'2005','Wats':'1994','Bro':'2010','Last':'2019'}



while True:

	searchName = raw_input("Enter a name: ")
	if not searchName:
		print "You forget to enter name:"
		break
	
	total = len(friends_dictionary)

	position = list(friends_dictionary).index(searchName)
	dobPosition = friends_dictionary[searchName]

	print "You have %.0f" % total ,  'friends'
	print searchName, 'is number %.0f' % position, 'in your list'
	print searchName, 'was born in ' , dobPosition

