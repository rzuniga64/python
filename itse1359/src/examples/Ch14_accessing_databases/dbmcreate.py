import dbm

db = dbm.open('websites', 'c')

# Add an item
db['www.python.org'] = 'Python home page'
db['www.wrox.com'] = 'Wrox home page'

# Verify the previous item remains
if db['www.python.org'] is not None:
    print('Found www.python.org')
else:
    print('Error: Missing item')

# Iterate over the keys.  May be slow and use a lot of memory
for key in db.keys():
    print('Key =', key, ' value = ', db[key])

del db['www.wrox.com']
print('After deleting www.wrox.com, we have:')

for key in db.keys():
    print('Key = ', key, 'value =', db[key])

# Close and save to disk
db.close()


