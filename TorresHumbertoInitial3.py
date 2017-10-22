# PYHTON WEB
# CISW 24 LAB
# 10/16/2017
# PROGRAM 3


# Start Function

print("""
	Please enter some keys to create a dictionary.
	To end entering keys, enter a blank line.
	""")

# Get the Keys..

def createKeys(input_prompt, saved_keys):
	keys = input(input_prompt)
	while keys:
		saved_keys.append(keys)
		keys = input(input_prompt)


# Get the vales..

def createValues(input_prompt, saved_values):
	values = input(input_prompt)
	while values:
		saved_values.append(values)
		values = input(input_prompt)


list_keys = []
list_values = []
key_msg = 'Enter a key: '
value_msg = 'Enter a value: '

createKeys(key_msg, list_keys)

print("""
	Please enter some values to associate with the keys.
	To end entering values, enter a blank line.
	""")

createValues(value_msg, list_values)

# Making a dictionary..

d = dict(zip(list_keys, list_values))

# Let the user search for the values..

user_mgs = "\nEnter a key to look up it's values: "
search = input(user_mgs)
while search:
	if search in d:
		print("The value for", search, "is", d[search])
	else:
		print(search, "is not a key in our dictionary.")
	search = input(user_mgs)



# End of Function