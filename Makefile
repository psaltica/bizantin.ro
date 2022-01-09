migrate:
	$(PYTHON) src/manage.py makemigrations
	$(PYTHON) src/manage.py makemigrations collection
	$(PYTHON) src/manage.py migrate
	$(PYTHON) src/manage.py migrate --database=content

.PHONY: test
test:
	$(PYTHON) src/manage.py test collection

.PHONY: run
run:
	$(PYTHON) src/manage.py runserver
