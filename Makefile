migrate:
	$(PYTHON) src/manage.py makemigrations
	$(PYTHON) src/manage.py migrate
	$(PYTHON) src/manage.py migrate --database=content

.PHONY: run
run:
	$(PYTHON) src/manage.py runserver
