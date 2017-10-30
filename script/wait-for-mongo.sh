#!/bin/bash

until echo "exit" | mongo mongodb://$MLAB_MONGO_HOST/$DATABASE_NAME ; do
    echo "Mongo is not available yet"
    sleep 1
done
echo "Mongo is UP!"

exec ./mongo_database_init.sh