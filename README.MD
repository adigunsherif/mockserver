## MOCKSERVER

MockServer is a powerful and flexible tool used to mock APIs, simulate servers, and create test environments for your applications. It allows developers to run integration tests without relying on external services or APIs, making it easier to test edge cases, failures, and specific conditions.

## Defaults

This codebase uses sqlite3 by default and works fine. However, you can change the db to use without touching the setting file.

In ur .env,:

- for mysql db, set `DB_ENGINE=django.db.backends.mysql` and other parameters. Uncomment mysqlclient in the requirements.txt file so that the package can be installed.
- for postgres, set `DB_ENGINE=django.db.backends.postgresql`.Uncomment psycopg in the requirements.txt file so that the package can be installed.
- for other dbs, check https://docs.djangoproject.com/en/5.1/ref/databases/

## Setup

- copy example.env to .env and update the file
- run migrate `python manage.py migrate`
- run server `python manage.py runserver`
- visit http://127.0.0.1:8000/ and login with `admin` and `admin`
