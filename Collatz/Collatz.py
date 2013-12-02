"""Collatz Conjecture 
Start with a number n > 1. 
Find the number of steps it takes to reach one using the following process: 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
As an example, 27 has 111 steps
"""

#get input from user
n = raw_input('Enter a number:')

#change input into int so we can do maths on it
n = int(n)

#set counter
i = 0

#if they enter 0, we can't do anything useful so print an error
if n > 0:
	#loop til n = 1
	while n != 1:
		if n % 2 == 0:
			#if the modulo is 0 then it's an even number, so divide by 2 and increase counter
			n = n / 2
			i = i + 1
		else:
			#if it's not 0 it's odd, so do the other stuff and increase counter
			n = n * 3 + 1
			i = i + 1
	#when n no longer != 1, we have an answer, so print the count
	print "count: " + str(i)
else:
	print "Please enter a number greater than 0"