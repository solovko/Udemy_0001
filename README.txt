** need start mongodb in terminal:
for UBUNTU 18... sudo service mongod start
------------------------------------------
verify that the mongod process has started successfully by checking the contents of the log file at
 /var/log/mongodb/mongod.log for a line reading :: [initandlisten] waiting for connections on port 27017

------------------------------------------
Stop MongoDB::
sudo service mongod stop
Restart MongoDB::
sudo service mongod restart
Start mongo shell::
mongo
Show existing DBs::
> show dbs
> use fullstack
switched to db fullstack
Add entry::
> db.students.insert({"name": "Jose", "mark":99})
WriteResult({ "nInserted" : 1 })
> db.students.find({})
{ "_id" : ObjectId("5c6fa0d73232e315eed404ef"), "name" : "Jose", "mark" : 99 }
> db.students.find({})
{ "_id" : ObjectId("5c6fa0d73232e315eed404ef"), "name" : "Jose", "mark" : 99 }
{ "_id" : ObjectId("5c6fb86d3232e315eed404f0"), "item" : "Chair", "price" : 99, "age" : 25 }
db.studens.remove({"item" : "Chair"})
### For the Posts collection
#--------------------------------
### finding path  and permissions
oleksandr@oleksandr-ThinkPad-X140e:~$ grep dbPath /etc/mongod.conf
  dbPath: /var/lib/mongodb
oleksandr@oleksandr-ThinkPad-X140e:~$ ls -ld /data/db/
drwxr-xr-x 4 root root 4096 Nov 25 22:35 /data/db/
oleksandr@oleksandr-ThinkPad-X140e:~$ sudo chmod 0755 /data/db && sudo chown $USER /data/db
################ Created collection befre adding lements to it
> db.createCollection("posts")
{ "ok" : 1 }
>
