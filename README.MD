## MOCKSERVER

MockServer is a powerful and flexible tool used to mock APIs, simulate servers, and create test environments for your applications. It allows developers to run integration tests without relying on external services or APIs, making it easier to test edge cases, failures, and specific conditions.

## Assumptions
This codebase uses sqlite3 by default

## Setup

- copy example.env to .env and update the file
- run migrate `python manage.py migrate`
- run server `python manage.py runserver`
