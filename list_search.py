friends = ['Ada','Adidas','Asaf','Will','Jackson','Sam','Samson','Wats','Bro','Last']
dateOfBirth = [1991,1992,1993,1990,2001,2004,1989,2005,1992,2019]

searchName = input("Enter a name: ")

total = len(friends)
position = friends.index(searchName)
dobPosition = dateOfBirth[position]

print "You have %.0f" % total ,  'friends'
print searchName, 'is number %.0f' % position, 'in your list'
print searchName, 'was born in %.0f' % dobPosition

