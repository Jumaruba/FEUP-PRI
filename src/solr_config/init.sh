#!/bin/bash

precreate-core books 
precreate-core authors
precreate-core reviews 

bin/solr start
# Give time to connect
sleep 4

# Schema definition via API
curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books/schema

# Populate collection
bin/post -c authors /data/authors.csv
bin/post -c books /data/books.csv
bin/post -c reviews /data/reviews.csv

solr restart -f