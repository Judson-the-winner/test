#!/bin/python3

print("_" * 50) 
('\n')
print(" " * 50)
print("Awesome amazing game by Judson.")
('\n') 
print("_" * 50) 
('\n')


import time


print(" " * 50) 


Piece = input("What is your favorite chess piece?: ")
('\n')

print(" " * 50)

if Piece == "the rook":
	print("THE ROOOOK")
else :
	print("loser, you should have picked the rook") 
inventory = [ ]
print("_" * 50) 
print(" " * 50) 
print(" " * 50) 
space = " " * 50
while True: 
	try: 
		answer1 = input("You find yourself on a path in the forest.(please put your answer in the form of the '  ' path.) Do you choose the left path forward or the right path forward?: ")  
		if answer1 == "the right path":
			print("You continue down the right path in the forest.")
			print(" " * 50)
			print("You then get mawled by a bear") 
			continue
		elif answer1.lower() == "the left path":
			time.sleep(1)
			print("You continue down the left path in the forest.")
			print(" " * 50) 
			time.sleep(3)
			print("You see a crow sitting on a branch, cawing loudly while you hear the crunch of leaves under your feet.")
			print(" " * 50)
			time.sleep(2)
			break
		else:
			print("Invalid answer please try again and remove any unecessary spaces.")
			print(" " * 50) 
			print(" " * 50) 
			print("_" * 50) 
			time.sleep(5)
			continue
	except:  
		quit()
while True:
	try:
		answer2 = input("Eventually you find a skull on the path in front of you. What do you do?:") 
		if answer2 == "I pick it up" :
			print("As you reach for the skull, it awakens and eats you.")
			print(" " * 50) 
			print(" " * 50) 
			print("The end") 
			print(" " * 50)
			continue
		elif answer2 == "I grab it" :
			print("As you reach for the skull, it awakens and eats you.")
			print(" " * 50) 
			print(" " * 50) 
			print("The end") 
			print(" " * 50)
			continue	
		elif answer2 == "I crush it" :
			print("You bring up your foot and crush it to smitheerens.") 		
			print("You gain a BONE SHARD!")
			inventory.append ("BONE SHARD")
			print("inventory: ")
			print(inventory)
			break			
		elif answer2 == "I continue down the path" : 
			print(" You continue through the forest.") 
			print(" " * 50) 
			time.sleep(3)
			break
		else : print(" invalid answer please try again") 
		continue
	except: 
		quit()








				
while True: 
	try: 
		print(" " * 50)  
		time.sleep(3) 
		print("_" * 50) 
		time.sleep(3) 
		print("You have been walking for hours at this point and you find a cabin in the woods.")
		print(" " * 50) 
		time.sleep(2) 
		answer3 = input("Do you choose to approach the cabin, or continue to wander through the woods?: ") 
		if answer3 == "I approach" or "I approach the cabin" :
			time.sleep(3)
			print(" " * 50)
			time.sleep(2)
			print("As you reach the door, you see a sign hanging above the door saying: ") 
			time.sleep(3)
			print('"To enter this place you must present the the owner."') 
			if "BONE SHARD" in inventory:	
				print("You reveal the BONE SHARD to the door. It accepts this and opens for you.")
				break
			else: print(" You do not have the owner with you so you turn away from the cabin.")

		elif answer3.lower() == "i continue to wander" :
			print("You decide to continue on, ignoring the cabin.") 
			print(" " * 50) 
			time.sleep(5)
			print("You die of thirst out in the woods.") 
			time.sleep(5)
			print(" " * 50) 
			print("Alone.") 
			quit()

		else: print("Please put in a valid answer.")
		continue
	except: 
		quit()
while True:
	try: 
		print("_" * 50) 
		print(" " * 50) 
		time.sleep(3) 
		print("You slowly step into the cabin, and it is very dark inside.")
		print(" " * 50) 
		time.sleep(3)
		print("You could search around for a lightswitch or some other form of lighting, or you could continue on.")
		time.sleep(2)
		print(" " * 50) 
		answer4 = input("What do you choose to do?: ")
		if answer4 == "Leave the cabin":
			time.sleep(10) 
			print(" " * 50)
			print("Okay") 
			time.sleep(3)
			quit() 
		elif answer4 == "I continue through the darkness" or "I continue on":
			print(" " * 50) 
			time.sleep(1)
			print("You continue into the cabin.") 
			print(" " * 50)
			time.sleep(2) 
			print("You step into the darkness and feel something squish under your foot.")
			time.sleep(2) 
			print(" " * 50) 
			print("You peel it off and put it in your backpack.") 
			print("You gain a MYSTERIOUS GOO!")
			inventory.append ("MYSTERIOUS GOO")
			time.sleep(3)
			print("inventory: ")
			print(inventory)
			break
			

	except: 
		quit()









