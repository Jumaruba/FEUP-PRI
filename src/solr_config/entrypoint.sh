#!/bin/bash


RES_BOOK_CORE=`precreate-core books | grep "already exists"`

# MILESTONE 2
if [ -z $RES_BOOK_CORE ] && [ $MILESTONE -eq 2 ]
then 
    precreate-core books 
    precreate-core reviews 
    precreate-core books_subset_1   # Romantic tragedy
    precreate-core books_subset_2   # World war  
    precreate-core books_subset_3   # Science query
    precreate-core books_subset_4   # World war no filter
    precreate-core reviews_subset
    bin/solr start

    # Give time to connect
    sleep 4

    # COMPLETE SCHEMA ================
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books/schema
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/reviews/schema 
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books_subset_1/schema  
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books_subset_2/schema  
    # curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books_subset_3/schema 
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/reviews_subset/schema  

    cat /solr_config/synonyms.txt >> /var/solr/data/books/conf/synonyms.txt
    cat /solr_config/synonyms.txt >> /var/solr/data/reviews/conf/synonyms.txt
    cat /solr_config/synonyms.txt >> /var/solr/data/books_subset_1/conf/synonyms.txt  
    cat /solr_config/synonyms.txt >> /var/solr/data/books_subset_2/conf/synonyms.txt   
    cat /solr_config/synonyms.txt >> /var/solr/data/books_subset_3/conf/synonyms.txt   
    cat /solr_config/synonyms.txt >> /var/solr/data/reviews_subset/conf/synonyms.txt 

    # SIMPLE SCHEMA ==================
    #curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/books/schema
    #curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/reviews/schema 
    #curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/books_subset_1/schema   
    #curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/books_subset_2/schema   
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/books_subset_3/schema 
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/books_subset_4/schema  
    #curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema_simple.json http://localhost:8983/solr/reviews_subset/schema 

    # Populate collection
    bin/post -c books /data/books.csv
    bin/post -c reviews /data/reviews.csv
    bin/post -c books_subset_1 /data/books_subdataset_1.csv 
    bin/post -c books_subset_2 /data/books_subdataset_2.csv 
    bin/post -c books_subset_3 /data/books_subdataset_3.csv
    bin/post -c books_subset_4 /data/books_subdataset_4.csv
    bin/post -c reviews_subset /data/reviews_subdataset.csv
fi   

# MILESTONE 3 
if [ -z $RES_BOOK_CORE ] && [ $MILESTONE -eq 3 ]
then 
    precreate-core reviews    
    bin/solr start  
    
    # Give time to connect
    sleep 4

    # Add schema 
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/books/schema
    curl -X POST -H 'Content-type:application/json' --data-binary @/solr_config/schema.json http://localhost:8983/solr/reviews/schema 

    # Add synonyms 
    cat /solr_config/synonyms.txt >> /var/solr/data/books/conf/synonyms.txt
    cat /solr_config/synonyms.txt >> /var/solr/data/reviews/conf/synonyms.txt 

    # Populate collections
    bin/post -c books /data/books.csv
    bin/post -c reviews /data/reviews.csv 
fi 

solr restart -f
curl 'http://localhost:8983/solr/admin/cores?action=RELOAD&core=books'