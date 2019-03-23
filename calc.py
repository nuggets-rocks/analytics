import json
from pprint import pprint
pprint("hello world")
with open('Nugget.json') as f:
	data = json.load(f)
pprint(len(data['results']))

total = 0;
tags = 0;
#owner = 0;
ownerToNug = {}
for nugget in data['results']:
	if nugget.get('tags') is not None:
		tags+=1
	if nugget.get('owner') is not None:
		owner = nugget.get('owner')
		objectId = owner.get('objectId')
		if ownerToNug.get(objectId) is not None:
			# Owner entry exists. Add one to the existing count
			ownerToNug[objectId] = ownerToNug[objectId] + 1
		else:
			# Ownder never existed so set count as 1
			ownerToNug[objectId] =  1
#		owner+=1
	total+=1

for key in ownerToNug:
	pprint(key + "," + str(ownerToNug[key]))


pprint("total is " + str(total))
pprint("tags is " + str(tags))
pprint("% of nuggets with tags is " + str((tags*100)/total))	
