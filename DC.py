import random, time
import os
from termcolor import colored, cprint

#For clearing the console
os.system('cls' if os.name == 'nt' else 'clear')

#Important lists/variables here
inventory = [] #inventory starts as an empty list, so we can append things to it as we go
A = ["A", "a"]
B = ["B", "b"]
C = ["C", "c"]
I = ["I", "i"]
yes = ["y", "Y", "yes", "YES", "Yes"]
no = ["N", "n", "no", "NO", "No"]
riddles = ["fire", "water"]
guess = 5
# This ensures the goblins are alive to start, so we can kill them later
GOB_E = True
GOB_N = True

#INTRO/TITLE
 ################################################
os.system('cls' if os.name == 'nt' else 'clear')

print('What is your name?')
name = input('>>> ')
print('Greetings ' + name)
time.sleep(1)
print('.........')
print(colored('Prepare yourself', 'red'))
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
 ################################################

#STORY BEGINS HERE
#Every room is a function, where choice is a variable determined by input. Then that input is compared to the variables of either A, B, C.
#And I then use IF, ELSE statements to determine which event plays out or which function (room) the player goes to next
 ################################################

print('"Wake up ' + name + '! You must wake up!"')
time.sleep(1)
print('You hear a strange and disruptive voice bring you to your feet.')
print('You eagerly look around but you cannot see anyone.')
print("In fact you can't see anything.")
time.sleep(3)
print('You take notice of your surroundings: You are in a very dark murky room, sitting on what feels like cobblestone.')
print("You can't seem to remember anything besides your name, you have no idea where you are or how you got here.")

#OPENING ROOM ################################################
def first_room():
	print("You're engulfed in darkness, what do you do?")
	print("A: Stay where you are and hope someone comes")
	print("B: Venture out into the unknown, hoping to find an exit")
	choice = input(">>> ")
	if choice in A:
		print('You wait for what feels like an eternity')
		print('Slowly your mind begins to crumble away in the despair of the emptyness.')
		print('You are staring directly into the void')
		time.sleep(2)
		print('................')
		time.sleep(2)
		print('it stares back.')
		time.sleep(2)
		print('................')
		time.sleep(1)
		print('You can feel your grasp on reality slowly slipping.')
		print('You curl up into a ball on the cold dank floor, softly sobbing yourself to sleep.')
		time.sleep(5)
		GAME_OVER()
	if choice in B:
		print('While groping in the darkness, you feel a gap along the wall just big enough for you to slide through.')
		print('You decide to try going through it.')
		time.sleep(1)
		print("It's a little too close for comfort, but you do fit between the gap.")
		print('As you squeeze yourself along, you notice a dim light on the other side.')
		print('Excited you quicken your pace, forcing yourself through the ever tightening path.')
		time.sleep(2)
		print('Finally you emerge to the other side.')
		print('The light is too bright at first, but after a few moments your eyes adjust.')
		print('.................')
		time.sleep(5)
		second_room()
	else:
		print('INVALID INPUT')
		first_room()

#SECOND ROOM ################################################
def second_room():
	time.sleep(2)
	print('THE ROOM OF CHOICE')
	print('You are standing in what appears to be another stone room, roughly square in shape with 2 doors: one on the north end and another on the east.')
	print('The room is lit by several torches hanging on the wall.')
	if 'Torch' in inventory:
		print('Thankfully yours is still working great.')
	else:
		inventory.append('Torch')
		print('You pick up a torch and place it in your inventory.')
		print('CHECK YOUR INVENTORY BY TYPING "I" WHEN PROMPTED FOR INPUT')

	print("You have to figure out how you got here, but more importantly, how to escape.")
	print("What will you do?")
	print('A: Go through the north door')
	print('B: Go through the east door')
	print('C: Go Back where you entered from')
	choice = input(">>> ")
	if choice in A:
		print("You decide to enter through the north door.")
		if GOB_N == True:
			north_room()
		else:
			no_back()
	if choice in B:
		print("You decide to enter through the east door.")
		if GOB_E == True:
			east_room()
		else:
			no_back()
	if choice in C:
		print('You briefly consider going back through the gap.')
		print('But then you realize how truly idiotic that would be.')
		print('Only some seriously stupid doofus would even consider that.')
		time.sleep(1)
		print('Obviously the only way out of here is by going forward, and not waiting in a dark empty room.')
		print('You decide to look around the room again.')
		time.sleep(6)
		print('................')
		second_room()
	if choice in I:
		print('You have these items on you: ' + str(inventory))
		time.sleep(2)
		second_room()
	else:
		print('INVALID INPUT')
		time.sleep(1)
		second_room()
#NORTH ROOM ################################################
def north_room():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("You enter a small room with a high ceiling.")
	print("You immediately notice the crushed hay beaneth your feet, sprawled across the floor.")
	print("The walls are decorated with bright red banners dimly lit by more wall torches.")
	print("At one end of the room, you notice a locked chest.")
	time.sleep(2)
	print("You try, but are unable to open it.")
	time.sleep(2)
	print("That's when you notice a goblin sleeping on the other end of the room.")
	print("There is a key wrapped around its neck.")
	print("What do you do?")
	print("A: Try and take the key")
	print("B: Go Back")
	choice = input(">>> ")
	if choice in A:
		goblinN()
	if choice in B:
		print("You decide to head back to the main room.")
		second_room()
	if choice in I:
		print('You have these items on you: ' + str(inventory))
		time.sleep(2)
		north_room()
	else:
		print('INVALID INPUT')
		time.sleep(1)
		north_room()
#EAST ROOM ################################################
def east_room():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("You enter a small room with a high ceiling.")
	print("You immediately notice the muddy floor and egregious smell.")
	print("The walls are decorated with dull yellow banners dimly lit by more wall torches.")
	print("At one end of the room, you notice a locked chest.")
	time.sleep(2)
	print("You try, but are unable to open it.")
	time.sleep(2)
	print("That's when you notice a goblin sleeping on the other end of the room.")
	print("There is a key wrapped around its neck.")
	print("What do you do?")
	print("A: Try and take the key")
	print("B: Go Back")
	choice = input(">>> ")
	if choice in A:
		goblinE()
	if choice in B:
		print("You decide to head back to the main room.")
		second_room()
	if choice in I:
		print('You have these items on you: ' + str(inventory))
		time.sleep(2)
		east_room()
	else:
		print('INVALID INPUT')
		time.sleep(1)
		east_room()

#GOBLINS & CHESTS ################################################
def goblinN():
	global inventory
	global GOB_N
	print('While trying to steal the key, you inevitably wake the beast.')
	print("He awakes in a furious rage, he's ready to fight!")
	print("What will you do?")
	print("A: FIGHT BACK! (YOUR WEAPONS DETERMINE YOUR CHANCE OF WINNING)")
	print("B: RUN!")
	choice = input(">>> ")
	if choice in A:
		if 'LongSword' in inventory:
			print("You strike the goblin down in one swift blow!")
			print("Well that was suprisingly easy.")
			print("You take the key and open the chest.")
			time.sleep(3)
			print("Inside the chest you find a rusty dagger.")
			inventory.append('dagger')
			print("This...might be useful?")
			print("Then, something catches your eye.")
			GOB_N = False
			time.sleep(4)
			no_back()
		else:
			roll = random.randint(1, 3)
			if roll == 3:
				print("You move quickly.")
				print("The goblin is a towering wall, but he moves slowly.")
				print("You are able to land some deadly blows using nearby rocks.")
				print("You beat the beast!")
				print("You take the key and open the chest.")
				time.sleep(3)
				print("Inside the chest you find a rusty dagger.")
				inventory.append('dagger')
				print("This...might be useful?")
				print("Then, something catches your eye.")
				GOB_N = False
				time.sleep(4)
				no_back()
			else:
				print("You move quickly.")
				print("The goblin is a towering wall, but he moves slowly.")
				print("Unfortunately you are unable to land any real hits.")
				print("Within seconds the goblin has grabbed you by the throat; mercilessly he smashes your head against the floor repeatedly until you are unrecognizable.")
				time.sleep(2)
				print("At least the death was quick....")
				time.sleep(10)
				GAME_OVER()
	if choice in B:
		print("You try to run, but of course it's futile.")
		print("Within seconds the goblin has grabbed you by the throat; mercilessly he smashes your head against the floor repeatedly until you are unrecognizable.")
		time.sleep(2)
		print("At least the death was quick....")
		time.sleep(10)
		GAME_OVER()
	if choice in I:
		print('You have these items on you: ' + str(inventory))
		time.sleep(2)
		goblinN()
	else:
		print('INVALID INPUT')
		time.sleep(1)
		goblinN()

def goblinE():
	global inventory
	print('While trying to steal the key, you inevitably wake the beast.')
	print("He awakes in a furious rage, he's ready to fight!")
	print("What will you do?")
	print("A: FIGHT BACK! (YOUR WEAPONS DETERMINE YOUR CHANCE OF WINNING)")
	print("B: RUN!")
	choice = input(">>> ")
	if choice in A:
		if 'dagger' in inventory:
			print("You estimate a roughly 50/50 chance of winning.")
			print("You give it all you got!")
			roll = random.randint(1, 2)
			if roll == 2:
				print("It takes a while, but you strike the goblin down in a few decisive blows!")
				print("You slay the beast!")
				print("You take the key and open the chest.")
				time.sleep(3)
				print("Inside the chest you find a Long Sword")
				inventory.append('LongSword')
				print("This seems really useful!")
				print("Then, something catches your eye.")
				GOB_E = False
				time.sleep(4)
				no_back()
			else:
				print("You move quickly.")
				print("The goblin is a towering wall, but he moves slowly.")
				print("Unfortunately you are unable to land any real hits.")
				print("Within seconds the goblin has grabbed you by the throat; mercilessly he smashes your head against the floor repeatedly until you are unrecognizable.")
				time.sleep(2)
				print("At least the death was quick....")
				time.sleep(10)
				GAME_OVER()
		else:
			print("The chance of winning isn't great, maybe 1/3.")
			print("But you desperately try regardless.")
			roll = random.randint(1, 3)
			if roll == 3:
				print("You move quickly.")
				print("The goblin is a towering wall, but he moves slowly.")
				print("You are able to land some deadly blows using nearby rocks.")
				print("You beat the beast!")
				print("You take the key and open the chest.")
				time.sleep(3)
				print("Inside the chest you find a Long Sword")
				inventory.append('LongSword')
				print("This seems really useful!")
				print("Then, something catches your eye.")
				GOB_E = False
				time.sleep(4)
				no_back()
			else:
				print("You move quickly.")
				print("The goblin is a towering wall, but he moves slowly.")
				print("Unfortunately you are unable to land any real hits.")
				print("Within seconds the goblin has grabbed you by the throat; mercilessly he smashes your head against the floor repeatedly until you are unrecognizable.")
				time.sleep(2)
				print("At least the death was quick....")
				time.sleep(10)
				GAME_OVER()
	if choice in B:
		print("You try to run, but of course it's futile.")
		print("Within seconds the goblin has grabbed you by the throat; mercilessly he smashes your head against the floor repeatedly until you are unrecognizable.")
		time.sleep(2)
		print("At least the death was quick....")
		time.sleep(10)
		GAME_OVER()
	if choice in I:
		print('You have these items on you: ' + str(inventory))
		time.sleep(2)
		goblinE()
	else:
		print('INVALID INPUT')
		time.sleep(1)
		goblinE()

#NO GOING BACK ################################################
def no_back():
	print("Beneath the goblins resting place is a small wooden trapdoor.")
	print("If you go down it, it doesn't seem like you'll be able to come back.")
	print("Will you go down? Or return to the other room?")
	print("NOTE THIS DECISION IS IRREVERSIBLE")
	print("A: Go down")
	print("B: Go back")
	choice = input(">>> ")
	if choice in A:
		print("You decide to go down the trap door.")
		time.sleep(4)
		riddle_room()
	if choice in B:
		print("You decide to go back.")
		time.sleep(4)
		second_room()
	if choice in I:
		print('You have these items on you: ' + str(inventory))
		time.sleep(2)
		no_back()
	else:
		print('INVALID INPUT')
		time.sleep(1)
		no_back()
#RIDDLE ROOM ################################################
def riddle_room():
	os.system('cls' if os.name == 'nt' else 'clear')
	global guess
	if guess == 0:
		bad_ending()
	else:
		print("RIDDLES")
		print("You enter a large empty room.")
		print("The only notable feature is a sizable elaborately decorated door on the far end.")
		print("Of course, it's locked.")
		print("Upon closer inspection, you notice something has been carved into it.")
		print("It appears to be a riddle!")
		time.sleep(2)
		print("You begin to read it aloud:")
		print(">A Wonderful warrior exists")
		print(">Decorated in colours upon rooms where monsters sleep")
		print(">He is fierce, but he can be tamed")
		print(">He meekly serves both man and woman alike")
		print(">As long as you feed him well")
		print(">But if you let him grow proud")
		print(">This ungrateful fiend will soon turn against you")
		time.sleep(2)
		print("You wonder what it could be.")
		print("If you say the correct answer out loud, the door may unlock")
		print(colored("(Answer will only be accepted as a singular noun, in lower-case: You have a limited amount of guesses)", 'red'))
		choice = input(">>> ")
		if choice in riddles[0]:
			print("With a slow creaking screech the doors begin to open.")
			print("It seems you got it right!")
			print('Press any key to proceed, this is your final destination')
			proceed = input('>>> ')
			if proceed in yes:
				print("You proceed to the next room, inching closer to the final destination")
				dragon()
			else:
				print("You proceed to the next room, inching closer to the final destination")
				dragon()
		if choice in I:
			print('You have these items on you: ' + str(inventory))
			time.sleep(2)
			riddle_room()
		else:
			print('INVALID INPUT')
			time.sleep(1)
			guess = guess - 1
			print("You have " + str(guess) + " Guesses left")
			riddle_room()
#DRAGON ################################################
def dragon():
	os.system('cls' if os.name == 'nt' else 'clear')
	global name
	os.system('cls' if os.name == 'nt' else 'clear')
	print('"Welcome "' + name + '"! I have been waiting for you"')
	time.sleep(2)
	print("You recognize that voice, it's the same voice you heard when you first woke up.")
	print("You scan the room for where it could be coming from.")
	print("Unfortunately the room is pitch-black, ")
	time.sleep(5)
	print('In frustration you shout back: "Why did you bring me here! What do you want from me?"')
	print('................')
	time.sleep(1)
	print('................')
	time.sleep(1)
	print('With a sudden blinding flash of light, your surroundings suddenly become perceivable')
	time.sleep(0.5)
	print('You find youreself in a highly decorated crypt, with ornate arches and gorgeous gothic stylings.')
	print('Towering in the center of this massive room, is an old withered dragon')
	print('"Hello traveller, you have been called here as a test."')
	print('"I have been tasked with guarding a precious treasure, waiting for the moment for a noble warrior of worth to receive it."')
	print('"Fate has brought you here, because it seems to believe you are worthy."')
	time.sleep(2)
	print('"Now it is time to test your worth!"')
	print('What will you do?')
	print('A: Defeat the Dragon to prove your worth!')
	print('B: Try to avoid a fight')
	print('C: Refuse to participate')
	choice = input('>>> ')
	if choice in A:
		if 'LongSword' in inventory:
			print("With your mighty sword, you have the decent chance of winning. But the odds still aren't great.")
			print("But you give it all you got!")
			time.sleep(3)
			roll = random.randint(1, 3)
			if roll == 3:
				print("It takes a while, but you strike some solid hits")
				print("You strike him down!")
				print('The dragon sweeps you aside with his mighty tail.')
				print('"You have proven your valor mighty hero. I will grant you what you desire."')
				time.sleep(5)
				good_ending()
			else:
				print("You move quickly.")
				print("The dragon has you cornered.")
				print("Unfortunately you are unable to land any real hits.")
				print("With an immense heat, a scorching flame is emitted from the dragons mouth.")
				print("With no escape you are caught in the fierce blaze.")
				time.sleep(2)
				print("You are now but a pile of burnt bones and ash.")
				time.sleep(10)
				GAME_OVER()
		if 'dagger' in inventory:
			print("With just your old dagger, your odds are slim.")
			print("But nevertheless, you can't give up!")
			time.sleep(3)
			roll = random.randint(1, 6)
			if roll == 6:
				print("It takes a while, but you strike some solid hits")
				print("You strike him down!")
				print('The dragon sweeps you aside with his mighty tail.')
				print('"You have proven your valor mighty hero. I will grant you what you desire."')
				time.sleep(5)
				good_ending()
			else:
				print("You move quickly.")
				print("The dragon has you cornered.")
				print("Unfortunately you are unable to land any real hits.")
				print("With an immense heat, a scorching flame is emitted from the dragons mouth.")
				print("With no escape you are caught in the fierce blaze.")
				time.sleep(2)
				print("You are now but a pile of burnt bones and ash.")
				time.sleep(10)
				GAME_OVER()
		else:
			dragon()
	if choice in B:
		print("So, you'd rather not fight? MUHAHAH! Perhaps that is the wise choice considering our obvious difference in strength.")
		print("There is one other way to prove your worth.")
		print("If you can decipher this next riddle, I will consider you worthy.")
		time.sleep(5)
		final_riddle()
	if choice in C:
		print('If you do not want the treasure, I suppose I cannot force you to desire it.')
		print(colored("Unfortunately however, now that you have seen my crypt. I cannot let you leave alive", 'red'))
		time.sleep(5)
		bad_ending2()
	if choice in I:
		print('You have these items on you: ' + str(inventory))
		time.sleep(2)
		dragon()
	else:
		print('INVALID INPUT')
		time.sleep(1)
		dragon()
#FINAL RIDDLE ################################################
def final_riddle():
	global guess
	if guess == 0:
		bad_ending()
	else:
		print("The riddle is as follows:")
		print(">There is a solitary creature on this earth")
		print(">Simple and humble in appearance")
		print(">She is rather timid and gentle, but can be quite wild and wrathful too")
		print(">She is beloved by the propserous and poor alike")
		print(">She is far older than any man")
		print(">Her beauty is measured in her utility")
		print(">Her worth in what she provides")
		print(">She is beloved by all, but feared in equal measure")
		time.sleep(3)
		print('"So, what is the answer?"')
		print(colored("(Answer will only be accepted as a singular noun, in lower-case: You have a limited amount of guesses)", 'red'))
		choice = input(">>> ")
		if choice in riddles[1]:
			print('"I see, your wisdom is beyond measure."')
			good_ending()
		else:
			print('INVALID INPUT')
			time.sleep(1)
			guess = guess - 1
			print("You have " + str(guess) + " Guesses left")
			final_riddle()

#################################################
#ENDINGS ################################################
#################################################

#GAME OVER FUNCTION
 ################################################
def GAME_OVER():
	os.system('cls' if os.name == 'nt' else 'clear')
	global inventory
	inventory.clear()
	print(colored('GAME OVER','red'))
	print('WANT TO RETURN TO THE BEGINNING?')
	choice = input(">>> ")
	if choice in yes:
		os.system('cls' if os.name == 'nt' else 'clear')
		inventory = []
		first_room()
	else:
		print('EXIT THE WINDOW TO LEAVE OR PRESS CTRL+C TO STOP TERMINAL PROCESS')
		GAME_OVER()
#GOOD ENDING ################################################
def good_ending():
	os.system('cls' if os.name == 'nt' else 'clear')

	print('"You have passed the test."')
	print('"The ever-spinning wheel of fate has favoured you this day."')
	print('"TaKe this treasure, and sit upon your throne."')
	print("The dragon moves to the side to reveal a gold throne behind him.")
	print("He gestures you on-ward, encouraging you towards it.")
	time.sleep(1)
	print("You have proven yourself worthy")
	time.sleep(8)
	os.system('cls' if os.name == 'nt' else 'clear')
	print(colored("CONGRATULATIONS!", 'green'))
	time.sleep(2)
	print(colored("YOU WIN!", 'green'))
	time.sleep(1)
	GAME_OVER()

#BAD ENDING ################################################
def bad_ending():
	global name
	os.system('cls' if os.name == 'nt' else 'clear')
	print("You feel a soft rumbling from the ground.")
	print('"You have failed me ' + name + ', You are not worthy after all."')
	print("The cobblestone beneath you begins to give-way...")
	time.sleep(2)
	print('..................')
	time.sleep(2)
	print(colored("THE EARTH IS MOVING FROM BENEATH YOU!!", 'red'))
	print('..................')
	time.sleep(2)
	print('..................')
	print("Brick by brick, the floor begins to fall into a bottomless void")
	print(colored('"AHHHHHHHHHHHHH!!!!!"', 'red'))
	print('Your screams of course are futile, your fate is sealed.')
	print('Your doom has been cast before you, and there is no turning back as you are consumed into a pit of unimaginable depth.')
	time.sleep(10)
	GAME_OVER()

#BAD ENDING ################################################
def bad_ending2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The dragons scorching flames burn you alive on the spot.")
    print("You have died")
    time.sleep(2)
    GAME_OVER()

#This line is required to start the story, has to be set after all the functions in the story are defined
first_room()
