#!/usr/bin/make -f
# -*- makefile -*-

PYTHONPATH := ${CURDIR}
export PYTHONPATH


all: help
help:
	@echo ""
	@echo "-- Help Menu"
	@echo ""
	@echo "   1. make clean 			- Clean all pyc and caches"
	@echo "   2. make run				- Run application locally"
	@echo "   3. make migrate 			- Run migrations"
	@echo "   4. make createsuperuser   - Create django superuser"
	@echo "   5. make test 			    - Run tests"
	@echo "   6. make test_cov 			- Run tests"
	@echo "   7. make black 			- Run black"
	@echo "   8. make flake8		    - Run flake8"
	@echo "   9. make docker_build		- Run docker compose build"
	@echo ""
	@echo ""


.PHONY: clean
clean:
	@echo "Clean files pyc and caches..."
	rm -rf build/ dist/ docs/_build *.egg-info
	find $(CURDIR) -name "*.py[co]" -delete
	find $(CURDIR) -name "*.orig" -delete
	find $(CURDIR)/$(MODULE) -name "__pycache__" | xargs rm -rf
	find $(CURDIR)/$(MODULE) -name ".pytest_cache" | xargs rm -rf


.PHONY: run
run:
	pipenv run python manage.py runserver


.PHONY: migrate
migrate:
	pipenv run python manage.py runserver migrate


.PHONY: black
black:
	pipenv run black -l 79 -t py37 . --exclude frontend


.PHONY: test
test:
	@echo $(PYTHONPATH)
		pipenv run pytest

.PHONY: test_cov
test_cov:
	pipenv run pytest --cov=. tests/ */tests/


.PHONY: test_cov_html
test_cov_html:
	pipenv run pytest --cov=. --cov-report term --cov-report=html tests/ */tests/


.PHONY: flake8
flake8:
	pipenv run flake8 --exclude */migrations,settings.py


.PHONY: createsuperuser
createsuperuser:
	@echo $(PYTHONPATH)
		pipenv run python manage.py createsuperuser


docker_build: ## Build the container
	docker-compose run web pipenv run python /app/manage.py migrate --noinput
	docker-compose run web pipenv run pytest --cov=. tests/ */tests/
	docker-compose up -d --build