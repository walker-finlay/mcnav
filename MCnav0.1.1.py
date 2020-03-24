from math import atan2, degrees

print "MC Navigator\n"

while True:
    inp = raw_input("<from x> <from z> <to x> <to z>: ").split()

    if inp[0] == "quit" or inp[0] == "q": quit()

    fromX = int(inp[0])
    fromZ = int(inp[1])
    toX = int(inp[2])
    toZ = int(inp[3])

    opposite = toZ - fromZ
    adjacent = toX - fromX

    theta = degrees(atan2(opposite, adjacent))

    if toX < fromX and toZ < fromZ:
        print "Take heading ( %s )\n" % round(theta + 270, 1)
    else :
        print "Take heading ( %s )\n" % round(theta - 90, 1)