Install
======

* cp *.csv src/var/
* python manage.py migrate
* python manage.py init_data # Only for first time deploying

Database
======
```
$ postgres -D /user/local/postgres  # Run as daemon
$ createdb dinner [password] 
$ dropdb dinner
$ pg_dump -U django(username) dinner(dbname) > dinner.export.sql ## Dumps data
$ psql -U mic(username) dinner(dbname) < dinner.export.sql  ## Import data
