import os
os.system("clear")

####################################
# FizzBuzz
# divisible by 3 fizz
# divisible by 5 buzz
# divisibe by both fizzbuzz
####################################

num = 1
while (num <= 100):
	if(num % 3 ==0) and (num % 5 == 0):
		print("\nFizzBuzz on ",num)

	elif(num % 5 == 0):
		print("\nBuzz on ",num)

	elif(num % 3 == 0):
		print("\nFizz on ",num)

	else:
		print("\nNeither Fizz Nor Buzz on " + str(num))

	num += 1
