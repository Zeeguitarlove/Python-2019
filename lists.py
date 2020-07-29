import os
os.system("clear")

#########################
# Lists in Python
#########################

names = [" Zee", "Bob","Tina",40]			# creating a list.

names[1] = "Wes"							# Replacing a list member

names.append("John")						# Adding a new member to the list.

print(names)								# Print the complete list

print(names[2])								# Printing a specific list member.

print(names[3] + 10)						# Adding list member with 10. This shows arithmatic operations can be done to list members.

other_names = "Elder"						# Using variables can alos be used
names = [" Zee", "Bob","Tina",40, other_names]
print(names)

nums = [1,2,3,4,5]
names = [" Zee", "Bob","Tina",40, nums]		# Can be used to access liosts in lists.
print(names)

nums = [1,2,3,4,5]
names = [" Zee", "Bob","Tina",40, nums]		# can be used to call the lists in a list.
print(names[4])

nums = [1,2,3,4,5]
names = [" Zee", "Bob","Tina",40, nums]		# can be used to call a list member in a list.
print(names[4][2])

nums = [1,2,3,4,5]
names = [" Zee", "Bob","Tina",40, nums]		# can be used to call a list member in a list and then do arithmatic operations on it too.
print(names[4][2] + 7)

names = [" Zee", "Bob","Tina"]				
print(len(names))							# NOTE:- Returns value starting from 1 and not 0.

names = [" Zee", "Bob","Tina"]				# If you want the last member in the list 
print(names[len(names)-1])					#  names[] for returning list member,
											# len names for length of string,-1 since len(names) starts from 1 and not 0.



