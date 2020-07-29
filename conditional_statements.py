import os
os.system("clear")

################################

# Conditional Statement
# if/else/elif

################################

num = 10

if(num > 10):
	print("Your number is greater than 10")

elif(num == 10):
	print("Your number is 10")

else:
	print("Your number is less than 10")

num = "zee" 
if(num == "zee" ):
	print("Same")
else:
	print("Different")

################################

# Multiple conditions

################################
num = 200

if(num > 10) and (num > 100):
	print("Your number is greater than 10 and 100")

num = 11
if(num > 10) or (num > 100):
	print("Your number is greater than 10 and 100")
else:
	print("Your number lies between 0 - 10")