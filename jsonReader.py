import json
f = open('kr.json')
jsonArray = json.load(f)
for jsonObj in jsonArray:
    print unicode(jsonObj['title'][0]).encode("utf8")
    print unicode(jsonObj['description'][0]).encode("utf8")
    print ""