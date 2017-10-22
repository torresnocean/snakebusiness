# HUMBERTO TORRES
# CISW 24 LAB
# 09/22/2017
# PROGRAM 2


umber = ["KEY:"]
food = ["VALUE:"]

dic = None
print("No items")

insert = True
while(insert):
	add_name = input("Enter a NAME: ")
	add_food = input("Enter your favorite FOOD: ")

	if(add_name + add_food == ''):
		insert = False
	else:
		umber.append(add_name)
		food.append(add_food)
		
	print(umber)
	print(food)

dic = dict(zip(umber, food))

find = input("Search for a key inside the Dictionary: ")

while (find not in dic):
	find = input("Key not found, please try again..: ")
else:
	print("The KEY VALUE is : " + dic[find])