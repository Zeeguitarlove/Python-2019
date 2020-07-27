import os
os.system("clear")

##########################
# String
##########################

greetings1 = 'My boss yelled at me "GET BACK TO WORK"\n' 
print(greetings1)

greetings2 = "My boss yelled at me \"GET BACK TO WORK\"\n"      # Here "\" is called as an escape character i.e it escapes the very next character.
print(greetings2)

greetings3 = 'My boss yelled at me \n"GET BACK TO WORK"\n'      # Here "\n" helps to print a new line
print(greetings3)

greetings4 = 'My boss yelled at me \n\"GET BACK TO WORK\"\n'
print(greetings4)

greetings5 = 'My boss yelled at me \n\"GET BACK TO WORK\"\n'
print(greetings4)

job = ' WORK"\n' 
greetings6 = 'My boss yelled at me \n\"GET BACK TO' + job       # Here we learn how to concatenate and there is no neccissity to mention "job" in print it just has to be assigned. 
print(greetings5)                                               # Another note... ONLY STRINGS CAN BE CONCATINATED.(i.e not numbers,etc)

greetings7 = 'My boss yelled at me \n\"GET BACK TO WORK\"\n'
print(greetings7.upper())                                       # Here UPPER indicates that the whole string is not CAPITALIZED.

greetings8 = 'My boss yelled at me \n\"GET BACK TO WORK\"\n'    # First letter capital of all
print(greetings8.title())                                            

greetings9 = 'My boss yelled at me \n\"GET BACK TO WORK\"\n'    # The case gets swapped upper to lower and vice versa
print(greetings9.swapcase())  

greetings10 = 'My boss yelled at me \n\"GET BACK TO WORK\"\n'   # Returns the length of the string.
print(len(greetings10))

greetings11 = 'My boss yelled at me \n\"GET BACK TO WORK\"\n'   # Returns the exact character in string. PS:- it starts from 0th character
print(greetings11[5])

greetings12 = 'My boss yelled at me \n\"GET BACK TO WORK\"\n'   # Returns the range of characters lying between the mentioned range.
print(greetings12[3:7])

greetings13 = 'My boss yelled at me \"GET BACK TO WORK\"\n'   # Splits all the words with a space/gap.
print(greetings13.split(" "))

greetings13 = 'My boss yelled at me \"GET BACK TO WORK\"\n'   # Splits all the words with a space/gap to the specified allocations.
print(greetings13.split(" ")[1:6])
