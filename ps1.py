#!/usr/bin/python3
#program for bit stuffing and parity check

def check(string):                   #function to check for a valid string
	p=set(string)
	s={'0','1'}
	if s==p or p=={'0'} or p=={'1'}:
		print("It is a valid string")
	else:
		print("please enter again a valid string")	

if __name__ == "__main__" : 
	string=input("please enter a valid binary string\n")
	check(string)

