# Humberto Torres
# CISW 24 LAB
# 11/9/17
# Program 4

# open the database db
# read and print all key/value pairs in db
# change objects 
# then save

import shelve

dbName = input("Database name: ")
db = shelve.open(dbName)

# now db should be open and ready to use

for i in sorted(db):                                                                                                                 
    print(i, "->", db[i])

print()

changeKey = input("Insert the first name to make changes: ")
s = db[changeKey]

first_name = input("New First Name: ")
last_name = input("New Last Name: ")

s.setNames(first_name, last_name)
print("New changes has been made.. ")
print(s)

db[changeKey] = s


db.close()


# END of DATABASE FILE