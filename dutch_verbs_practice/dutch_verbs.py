#infinitive imperfectum_s imperfectum_p perfectum vertaling
print "Good day and welcome to the Dutch verb practice service."
print "This service will help you practice your Dutch verbs."
print "Note that 1 is the infinitive, 2 is the imperfectum_s, 3 is the imperfectum_p, 4 is the perfectum"
import random
verbs = [
	['vechten', 'vocht', 'vochten', 'gevochten', 'hebben', 'fight'],
	['trekken', 'trok', 'trokken', 'getrokken', 'zijn', 'take'],
	['sterven', 'stierf', 'stierven', 'gestorfen', 'zijn', 'die'],
	['varen', 'voer', 'voeren', 'gevaren', 'hebben', 'sail'],
	['vangen', 'ving', 'vingen', 'gevangen', 'hebben', 'catch']
	]

verb = random.choice(verbs)
x = random.randint(0,4)
print "What is the %i for"%x
print verb[5]
next = raw_input("> ")
if next == verb[x]:
	print "correct"
elif next != verb[x]:
	print "incorrect"
else:
	print "error"
