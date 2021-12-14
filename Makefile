migrate:
	$(PYTHON) src/manage.py makemigrations
	$(PYTHON) src/manage.py migrate

.PHONY: run
run:
	$(PYTHON) src/manage.py runserver
