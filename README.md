# IoT-Couchbase-Example
It reads sensors data from text files and saves to database.
There are 3 tables this example.
  1-)Objects 
  2-)Users
  3-)Sensors data

<b>First insert json files(users, objects) into database.</b> 

```sudo cbc create --mode insert user1 < user1.json -u your_username -P your_password -U couchbase://localhost/BucketName```

```sudo cbc create --mode insert user1 < user2.json -u your_username -P your_password -U couchbase://localhost/BucketName```

```sudo cbc create --mode insert user1 < object1.json -u your_username -P your_password -U couchbase://localhost/BucketName```

```sudo cbc create --mode insert user1 < object2.json -u your_username -P your_password -U couchbase://localhost/BucketName```

<b>Run command.</b>
```python couchbase-example.py```


