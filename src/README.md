Install
======

* cp *.csv src/var/
* python manage.py migrate
* python manage.py init_data # Only for first time deploying

## Database
```
$ postgres -D /user/local/postgres  # Run as daemon Mac OSX: /usr/local/var/postgres
$ createdb dinner [password] 
$ dropdb dinner
$ pg_dump -U django(username) dinner(dbname) > dinner.export.sql ## Dumps data
$ psql -U mic(username) dinner(dbname) < dinner.export.sql  ## Import data

```
# 根据身份证查询生日
sql > update public_user
  set birthday = to_date(substring(idcard_no, 7, 8), 'yyyymmdd')
  where 1=1
```

## Test
```
$ python manage.py test
$ python manage.py show_urls
```

## Deploy
```
pip install -r requirements.txt

pip install supervisord
cp src/settings/supervisor.conf /etc/supervisor/conf.d/dinner.conf
supervisorctl reload
supervisorctl start dinner

cd src
python manage.py collectstatic
```