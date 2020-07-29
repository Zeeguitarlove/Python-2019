import os
os.system("clear")

#############################
# Tuplee in Python
#############################

names = ('Zee','Bob','Tina')						# () are used in tuples rather than []
print(names)

tuple1 = ('Zee','Bob','Tina')						# A hack to ADD a member in it. ps:- you cant do this the normal way since its a tuple
tuple2 = ("Mary",)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple1 = ('Zee','Bob','Tina')						# A hack to orint a range of member in it. 
tuple2 = ("Mary",)
tuple3 = tuple1[0:2]
print(tuple3)

tuple1 = ('Zee','Bob','Tina')						# A hack to print a member in it.
tuple2 = ("Mary",)
tuple3 = tuple1[0]
print(tuple3)
