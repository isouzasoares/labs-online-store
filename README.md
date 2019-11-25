# Labs store

[![Build Status](https://travis-ci.org/isouzasoares/labs-online-store.svg?branch=master)](https://travis-ci.org/isouzasoares/labs-online-store) [![codecov](https://codecov.io/gh/isouzasoares/labs-online-store/branch/master/graph/badge.svg)](https://codecov.io/gh/isouzasoares/labs-online-store)

## Installation guide

### Requirements

* Python3.7+
* Django2.2+
* [pipenv](https://pipenv.kennethreitz.org/en/latest/)


### Install project dependencies

**On the project root folder**, execute the following command:

`pipenv install --dev`


### Run the project locally

If your are running the application for the first time, you should do first:

`export DATABASE_URL=postgres://user:password@db:5432/database`

If you don`t configure the DATABASE_URL the system will use sqlite3.


To update the local database schema you can use:

`make migrate`

Create django admin superuser for you to register/delete/update products 

`make createsuperuser`


Now you are ready to run the application:

`make run`

You can confirm that the application is running properly checking the application's swagger url:

http://127.0.0.1:8000/api/swagger/


### Products administrator

To create products you can use django admin (Use your superuser login):

http://127.0.0.1:8000/admin/


### API NOTE

**For create customer, list products and get product the customer login is not necessary**


# Tests

### Running all unit tests

To run all unit tests with coverage:

`make test_cov`

or 

`make test`


### Docker
See installation instructions at: [docker documentation](https://docs.docker.com/install/)

### Docker Compose
Install [docker compose](https://github.com/docker/compose), see installation
instructions at [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

### Run project docker

`make docker_build`

You can confirm that the application is running properly checking the application's swagger url:

http://127.0.0.1:8000/api/swagger/



