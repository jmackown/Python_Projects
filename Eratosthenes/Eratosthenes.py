"""Sieve of Eratosthenes
An easy way to find all low-ish primes (below 10 million)

	Take a list of consecutive numbers starting at 2 (0 and 1 are special cases)
	Remove all multiples of 2
	Remove all multiples of 3
	Remove all multiples of 4
	Etc etc til the end of list
	What remains are all the primes"""




	
def find_prime(n):
	"""
	c is the start of the range, use that and end to fill in the list with all our numbers
	set the divisor to be the first element in the list
	divide every item in the list by the divisor
	if the item > divisor (has to be otherwise the modulo gives a +ve no, eg 2 % 10 = 2 because 10 goes into 2 0 times with a remainder of 2) and the modulo is 0 (ie the item is a multipe of the divisor), then remove from the list
	specials is just a cheaty way to add in 0 and 1, though technically these are not primes
	"""
	
	list = []
	c = 2
	i = 0
	
	while c < n + 1:
		list.extend([c])
		c = c + 1


	for s in list:
		divisor = list[i]
		for s in list:
			if (s > divisor and s % divisor == 0):
				list.remove(s)
		
		i = i + 1

	specials = [0,1]
	return specials + list

decide = raw_input("Would you like to\na: list primes\nb: check if your number is prime?\n")


if decide == "a":	
	
	#get user input for end of range
	end = raw_input('Find primes up to:')
	if str.isdigit(end):
		end = int(end)
				
		#some funky stuff to make the list print out as a string without the square brackets
		print ', '.join(map(str, find_prime(end)))
	else:
		print "Only WHOLE numbers can be primes"

elif decide == "b":

	check = raw_input("Is my number prime? ")
	if str.isdigit(check):
		check = int(check)

		if check in find_prime(check):
			print "Yes, %s is prime" %check
		else:
			print "No, %s is not prime" %check
			
	else:
		print "Only WHOLE numbers can be primes"

else:
	print "That is not a valid option"



