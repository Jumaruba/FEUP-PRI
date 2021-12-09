#!/bin/bash

precreate-core books 
precreate-core reviews 
precreate-core books_subset
bin/solr start

# Give time to connect
sleep 4

# COMPLETE SCHEMA ================
#curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books/schema
#curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/reviews/schema 
#curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books_subset/schema
#cat /solr_config/synonyms.txt >> /var/solr/data/books/conf/synonyms.txt
#cat /solr_config/synonyms.txt >> /var/solr/data/reviews/conf/synonyms.txt
#cat /solr_config/synonyms.txt >> /var/solr/data/books_subset/conf/synonyms.txt

# SIMPLE SCHEMA ==================
curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/books/schema
curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/reviews/schema 
curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/books_subset/schema 

# Populate collection
bin/post -c books /data/books.csv
bin/post -c reviews /data/reviews.csv
bin/post -c books_subset /data/subdataset.csv


solr restart -f
curl 'http://localhost:8983/solr/admin/cores?action=RELOAD&core=books'