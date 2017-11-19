# Humberto Torres
# CISW 24 LAB
# 11/9/17
# Program 4

# open the database db
# read and print all key/value pairs in db
# change objects 
# then save

import shelve

dbName = input("Enter the Database name: ")
db = shelve.open(dbName)
print()
print("Registered Students: ")

# now db should be open and ready to use

for i in sorted(db):                                                                                                                 
    print(i, "->", db[i])

print()

changeKey = input("To edit, Please Type a name... or... press ENTER to exit: ")
s = db[changeKey]

first_name = input("New First Name: ")
last_name = input("New Last Name: ")

s.setNames(first_name, last_name)
print()
print("New changes has been made.. ")
print()
print(s)
db[changeKey] = s


print()
print("Thank You.. ")
print()

db.close()




# END of DATABASE FILE