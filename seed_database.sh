#!/bin/bash

rm db.sqlite3
rm -rf ./api/migrations
python3 manage.py migrate
python3 manage.py makemigrations api
python3 manage.py migrate api
# python3 manage.py loaddata users
# python3 manage.py loaddata tokens
python3 manage.py loaddata pet_behaviors
python3 manage.py loaddata posts

# run this command to make this an executable script
# chmod u+x ./seed_database.sh

# this is the command to run the script
# ./seed_database.sh

