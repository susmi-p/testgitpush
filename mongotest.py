import pymongo
client=pymongo.MongoClient("mongodb+srv://Susmitha:Susmitha @cluster0.cwphypd.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d = {
    "name" : "Susmitha",
    "email": "susmitha@gmail.com",
    "surname": "Penagalooru"
}
db1 = client['mongotest']
coll=db1['test']
coll.insert_one(d )


