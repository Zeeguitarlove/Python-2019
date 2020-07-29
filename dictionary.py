import os 
os.system("clear")

############################
# Dictionary in python
############################

fav_pizza = {
	"Zee": "Pepperoni",
	"John": "Sausage",
	"Tim": "Cheese",
	69 : "Twisty Mandels",
	"Jimmy": [1,2,3,4,5],
}

del fav_pizza["Tim"]								# Delete a member
print(fav_pizza)

fav_pizza.update({"Tina":"Green Peppers"})			# Add a new member 
print(fav_pizza)

fav_pizza["John"] = "Margharita"					# Update an already existing member
print(fav_pizza)
 
print(fav_pizza["Jimmy"][2])						# Can use array and also print one from the list and also perform arithmatic operations on it.