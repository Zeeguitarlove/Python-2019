import os
os.system("clear")

#################################

# Function/Method

#################################

def nameit(first_name,last_name):
	print("Hello " + first_name + " " + last_name)

nameit("Zee","Noor")



def mathit1(num1,num2):
	print(num1 + num2)

mathit1(99999,1)


def mathit(num1,num2):
	return(num1 + num2)

print(mathit(9999,1))


def math(num1,num2):
	return (num1 + num2) 
outcome = math(999,1)					# All were doin here is assignin value of math() into outcome

print(outcome)							# Here is where were printing outcome which holds the value of math().




def math(num1,num2):
	return (num1 + num2) 
outcome = math(9,1)

print(outcome * 10)
