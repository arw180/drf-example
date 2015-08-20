#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE=example.settings

# remove existing database and all migrations
rm db.sqlite3
rm -r ozpcenter/migrations/*
# create new database with a single new migration
python manage.py makemigrations myapp
python manage.py migrate

python insert_test_data.py
python manage.py runserver 8082