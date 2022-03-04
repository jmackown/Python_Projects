"""hangman"""

import random

wordlist = ["aardvark","alligator","alpaca","anteater","antelope","ape","armadillo","ass","baboon","badger","basilisk","bat","bear","beaver","bison","boar","budgerigar","buffalo","bull","bunny","camel","canary","capybara","cat","chameleon","cheetah","chimpanzee","chinchilla","chipmunk","cougar","cow","coyote","crocodile","crow","deer","dingo","doe","dog","donkey","dormouse","elephant","elk","ermine","ewe","fawn","ferret","finch","fish","fox","frog","gazelle","monster","giraffe","gnu","goat","gopher","gorilla","hamster","hare","hedgehog","hippopotamus","hog","horse","hyena","iguana","jackal","jaguar","kangaroo","kitten","koala","lamb","lemur","","lion","lizard","llama","lovebird","lynx","mare","marmoset","mole","mongoose","monkey","moose","mouse","mule","newt","ocelot","okapi","","otter","ox","panda","panther","parakeet","parrot","pig","platypus","pony","porcupine","porpoise","puma","puppy","quagga","rabbit","raccoon","ram","rat","reindeer","reptile","rhinoceros","salamander","seal","sheep","shrew","skunk","sloth","snake","squirrel","stallion","steer","tiger","toad","turtle","walrus","warthog","weasel","whale","wolf","wolverine","wombat"]

word = random.choice(wordlist)
word = list(word)
count = len(word)
guess = 0
answer = []

#initial setup of blank answer
i = 0
while i < count:
	answer.extend(["_"])
	i = i + 1

print ' '.join(map(str, answer))

#function to replace correct guess with letters
def have_go(guess):
	i = 0
	while i < count:
		
		if word[i] == guess:
			answer[i] = guess
		i += 1

	return ' '.join(map(str, answer))


turn = 0
	
while (answer.count("_") > 0 and turn < 15):

	go = raw_input("guess a letter, %d goes remaining: " %(15-turn))
	go = str.lower(go)
	turn = turn + 1
	print have_go(go)
	
if (answer.count("_") > 0 and turn == 15):
	print "Too slow, now you'll never know what the word was, ha."
else:	
	answer = ''.join(map(str, answer))
	turn = str(turn)
	print "Hurrah! The you guessed %s correctly in %s goes!" %(answer, turn)
	
	