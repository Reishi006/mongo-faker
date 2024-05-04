from pymongo.mongo_client import MongoClient
from exe_queries import exe_queries

uri = 'mongodb://localhost:27017/'

client = MongoClient(uri)
db = client['language-app']
collection = db['users']

try:
    client.admin.command('ping')
    print('\x1b[6;30;42m' +
          'Pinged your deployment. You successfully connected to MongoDB!' +
          '\x1b[0m')

    exe_queries(collection)
except Exception as e:
    print(e)
