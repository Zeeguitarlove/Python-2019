import os
os.system("clear")

####################################
# FizzBuzz
# divisible by 3 fizz
# divisible by 5 buzz
# divisibe by both fizzbuzz
####################################

num = 1
count_fizz = 0
count_buzz = 0
count_fizzbuzz = 0
count = 0

while (num <= 1000000):
	if(num % 3 ==0) and (num % 5 == 0):
		print("\nFizzBuzz on ",num)
		count_fizzbuzz += 1

	elif(num % 5 == 0):
		print("\nBuzz on ",num)
		count_buzz += 1

	elif(num % 3 == 0):
		print("\nFizz on ",num)
		count_fizz += 1
	else:
		print("\nNeither Fizz Nor Buzz on " + str("{:,}".format(num)))
		count += 1

	num += 1

print("\nTotal number of FizzBuzz are " + str("{:,}".format(count_fizzbuzz)))

print("\nTotal number of Fizz are " + str("{:,}".format(count_fizz)))

print("\nTotal number of Buzz are " + str("{:,}".format(count_buzz)))

print("\nTotal number of invaluable numbers are " + str("{:,}".format(count)))