import os
os.system("clear")


# Using Rectangular box method from saurabh sir youtube video

for i in range(1,5):
	for j in range(1,5):
		if(j <= i):
			print("*",end="")
		else:
			print(" ",end="")

	print()

print("\n---------------------------------------------\n")

# Using online method with FUNCTIONS

def pat(n):
	for i in range(0,n):
		for j in range(0,i+1):
			print("*",end="")
		print("\r")
n = 5
pat(n)
