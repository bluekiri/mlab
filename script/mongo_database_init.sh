#!/bin/bash

echo "Connecting to $MLAB_MONGO_HOST"
#echo 'db.testing.insert({_id:1, name:"a"});' | mongo mongodb://$MLAB_MONGO_HOST
mongorestore -d mlab
echo "Database initialized!"