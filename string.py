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
print(greetings7.upper())                                       # Here UPPER indicates that the whole string is not CAPITALIZED