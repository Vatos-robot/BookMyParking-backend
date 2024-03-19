

build:
	docker-compose build


build-no-cache:
	docker-compose build --no-cache


run-app:
	docker-compose up


makemigrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate
