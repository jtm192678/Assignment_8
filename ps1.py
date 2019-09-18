#!/usr/bin/python3
#program for bit stuffing and parity check

def check(string):                   #function to check for a valid string
	p=set(string) 
	s={'0','1'}
	if s==p or p=={'0'} or p=={'1'}:
		print("It is a valid string")
	else:
		print("please enter again a valid binary string")	

if __name__ == "__main__" : 
	string=input("please enter a valid binary string\n")
	check(string)                     #calling check function
substring='1'
count=string.count(substring)
#print("count is:",count)
if count%2==0:                                         #to add parity bit at the end of the binary data
	string=string+'1'
	print("The parity corrected data is:  ",string)      #print parity added data
else:
	string=string+'0'
	print("The parity corrected data is:  ",string)
print("\n")
string2=string.replace("010","0100")                      #replacing the '010' substring by '0100'
print("The transmitting data is:   ",string2)
