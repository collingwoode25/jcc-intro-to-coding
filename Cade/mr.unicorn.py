print("you are a unicorn trying to ride down the rainbow!")
print("press a if you want to fight the ogre on one side")
print("press b if you want to explore the other side")
answer1 = raw_input("press a or b: ")
if answer1 == "a":
	print("you lose!")
	print("press a if you want to explore the other side")
	answer2 = raw_input("press a: ")
	if answer2 == "a":
		print("you find a ladder")
		print("press a if you want to ride down the rainbow")
		answer3 = raw_input("press a: ")
		if answer3 == "a":
			print("you win!!!")
elif answer1 == "b":
	print("you find that this side is unguarded")
	print("you find a ladder")
	print("press a if you want to ride down the rainbow")
	answer3 = raw_input("press a: ")
	if answer3 == "a":
		print("you win!!!")
		
		
	
