#open db
#read and print all key/value pairs
#change objects
#save our changes
import shelve

dbName = input('Database name: ')
db = shelve.open(dbName)

#now db should be open and ready to use

for i in sorted(db):
	print(i, '->', db[i])

changeKey = input('Key of record to change: ')

s = db[changeKey]

# s.setFn(fn)
# s.setLn(ln)

save = input('Modify record? y/n')

if save == 'y':
	fn = input('new fn: ')
	ln = input('new ln: ')
	s.setNewStudent(fn, ln)
	db[changeKey] = s
	print(s)
else:
	print('Changes were not saved')

db.close()