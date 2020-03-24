from math import atan2, degrees

print "MC Navigator\n"
print "Enter destination coordinates(integers only)"
xDes = int(raw_input('destination x: '))
zDes = int(raw_input('destination z: '))

print "Enter origin coorinates(integers only)"
def recalc():
	xOri = int(raw_input('origin x: '))
	zOri = int(raw_input('origin z: '))
	
	opposite = zDes - zOri
	adjacent = xDes - xOri
	
	theta = degrees(atan2(opposite, adjacent))
	
	if xDes < xOri and zDes < zOri:
		print "From (%s, %s), take heading ( %s )\n" % (xOri, zOri, round((theta + 270), 1))
	else:
		print "From (%s, %s), take heading ( %s )\n" % (xOri, zOri, round((theta - 90), 1))

recalc()

print "Enter a command or type help for more information"

for num in range(0,50):
	input = raw_input('> ')
	if input == "quit":
		quit()
	elif input == "help":
		print """Press Enter to recalculate
Type new to enter a new destination
Type quit to quit"""
	elif input == "new":
		print "Enter new destination coordinates."
		xDes = int(raw_input('destination x: '))
		zDes = int(raw_input('destination z: '))
		recalc()
	elif input == "":
		recalc()
	else:
		print "Invalid command"