#!/usr/bin/python3
#program for a 3*3 tic-tac-toe
def chance():
	posi=int(input("Please enter the position:  \n"))        #user defined function to take position and number
	num=int(input("Please enter the number:  "))
	if posi>0 and posi<10 and num>0 and num<10:
		print("Valid")
	else:
		print("Invalid enteries")	


print("Welcome to the Tic-Tac-Toe game")
choice=input("Please enter any of the even and odd choices: ")
if choice=="odd":
	print("Player 1's choice")
	player1="1,3,5,7,9"
elif choice=="even":
	print("Players 2's choice")
	player2="2,4,6,8"
else:
	print("Invalid choice")
	

for i in range(1,10):
	chance()
	i+=2

