#!/usr/bin/python3
#program for a 3*3 tic-tac-toe
def entry(player):
	count=0
	j=0
	lst=[0,0,0,0,0,0,0,0,0]                                #function to add values to the lst
	for j in range(0,10):	
		posi=input("please enter the position: ")
		num=input("please enter the number: ")
		if int(posi)==(1 or 3 or 5 or 7 or 9):
			lst[int(posi)-1] = int(num)
		else:
			lst[int(posi) - 1] = int(num)	
		for i in range(0,9):
			if(i%3==0):
				print("\n")
			print(lst[i],end=" ")
			i=i+1
			
		if player in "player 1's chance":
			player="Player 1's chace"
			print(player)
		else:
			player="Player 2's chance"
			print(player)

def winner():
	if (lst[1]+lst [2]+lst[3]==15):
		print ('{0} are the winner' .format(player))
		return True

	if (lst[4]+lst [5]+lst[6]==15):
		print ('{0} are the winner' .format(player))
		return True

	if (lst[2]+lst [5]+lst[8]==15):
		print ('{0} are the winner' .format(player))
		return True

	if (lst[3]+lst [7]+lst[5]==15):
		print ('{0} are the winner' .format(player))
		return True

	if (lst[1]+lst [5]+lst[9]==15):
		print ('{0} are the winner' .format(player))
		return True
 
	if (lst[7]+lst [8]+lst[9]==15):
		print ('{0} are the winner' .format(player))
		return True

	else: return False

print("Welcome to the Tic-Tac-Toe game")                                   #taking choice from the user
choice=input("Please enter any of the even and odd choices: ")
if choice=="odd":
	print("Player 1's choice")
elif choice=="even":
	print("Players 2's choice")
else:
	print("Invalid choice")
	exit(0)
player="Player 1's chance"
print(player)
entry(player)
while (True):
	if winner(): break














