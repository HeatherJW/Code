# imports the thing that reads files and imports random to make random numbers
from sys import argv
import random

# assigns some stuff to argv
script, filename = argv

# opens the file that the user specifies and assigns it to txt
txt = open(filename,'r')

# makes a list of the all the lines in the file
verbList = txt.readlines()

# closes the file
txt.close()

# actually tells the user what this is
print "Good day and welcome to the Dutch verb practice service."
print "This service will help you practice your Dutch verbs."
score = 0

for i in range(0,9):
	# picks a random number
	y = random.randint(1,6)

	# and uses that random number to find a random line of the file
	z = verbList[y]

	# splits the verb list at the ampersand and prints the result
	a = z.split('&')

	# makes the list of possible types of verb
	verbTypes = ['infinitive', 'imperfectum_s', 'imperfectum_p', 'perfectum', 'mhww']

	# pick one randomly
	b = random.randint(0,4)
	verbTypeChosen = verbTypes[b]

	# use that to make a string to ask the user 
	s = 'What is the ' + verbTypeChosen + ' for' + a[5]
	print s
	next = raw_input("> ")
	if next == a[b].strip():
		print "correct \n"
		print ""
		score += 1
	elif next != a[b].strip():
		print "incorrect \n"
		print ""
	else:
		print "error"

print "You scored %i out of 10."%score
