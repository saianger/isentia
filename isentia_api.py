import json
import bottle
from bottle import route, run, request, abort
from pymongo import MongoClient
 
import json
from bson import ObjectId

# compose mongo db connection
client = MongoClient('aws-us-east-1-portal.12.dblayer.com',10223)
client.isentia.authenticate('isentia', 'isentia')
db = client.isentia
 
# class for json encoder, to display json format in browser properly
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# Get method, find the document with articles has certain keyword
@route('/articles/:id', method='GET')
def get_document(id):
    # mongo db command to retrieve documents
    entity = db['articles'].find_one({'article':{'$regex':id}})
    # abort if no document is found
    if not entity:
        abort(404, 'No document with id %s' % id)
    # return the document been found
    return JSONEncoder().encode(entity)


# bulk search and disply, currently not working properly
#@route('/articles/:id', method='GET')
#def get_document(id):
#    entity = db['articles'].find_one({'article':{'$regex':id}})
#    if not entity:
#        abort(404, 'No document with id %s' % id)
#    entity_list = []
#    for e in entity:
#        entity_list.append(JSONEncoder().encode(e))
#	return str(entity_list)
	
run(host='localhost', port=8080)