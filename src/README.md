Install
======

* cp *.csv src/var/
* python manage.py migrate
* python manage.py init_data

Database
======
```
$ postgres -D /user/local/postgres
$ createdb dinner
$ dropdb dinner

