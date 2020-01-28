run:
	python3 manage.py runserver 0.0.0.0:8000

db:
	python3 manage.py migrate

migration:
	python3 manage.py makemigrations
	python3 manage.py migrate

clean:
	find . -name "*.pyc" -delete

setup:
	pip3 install -r requirements.txt
	make run

shell:
	python3 manage.py shell_plus --traceback