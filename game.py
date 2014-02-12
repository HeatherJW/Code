from sys import exit
from random import randint
import random

inventory = []
points = []

class Game(object):

#defines the starting point and end quips
	def __init__(self, start):
		self.quips = [
			"Well done on finding the way of death.",
			"You have managed to kill yourself. Congratulations.",
			"With a small sigh you shuffle off this mortal coil.",
			"When you die, you loose an important part of yourself.",
			"Oh wow, you mean I am not immortal?"
		]
		self.start = start

#defines the game play order	
	def play(self):
		next = self.start
		
		while True:
			print "\n--------"
			room = getattr(self, next)
			next = room()

#defines what happens when you die			
	def death(self):
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1) 

#The first scene of the game. A beautiful beach with views of meadows, forest and mountains. From here you can go East to MeadowOne, North to BeachThree or South to BeachTwo
	def Beach_One(self):
		print "You have landed on a strange beach. A stream flows into the sea."
		if (inventory.count('bottle') == 0):
			print "An old bottle is lying on the ground. Sad to think that even in this pristine place there is rubbish."
			print "So what now? Should we at least pick up that bottle?"
		
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('take')
			output2 = next.find('yes')
			if output1 == 0 or output2 == 0:
				print "There is a message in the bottle. You read it."
				print "It says: 'The way home can only be found if you find the secret objects located on this island. Once you have found them, you must find the place where it all comes to an end. From there you can go home. It may help to know that you are on the western side of the island. The mountains are to the north.'"
				points.append(1)
				x = points.count(1)
				print "You have gained a point. You now have %i out of 6."%x
				inventory.append('bottle')
				return 'Beach_One'
			elif output1 != 0 or output2 != 0:
				print "Well walk somewhere or do something. Try typing east."
			
				next = raw_input("> ")
				next = next.lower()
				output1 = next.find('east')
				output2 = next.find('south')
				output3 = next.find('north')
				output4 = next.find('west')
		
				if output1 == 0:
					return 'Meadow_One'
				elif output4 == 0:
					print "You swim out to sea. After swimming aimlessly for some time, you grow tired and realise you have lost land."
					return 'death'
				elif output3 == 0:
					return 'Beach_Three'
				elif output2 == 0:
					return 'Beach_Two' 
				else:
					print "Choose a direction."
					return 'Beach_One' 
			else: 
				return 'Beach_One'		
		else:
			print "Which way then?"
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('east')
			output2 = next.find('south')
			output3 = next.find('north')
			output4 = next.find('west')
		
			if output1 == 0:
				return 'Meadow_One'
			elif output4 == 0:
				print "You swim out to sea. After swimming aimlessly for some time, you grow tired and realise you have lost land."
				return 'death'
			elif output3 == 0:
				return 'Beach_Three'
			elif output2 == 0:
				return 'Beach_Two' 			
			else:
				print "Choose a direction."
				return 'Beach_One'
				
# A beach scene. Links to BeachOne (North) and BeachFour (South) 
	def Beach_Two(self):
		print "You are walking along a pristine beach. To the east is a dense forest that you cannot walk through. To the north and south is more beach."
		
		if (inventory.count('shell') == 0):
			print "A shell catches your eye. Do you take the shell?"
		
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('take')
			output2 = next.find('yes')
			if output1 == 0 or output2 == 0:
				points.append(1)
				x = points.count(1)
				print "You have gained a point. You now have %i out of 6."%x
				inventory.append('shell')
				return 'Beach_Two'
				
			elif output1 != 0 or output2 != 0:
				print "Well walk somewhere or do something."
			
				next = raw_input("> ")
				next = next.lower()
				output1 = next.find('east')
				output2 = next.find('south')
				output3 = next.find('north')
				output4 = next.find('west')
		
				if output1 == 0:
					print "The forest is too dense."
					return 'Beach_Two'
				elif output4 == 0:
					print "You swim out to sea. After swimming aimlessly for some time, you grow tired and realise you have lost land."
					return 'death'
				elif output3 == 0:
					return 'Beach_One'
				elif output2 == 0:
					return 'Beach_Four' 
				else:
					print "Choose a direction."
					return 'Beach_Two' 
			else: 
				return 'Beach_Two'		
		else:
			print "Which way then?"
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('east')
			output2 = next.find('south')
			output3 = next.find('north')
			output4 = next.find('west')
		
			if output1 == 0:
				print "The forest is too dense to walk through."
				return 'Beach_Two'
			elif output4 == 0:
				print "You swim out to sea. After swimming aimlessly for some time, you grow tired and realise you have lost land."
				return 'death'
			elif output3 == 0:
				return 'Beach_One'
			elif output2 == 0:
				return 'Beach_Four' 			
			else:
				print "Choose a direction."
				return 'Beach_Two'

# A beach scene. Links to BeachOne (South), CliffsOne (North) and SlopesOne (East)
	def Beach_Three(self):
		print "You are walking along a pristine beach. To the east is the slopes of a huge mountain. To the north and south is more beach. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			return 'Slopes_One'
		elif output2 == 0:
			print 'You swim out to sea. After a while a huge shark finds you.'
			return 'death'
		elif output3 == 0:
			return 'Beach_One'
		elif output4 == 0:
			return 'Cliffs_One'
		else:
			print "Choose a sensible direction."
			return 'Beach_Three'

# A beach scene. Links to BeachTwo (North) and BeachFive (South) 
	def Beach_Four(self):
		print "You are walking along a pristine beach. To the east is a dense forest that you cannot walk through. But there must be a way in. To the north and south is more beach. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			print "You cannot go that way. The forest is too dense."
			return 'Beach_Four'
		elif output2 == 0:
			print 'You swim out to sea. After a while you are disoriented and lost.'
			return 'death'
		elif output3 == 0:
			return 'Beach_Five'
		elif output4 == 0:
			return 'Beach_Two'
		else:
			print "Choose a sensible direction."
			return 'Beach_Four'
			
# A beach scene. Links to BeachFour (North) 
	def Beach_Five(self):
		print "You are walking along a pristine beach. To the east is a dense forest that you cannot walk through. To the south and the west is sea. This clearly is not how you get in there. From here, you can see far out to sea, but alas you have not a boat. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			print "You cannot go that way. The forest is too dense."
			return 'Beach_Five'
		elif (output2 == 0) or (output3 == 0):
			print 'You swim out to sea. After a while you are disoriented and lost.'
			return 'death'
		elif output4 == 0:
			return 'Beach_Four'
		else:
			print "Choose a sensible direction."
			return 'Beach_Five'			

# A beach scene. Links to BeachSeven (North)
	def Beach_Six(self):
		print "You are standing at the South East corner of the island. The sea laps gently against the beach. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if (output3 == 0) or (output1 == 0):
			print 'You swim out to sea. After a while a huge shark finds you.'
			return 'death'
		elif output2 == 0:
			print "You cannot go that way. That forest is too dense."
			return 'Beach_Six'
		elif output4 == 0:
			return 'Beach_Seven'
		else:
			print "Choose a sensible direction."
			return 'Beach_Six'			
			
# A beach scene. Links to BeachSix (South) and BeachEight (North)
	def Beach_Seven(self):
		print "More pristine beach. It makes you want to lie down and sleep in the sun. The sea laps gently against the beach. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			print 'You swim out to sea. After a while a huge shark finds you.'
			return 'death'
		elif output2 == 0:
			print "You cannot go that way. That forest is too dense."
			return 'Beach_Seven'
		elif output3 == 0:
			return 'Beach_Six'
		elif output4 == 0:
			return 'Beach_Eight'
		else:
			print "Choose a sensible direction."
			return 'Beach_Seven'
			
# A beach scene. Links to BeachSeven (South) and BeachNine (North)
	def Beach_Eight(self):
		print "More pristine beach. What is wrong with this island, can there not at least be a palm tree? The sea laps gently against the beach. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			print 'You swim out to sea. After a while a huge shark finds you.'
			return 'death'
		elif output2 == 0:
			print "You cannot go that way. That forest is too dense."
			return 'Beach_Eight'
		elif output3 == 0:
			return 'Beach_Seven'
		elif output4 == 0:
			return 'Beach_Nine'
		else:
			print "Choose a sensible direction."
			return 'Beach_Eight'	
			
# A beach scene. Links to BeachEight (South) and BeachTen (North) . Also to MeadowFour (west)
	def Beach_Nine(self):
		print "Great, another beach. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			print 'You swim out to sea. After a while a huge shark finds you.'
			return 'death'
		elif output2 == 0:
			return 'Meadow_Four'
		elif output3 == 0:
			return 'Beach_Eight'
		elif output4 == 0:
			return 'Beach_Ten'
		else:
			print "Choose a sensible direction."
			return 'Beach_Nine'		
			
# A beach scene. Links to BeachNine (South) and BeachEleven (North) and SlopesFour (West)
	def Beach_Ten(self):
		print "Oh wow, a palm tree. That breaks the endless beach scene. The sea laps gently against the beach. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			print 'You swim out to sea. After a while a huge shark finds you.'
			return 'death'
		elif output2 == 0:
			return 'Slopes_Four'
		elif output3 == 0:
			return 'Beach_Nine'
		elif output4 == 0:
			return 'Beach_Eleven'
		else:
			print "Choose a sensible direction."
			return 'Beach_Ten'	
			
# A beach scene. Links to BeachTen (South)
	def Beach_Eleven(self):
		print "You have found another corner of the island. Mighty cliffs rise up behind you. The sea laps gently against the beach. Which way?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if (output1 == 0) or (output4 == 0):
			print 'You swim out to sea. After a while a huge shark finds you.'
			return 'death'
		elif output2 == 0:
			print "You cannot go that way. That forest is too dense."
			return 'Beach_Eleven'
		elif output3 == 0:
			return 'Beach_Ten'
		else:
			print "Choose a sensible direction."
			return 'Beach_Eleven'			

# Impressive cliff scene,  links to BeachThree (South)
	def Cliffs_One(self):
		print 'You are standing at the top of some magnificent cliffs.'
		print 'The land falls steeply into the sea here.'
		print 'You could get seriously hurt.'
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			print "You cannot go that way at present, tell the author to code it in."
			return 'Cliffs_One'
		elif output2 == 0:
			print 'You swim out to sea. After a while a huge shark finds you.'
			return 'death'
		elif output3 == 0:
			return 'Beach_Three'
		elif output4 == 0:
			print "You plummet down to the rocks below."
			return 'death'
		else:
			print "Choose a sensible direction."
			return 'Beach_Three'
			
# The slopes of the mountain. Links to BeachThree (West), MeadowOne (South) and SlopesTwo (East)
	def Slopes_One(self):
		print "You are standing on the slopes of a mountain. To the west is a beach, to the north a mountain." 
		
		if (inventory.count('flower') == 0):
			print "There is a stunning flower that will look so good in your hair."
			print "Do you take the flower?"
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('take')
			output2 = next.find('yes')
		
			if output1 == 0 or output2 == 0:
				points.append(1)
				x = points.count(1)
				print "You have gained a point. You now have %i out of 6."%x
				print "Great idea. You never know when you will need a flower."
				inventory.append('flower')
				return 'Slopes_One'
			elif output1 == 0 or output1 != 0:
				print "Which direction do you wish to go?"
				next = raw_input("> ")
				next = next.lower()
				output1 = next.find('south')
				output2 = next.find('east')
				output3 = next.find('north')
				output4 = next.find('west')
			
				if output1 == 0:
					return "Meadow_One"
				elif output2 == 0: 
					return 'Slopes_Two'
				elif output3 == 0:
					print "The mountain is to steep to climb."
					return 'Slopes_One'
				elif output4 == 0:
					return 'Beach_Three'
			else:
				print "Learn to type idiot."
				return 'Slopes_One'
		else: # stops the user seeing the flower after they have it
			print "Which direction do you wish to go?"
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('south')
			output2 = next.find('east')
			output3 = next.find('north')
			output4 = next.find('west')
			
			if output1 == 0:
				return "Meadow_One"
			elif output2 == 0: 
				return 'Slopes_Two'
			elif output3 == 0:
				print "The mountain is to steep to climb."
				return 'Slopes_One'
			elif output4 == 0:
				return 'Beach_Three'
			else:
				print "Learn to type idiot."
				return 'Slopes_One'
			
# The slopes of the mountain. Links to MeadowTwo (South), MountainOne (East) and SlopesOne (West)			
	def Slopes_Two(self):
		print "You are standing on the slopes of a mountain. There is a pretty meadow all around you. To the north a mountain."
		print "Where do you wish to go?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			return 'Mountain_One'
		elif output2 == 0:
			return 'Slopes_One'
		elif output3 == 0: 
			return 'Meadow_Two'
		elif output4 == 0:
			print "The mountain is to steep to climb. Choose another direction."
			return 'Slopes_Two'
		else: 
			print "What? Are you just going to sit here all day?"
			return 'Slopes_Two'

# The slopes of the mountain. Links to PondCrossroad (South), MountainOne (West)			
	def Slopes_Three(self):
		print "You are standing on the slopes of a mountain. There is a pretty meadow all around you. To the north a mountain."
		print "Where do you wish to go?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			return 'Slopes_Four'
		elif output2 == 0:
			return 'Mountain_One'
		elif output3 == 0: 
			return 'Pond_Crossroad'
		elif output4 == 0:
			print "The mountain is to steep to climb. Choose another direction."
			return 'Slopes_Three'
		else: 
			print "What? Are you just going to sit here all day?"
			return 'Slopes_Three'

# The slopes of the mountain. Links to MeadowFour (South), SlopesThree (West), BeachTen (East)			
	def Slopes_Four(self):
		print "You are standing on the slopes of a mountain. There is a pretty meadow all around you. To the north a mountain."
		print "Where do you wish to go?"
		
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			return 'Beach_Ten'
		elif output2 == 0:
			return 'Slopes_Three'
		elif output3 == 0: 
			return 'Meadow_Four'
		elif output4 == 0:
			print "The mountain is to steep to climb. Choose another direction."
			return 'Slopes_Four'
		else: 
			print "What? Are you just going to sit here all day?"
			return 'Slopes_Four'


#A meadow scene. Links to MeadowTwo (East), BeachOne (West) and SlopesOne (North)
	def Meadow_One(self):
		print "You are in a beautiful meadow. There is a gently flowing stream. A path leads east."
		print "To the west and south is dense forest, to the north is a mountain."
		print "Where to now?" 
	
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('east')
		output2 = next.find('west')
		output3 = next.find('south')
		output4 = next.find('north')
		
		if output1 == 0:
			return 'Meadow_Two'
		elif output2 == 0:
			return 'Beach_One'
		elif output3 == 0:
			print "You cannot go that way."
			return 'Meadow_One'
		elif output4 == 0:
			return 'Slopes_One'
		else: 
			print "What? Are you just going to sit here all day?"
			return 'Meadow_One'

#Another meadow scene with a branching path. Leads to MeadowThree (East) or ForestOne (South) (or back to MeadowOne (West))	or SlopesTwo (North)	
	def Meadow_Two(self):
		print "You are walking alongside a gently flowing stream. A path leads from west to east."
		print "There is also a path heading south through the forest."
		print "To the north is a mountain."
		print "Which way do you go?"
	
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('south')
		output2 = next.find('east')
		output3 = next.find('north')
		output4 = next.find('west')
		
		if output1 == 0:
			return 'Forest_One'
		elif output2 == 0:
			return 'Meadow_Three'
		elif output3 == 0:
			return 'Slopes_Two'
		elif output4 == 0:
			return 'Meadow_One'
		else:
			print "Choose a direction."
			return 'Meadow_Two' 

#And another meadow scene with a branching path. You can go to MountainOne (North), MeadowTwo (West) or PondCrossroad (East)	
	def Meadow_Three(self):
		print "You are walking alongside a gently flowing stream. A path leads from west to east."
		print "There is also a path heading north towards the mountain."
		print "To the south is dense forest."
		print "Which way do you go?"
	
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('south')
		output2 = next.find('east')
		output3 = next.find('north')
		output4 = next.find('west')
	
		if output3 == 0:
			return 'Mountain_One'
		elif output2 == 0:
			return 'Pond_Crossroad'
		elif output1 == 0:
			print "You cannot go that way. The forest is impenatrable at this point."
			return 'Meadow_Three'
		elif output4 == 0:
			return 'Meadow_Two'
		else:
			print "Choose a direction." 
			return 'Meadow_Three'

#More meadow. You can go to PondsCrossroad (West) and SlopesFour (North)
	def Meadow_Four(self):
		print "Yet more of the same pristine meadow. Sigh."
		print "To the south is dense forest."
		print "Which way do you go?"
	
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('south')
		output2 = next.find('east')
		output3 = next.find('north')
		output4 = next.find('west')
	
		if output3 == 0:
			return 'Slopes_Four'
		elif output2 == 0:
			print "That direction does not yet exist."
			return 'Meadow_Four'
		elif output1 == 0:
			print "You cannot go that way. The forest is impenatrable at this point."
			return 'Meadow_Three'
		elif output4 == 0:
			return 'Pond_Crossroad'
		else:
			print "Choose a direction." 
			return 'Meadow_Four'

#The huge mountain. With a cave. Branches off MeadowThree (South). Leads to CaveOne (North). Can be accessed from SlopesTwo (West) and SlopesThree (East)
	def Mountain_One(self):
		print "You are staring at a huge mountain. There is a cave to the north."
		print "Do you enter the cave?"
		
		next = raw_input("> ") 
		next = next.lower()
		output1 = next.find('yes')
		output2 = next.find('enter')
		
		if output1 == 0 or output2 == 0:
			return 'Cave_One'
		elif output1 != 0 or output2 != 0:
			print "Which direction do you want to go?"
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('south')
			output2 = next.find('east')
			output3 = next.find('north')
			output4 = next.find('west')
			
			if output1 == 0:
				return 'Meadow_Three'
			elif output4 == 0:
				return 'Slopes_Two'
			elif output2 == 0:
				return 'Slopes_Three'
			elif output3 == 0:
				return 'Cave_One'
			else:
				print "There is clearly a problem between chair and keyboard."
				return 'Mountain_One'
		else:
			print "Learn to type moron."
			return 'Mountain_One'

#Inside a cave. Possibility of sudden death. Comes from MountainOne (South) and leads nowhere
	def Cave_One(self):
		print "You are in a dark cave." 
		print "You may be eaten by something nasty."
		options = random.choice(['live', 'die'])
		if options == 'live':
			if (inventory.count('platinum') == 0):
				print "A brief flash of light reveals a bar of platinum."
				print "Do you take the platinum?"
				next = raw_input("> ")
				next = next.lower()
				output1 = next.find('take')
				output2 = next.find('yes')
		
				if output1 == 0 or output2 == 0:
					points.append(1)
					x = points.count(1)
					print "You have gained a point. You now have %i out of 6."%x
					print "Great idea. You never know when you will need it."
					inventory.append('platinum')
					return 'Cave_One'
				elif output1 == 0 or output1 != 0:
					print "Which direction do you wish to go?"
					next = raw_input("> ")
					next = next.lower()
					output1 = next.find('south')
					output2 = next.find('east')
					output3 = next.find('north')
					output4 = next.find('west')
			
					if output1 == 0:
						return "Mountain_One"
					elif (output2 == 0) or (output3 == 0) or (output4 == 0): 
						print "You fell into a chasm."
						return 'death'
				else:
					print "Learn to type idiot."
					return 'Cave_One'
			else: # stops the user seeing the platinum after they have it
				print "Which direction do you wish to go?"
				next = raw_input("> ")
				next = next.lower()
				output1 = next.find('south')
				output2 = next.find('east')
				output3 = next.find('north')
				output4 = next.find('west')
				
				if output1 == 0:
					return "Mountain_One"
				elif (output2 == 0) or (output3 == 0) or (output4 == 0): 
					print "You fell into a chasm."
					return 'death'
				else:
					print "Learn to type idiot."
					return 'Cave_One'
		else: 
			print "Oh no! It got you! Run for your life! To late!"
			return 'death'		
#Branches off MeadowTwo (North). A forest. Leads to ForestTwo (South).	
	def Forest_One(self):
		print "You are walking through a dense forest. A path leads from north to south."
		print "To the east and west is dense forest."
		print "Which way?"
	
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('south')
		output2 = next.find('east')
		output3 = next.find('north')
		output4 = next.find('west')
	
		if output1 == 0:
			return 'Forest_Two'
		elif output3 == 0:
			return 'Meadow_Two'
		elif (output2 == 0) or (output4 == 0):
			print "You cannot go that way."
			return 'Forest_One'
		else:
			print "Choose a direction."
			return 'Forest_One'

#From ForestOne (North). More forest, a dead end and a tree with fruit. 		
	def Forest_Two(self):
		print "To the east, west and south is dense forest."
		if (inventory.count('fruit') == 0):
			print "There is a tall, lush tree in front of you. The tree is heavy with fruit."
			print "Do you take the fruit?"
	
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('take')
			output2 = next.find('yes')
		
			if output1 == 0 or output2 == 0:
				points.append(1)
				x = points.count(1)
				print "You have gained a point. You now have %i out of 6."%x
				print "Good choice"
				inventory.append('fruit')
				return 'Forest_Two'
			elif output1 != 0 or output2 != 0:
				print "Which way then?"
				next = raw_input("> ")
				next = next.lower()
				output1 = next.find('south')
				output2 = next.find('east')
				output3 = next.find('north')
				output4 = next.find('west')
				if output3 == 0:
					return 'Forest_One'
				elif (output1 == 0) or (output2 == 0) or (output4 == 0):
					print "You cannot go that way."
					return 'Forest_Two'
				else:
					print "Choose a direction."
					return 'Forest_Two'
		else:
			print "There is a tall, lush tree in front of you."
			print "Which way then?"
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('south')
			output2 = next.find('east')
			output3 = next.find('north')
			output4 = next.find('west')
			if output3 == 0:
				return 'Forest_One'
			elif (output1 == 0) or (output2 == 0) or (output4 == 0):
				print "You cannot go that way."
				return 'Forest_Two'
			else:
				print "Choose a direction."
				return 'Forest_Two'
			
#Comes from MeadowThree (West). A pond. Leads to a house (South). Links to MeadowFour (East) and SlopesThree (North)
	def Pond_Crossroad(self):
		print "You are at a crossroads. The path leads east, west, south and north from here."
		print "There is a pond with a frog in it. The frog looks like it knows something. Try talking to the frog."
		next = raw_input("> ")
		next = next.lower()
		output1 = next.find('talk')
		if output1 == 0:
			frogTalk = ['Have you found the gleaming gem?', 'I would be careful around those cliffs if I were you.', 'Do you like to swim? I only like to swim in the pond, it is safer here.', 'What is there to eat here? I like fruit and gingerbread, do you?', 'There are many ways to die on this island, but only one way home.']
			print frogTalk[randint(0, len(frogTalk)-1)]
			print "Which way?"
	
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('south')
			output2 = next.find('east')
			output3 = next.find('north')
			output4 = next.find('west')
	
			if output3 == 0:
				return 'Slopes_Three'
			elif output2 == 0:
				return 'Meadow_Four'
			elif output1 == 0:
				return 'house'
			elif output4 == 0:
				return 'Meadow_Three'
			else:
				print "Well don't just stand there, do something."
				return 'Pond_Crossroad'
		elif output1 != 0:
			print "Which way?"
	
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('south')
			output2 = next.find('east')
			output3 = next.find('north')
			output4 = next.find('west')
	
			if output2 == 0:
				return 'Meadow_Four'
			elif output1 == 0:
				return 'house'
			elif output3 == 0:
				return 'Slopes_Three'
			elif output4 == 0:
				return 'Meadow_Three'
			else:
				print "Well don't just stand there, do something."
				return 'Pond_Crossroad'
	
#A pretty house. Comes from PondCrossroad (North). Leads to the end (South).
	def house(self):
		print "You are walking through a forest. A path leads north-south."
		if (inventory.count('house') == 0):
			print "There is a gingerbread cottage here."
			print "You realise you are quite hungry."
			print "Do you eat some of the house?"
	
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('eat')
			output2 = next.find('yes')
		
			if output1 == 0 or output2 == 0:
				points.append(1)
				x = points.count(1)
				print "You have gained a point. You now have %i out of 6."%x
				print "Yum, yum."
				inventory.append('house')
				return 'house'
			elif output2 != 0 or output1 != 0:
				print "Pick a direction"
				next = raw_input("> ")
				next = next.lower()
				output1 = next.find('south')
				output2 = next.find('east')
				output3 = next.find('north')
				output4 = next.find('west')
				
				if output1 == 0:
					return 'End_One'
				elif (output2 == 0) or (output4 == 0):
					print "You cannot go that way."
					return 'house'
				elif output3 == 0:
					return 'Pond_Crossroad'
				else: 
					print "Pick a direction or do something."
					return 'house'
		else:
			print "There is a half-eaten gingerbread cottage."
			print "Pick a direction"
			next = raw_input("> ")
			next = next.lower()
			output1 = next.find('south')
			output2 = next.find('east')
			output3 = next.find('north')
			output4 = next.find('west')
				
			if output1 == 0:
				return 'End_One'
			elif (output2 == 0) or (output4 == 0):
				print "You cannot go that way."
				return 'house'
			elif output3 == 0:
				return 'Pond_Crossroad'
			else: 
				print "Pick a direction or do something."
				return 'house'

#End game. Accessed from house (North).	
	def End_One(self):
		if (inventory.count('platinum')==0) or (inventory.count('fruit')==0) or (inventory.count('house')==0) or (inventory.count('bottle')==0) or (inventory.count('shell')==0) or (inventory.count('flower')==0):
			print "You have not completed your quest. Please keep trying."
			x = points.count(1)
			print "You have %i point(s) out of 6."%x
			return 'Beach_One'
		else:
			print "You have reached the end. Congratulations."
			exit(0)

#starts the game going		
a_game = Game("Beach_One")
a_game.play()
