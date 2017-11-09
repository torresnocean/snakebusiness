import shelve
#open db
#read and print all key/value pairs
#change objects
#save our changes

dbName = input('db name: ')
db = shelve.open(dbName)

#now db should be open and ready to use

for i in sorted(db):
	print(i, '->', db[i])

changeKey = input('key for record that we want to change: ')

s = db[changeKey]

fn = input('new fn: ')
ln = input('new ln: ')

# s.setFn(fn)
# s.setLn(ln)

s.setName(fn, ln)
print(s)

db[changeKey] = s

db.close()