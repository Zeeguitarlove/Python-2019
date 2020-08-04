import os
os.system('clear')

############################
# For Loops
############################

name = "zeeshaan"

for x in name:
	print(x)

name = ["John","Mary","Zee"]
for lists in name:
	print(lists)


fav_pizza = {
	"Zee": "Pepperoni",
	"John": "Mushroom",
	"Bob": "Cheese",
}

for key,value in fav_pizza.items():
	print(key + " likes" + value + " Pizza")
