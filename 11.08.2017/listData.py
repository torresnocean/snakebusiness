import shelve

db = shelve.open('testData')

for key in sorted(db):
	print(db[key])