"""Monty Hall Problem - 1 turn"""

from random import choice

win_stick = 0
win_switch = 0

doors = ["A", "B", "C"]
car = choice(doors)
print "car = %s" %car
user = raw_input("Choose a door, A, B or C:")
print "user = %s" %user

host = ["A", "B", "C"]
host.remove(car)
if car != user:
	host.remove(user)
host = choice(host)
print "host = %s" %host

switch = ["A", "B", "C"]
switch.remove(host)
switch.remove(user)
switch = ''.join(map(str, switch))
print "switch = %s" %switch


print ("You picked door %s, the host has opened door %s to reveal a goat. Do you want to switch to door %s?") %(user, host, switch)
choice = raw_input("Y or N")

if choice == "N":
	print "You have chosen to stick with door %s" %user
	if user == car:
		print "Good choice, you've won a car!"
		win_stick +=1 
	else:
		print "Bad luck, you win a smelly old goat"
else: 
	print  "You have chosen to switch to door %s" %switch
	if switch == car:
		print "Good choice, you've won a car!"
		win_switch +=1
	else:
		print "Bad luck, you win a smelly old goat"
	
print win_stick
print win_switch

