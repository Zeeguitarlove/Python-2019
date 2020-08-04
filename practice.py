import os
os.system("clear")

num_1 = 100.99
num_2 = 70.15

add = num_1 + num_2
print ("The sum of the given number is ", float(add))

x = int(input("Enter the Number "))
x = x % 2

if(x == 0):
	print("The number is not prime")
else:
	print("The number is Prime")

word = "zeeshaan"
for x in word:
	if (x == "a") or (x=="e") or (x =="i") or (x =="o") or (x == "u"):
		print(x + " is a vowel")
	else:
		print(x + " is not a vowel")
