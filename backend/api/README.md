# FastAPI Endpoints

## Content

* [About](#about)
* [Environment](#environment)
* [Directories](#directories)
* [Files](#files)


## About

This repository contains files and folders to
setup the backend of the API. One of the
required files are not present on here for
security reasons but an example will be shown
on how to setup an ebvironment with that.


## Environment

1. Install and create a PostgreSQL server locally
with the following command:

```
sudo apt update
sudo apt install postgresql
```

2. Start and create a user and db using [this](./create_db.sh)
script with the following command:

```
./create_db.sh
```
3. Create a [Mailtrap]((https://mailtrap.io) account
and copy the credentials from `SMTP Settings`.
It should look like this:

```
SMTP
Host: sandbox.smtp.mailtrap.io
Port: 25 or 465 or 587 or 2525
Username: ****
Password: ****
Auth: PLAIN, LOGIN and CRAM-MD5
TLS: Optional (STARTTLS on all ports)
```

4. Create a config.py file in the api directory
with the followinh content:

```
#!/usr/bin/python3
"""Module that defines configuration settings"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class that stores configuration items"""

    SECRET_KEY: str = "unkown-secret-key"
    ALGORITHM: str = "algorithm"
    MAIL_USERNAME: str = "mailtrap-username"
    MAIL_PASSWORD: str = "****"
    MAIL_FROM: str = "admin@afrilegal.com"
    MAIL_PORT: int = 465
    MAIL_SERVER: str = "smtp.mailtrap.io"
    MAIL_TLS: bool = True
    MAIL_SSL: bool = False
    USE_CREDENTIALS: bool = True
    ACCESS_TOKEN_DURATION_IN_MINUTES: float = 30.5
    REFRESH_TOKEN_DURATION_IN_MINUTES: float = 87000.5
    RESET_PASSWORD_SESSION_DURATION_IN_MINUTES: float = 1
    STATIC_DIR: str = None
    API_BASE_URL: str = 'http://0.0.0.0:8000'
    COMPANY_URL: str = 'https://www.afrilegalapi.com'
    START_URL: str = 'http://100.26.231.45:5445/forms/start'
    PASSWORD_URL: str = 'http://100.26.231.45:5445/forms/start'
    POSTGRES_USER: str = "****"
    POSTGRES_PASSWORD: str = "****"
    POSTGRES_DB: str = "db-name"
    POSTGRES_DOMAIN: str = ("postgresql://POSTGRES_USER:POSTGRES_PASSWORD@http://URL/POSTGRES_DB")

    class Config:
        title = 'Base Settings'
        env_file = '.env'


settings = Settings()
```

5. Run the application locally with the following command:
```
uvicorn main:app --reload
```

### Things to note

- A free [Mailtrap](https://mailtrap.io) account can be setup
to test the mailing implementation with fake emails

- PostgreSQL or any other database system shouldbe setup
and connected with credentials locally in order to run
the application. This means all `database.py` files
should be modified with the credentials pointing
to the correct database.

- Authenticated endpoints can be tested with [Postman](https://www.postman.com/)
but not with the swagger docs.


### Endpoints & URLs

Check the README.md files for the individual [routers](./routers)
directories for their endpoints and more details on each of them.



## Directories

1. [Routers](./routers) -> Contains multiple
folders of different secions of the backend
with their individual CRUD files to allow
growth in the backend.

2. [Services](./services) -> Contains extra
utilised by the backend like email and
allows any future services like payment
gateways that will be integrated into
the backend.

3. [Static](./static) -> Contains static
templates for emails that will be sent
from the application. This allows devs
to create email templates for situations
such as password reset, request for api-
keys or any future emails.


## Files

1. [Database](./datapase.py) -> Contains info on
database connection.

2. [Exceptions](./exceptions.py) -> Contains responses
to handle errors with the appropriate response codes.

3. [Main](./main.py) -> Contains the routers and
the entire api structure.

4. [Oauth2 Scheme](./oauth2.py) -> Contains the
algorith for authentication.

5. [Schedulers](./schedulers.py) - Contains functions
to schedule background tasks like sending emails in
the background.

6. [Sockets](./sockets.py) -> Contains algorithms
to handle access tokens/ api keys of users logged
in and curent web sessions.

7. [Utils](./utils.py) -> Contains functions that
handle generation and decoding of access tokens
and password reset codes.

8. [Test](./test_main.py) -> Contains unit tests
for the main file to ensure the application is
functioning well.

9. [Script to create database](./create_db.sh) -> Contains
commands to create a PostgreSQL database user, a database
and set appropriate passwords and permissions.

10. [Config file](./config.py) -> Contains user passwords
and secured information like PostgreSQL url, user and
password, mailtrap credentials and other environment
variables required for the application to function.
