# Daniel Ocean
# CISW 24 LAB
# 10/15/17
# Program 3

# GET KEYS FUNCTION
def getKeys(userInput, StorageList):
	process = input(userInput)
	while process:
		StorageList.append(process)
		process = input(userInput)

# GET VALUES FUNCTION
def getVals(userInput, StorageList):
	process = input(userInput)
	while process:
		StorageList.append(process)
		process = input(userInput)


listKeys = []
listValues = []
keysMessageForUser = "Enter a key: "
valuesMessageForUser = "Enter a value: "

print("""
Enter keys to create storage.
To end, enter a blank line.
""")

getKeys(keysMessageForUser, listKeys)

print("""
Enter values for your keys.
To end, enter a blank line.
""")

getVals(valuesMessageForUser, listValues)

#WE STOP AND COMBINE THE TWO VALUES INTO A DICTIONARY 
dictionaryZip = dict(zip(listKeys, listValues))

#FINALLY THE USER IS ABLE TO LOOKUP VALUES BY INPUTTING THE KEY
inputFromUser = '\nEnter a key to look up its value: '
searchKey = input(inputFromUser)
while searchKey:
    if searchKey in dictionaryZip:
        print('The value for', searchKey, 'is', dictionaryZip[searchKey])
    else:
        print(searchKey, 'is not a key in our dictionary.')
    searchKey = input(inputFromUser)



