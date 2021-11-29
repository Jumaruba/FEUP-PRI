#!/bin/bash

precreate-core books 

bin/solr start
# Give time to connect
sleep 4

# Schema definition via API
curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books/schema

# Populate collection
bin/post -c books /data/authors.csv


solr restart -f